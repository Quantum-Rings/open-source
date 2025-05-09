from math import gcd, ceil, log2
from fractions import Fraction
import random
from collections import Counter

from QuantumRingsLib import (
    QuantumRingsProvider,
    QuantumRegister,
    ClassicalRegister,
    QuantumCircuit,
    job_monitor,
    OptimizeQuantumCircuit
)

def shors_algorithm_toy(N, n_count=8, max_trials=300):
    def modular_exponentiation(qc, base_qubits, output_qubits, a, N):
        """
        Encode |x⟩|0⟩ → |x⟩|a^x mod N⟩ using repeated squaring.

        Assumes len(base_qubits) is small, and output_qubits initialized to |1⟩
        """
        n = len(base_qubits)
        current = a % N
        for i in range(n):
            exp = pow(current, 2 ** i, N)
            bin_str = format(exp, f"0{len(output_qubits)}b")[::-1]
            for j, bit in enumerate(bin_str):
                if bit == '1':
                    qc.cx(base_qubits[i], output_qubits[j])


    def inverse_qft_simple(qc, q, qubit_indices):
        # Lightweight inverse QFT: uses only SWAP and Hadamard gates
        n = len(qubit_indices)
        for i in range(n // 2):
            qc.swap(q[qubit_indices[i]], q[qubit_indices[n - i - 1]])
        for i in range(n):
            qc.h(q[qubit_indices[i]])

    # Setup Quantum Rings provider and backend
    provider = QuantumRingsProvider(token='YOUR_TOKEN', name='YOUR_EMAIL')
    provider.active_account()
    backend = provider.get_backend("scarlet_quantum_rings")

    for trial in range(1, max_trials + 1):
        a = random.randint(2, N - 1)
        if gcd(a, N) != 1:
            print(f"✔ Found classically: {gcd(a, N)} * {N // gcd(a, N)} = {N} (a = {a})")
            return gcd(a, N), N // gcd(a, N), a, None

        print(f"Trial {trial}: Trying a = {a}")
        n_bits = ceil(log2(N))
        total_qubits = n_count + n_bits

        q = QuantumRegister(total_qubits, "q")
        c = ClassicalRegister(n_count, "c")
        qc = QuantumCircuit(q, c)

        # Apply Hadamard to counting register
        for i in range(n_count):
            qc.h(q[i])
        qc.x(q[n_count])  # Initialize target register to |1⟩

        # Apply toy modular exponentiation
       # Apply simplified modular exponentiation
        modular_exponentiation(
            qc,
            base_qubits=[q[i] for i in range(n_count)],
            output_qubits=[q[n_count + i] for i in range(n_bits)],
            a=a,
            N=N
        )


        # Apply simplified inverse QFT
        inverse_qft_simple(qc, q, list(range(n_count)))

        # Measure counting register
        for i in range(n_count):
            qc.measure(q[i], c[i])

        # Optimize and run circuit
        # OptimizeQuantumCircuit(qc)
        job = backend.run(qc, shots=1024)
        job_monitor(job)
        result = job.result()
        counts = result.get_counts()

        if not counts:
            print("⚠️ Warning: No measurement results returned. Skipping trial.")
            continue

        measured_raw = Counter(counts).most_common(1)[0][0]

        measured = ''.join(measured_raw) if isinstance(measured_raw, tuple) else measured_raw
        print("  ↪ Raw measurement:", repr(measured))

        try:
            phase = int(measured, 2) / (2 ** n_count)
        except ValueError:
            print("⚠️ Invalid measurement string. Skipping trial.")
            continue


        frac = Fraction(phase).limit_denominator(N)
        r = frac.denominator
        print(f"  ↪ Measured: {measured} → phase = {phase:.4f} → Estimated r = {r}")
from math import gcd, ceil, log2
from fractions import Fraction
import random
from collections import Counter

from QuantumRingsLib import (
    QuantumRingsProvider,
    QuantumRegister,
    ClassicalRegister,
    QuantumCircuit,
    job_monitor,
    OptimizeQuantumCircuit
)

def shors_algorithm_toy(N, n_count=8, max_trials=20):
    def modular_exponentiation(qc, base_qubits, output_qubits, a, N):
        """
        Encode |x⟩|0⟩ → |x⟩|a^x mod N⟩ using repeated squaring.

        Assumes len(base_qubits) is small, and output_qubits initialized to |1⟩
        """
        n = len(base_qubits)
        current = a % N
        for i in range(n):
            exp = pow(current, 2 ** i, N)
            bin_str = format(exp, f"0{len(output_qubits)}b")[::-1]
            for j, bit in enumerate(bin_str):
                if bit == '1':
                    qc.cx(base_qubits[i], output_qubits[j])


    def inverse_qft_simple(qc, q, qubit_indices):
        # Lightweight inverse QFT: uses only SWAP and Hadamard gates
        n = len(qubit_indices)
        for i in range(n // 2):
            qc.swap(q[qubit_indices[i]], q[qubit_indices[n - i - 1]])
        for i in range(n):
            qc.h(q[qubit_indices[i]])

    # Setup Quantum Rings provider and backend
    provider = QuantumRingsProvider(token='YOUR_NAME', name='YOUR_EMAIL')
    provider.active_account()
    backend = provider.get_backend("scarlet_quantum_rings")

    for trial in range(1, max_trials + 1):
        a = random.randint(2, N - 1)
        if gcd(a, N) != 1:
            print(f"✔ Found classically: {gcd(a, N)} * {N // gcd(a, N)} = {N} (a = {a})")
            return gcd(a, N), N // gcd(a, N), a, None

        print(f"Trial {trial}: Trying a = {a}")
        n_bits = ceil(log2(N))
        total_qubits = n_count + n_bits

        q = QuantumRegister(total_qubits, "q")
        c = ClassicalRegister(n_count, "c")
        qc = QuantumCircuit(q, c)

        # Apply Hadamard to counting register
        for i in range(n_count):
            qc.h(q[i])
        qc.x(q[n_count])  # Initialize target register to |1⟩

        # Apply toy modular exponentiation
       # Apply simplified modular exponentiation
        modular_exponentiation(
            qc,
            base_qubits=[q[i] for i in range(n_count)],
            output_qubits=[q[n_count + i] for i in range(n_bits)],
            a=a,
            N=N
        )


        # Apply simplified inverse QFT
        inverse_qft_simple(qc, q, list(range(n_count)))

        # Measure counting register
        for i in range(n_count):
            qc.measure(q[i], c[i])

        # Optimize and run circuit
        OptimizeQuantumCircuit(qc)
        job = backend.run(qc, shots=1024)
        job_monitor(job)
        result = job.result()
        counts = result.get_counts()

        if not counts:
            print("⚠️ Warning: No measurement results returned. Skipping trial.")
            continue

        measured_raw = Counter(counts).most_common(1)[0][0]

        measured = ''.join(measured_raw) if isinstance(measured_raw, tuple) else measured_raw
        print("  ↪ Raw measurement:", repr(measured))

        try:
            phase = int(measured, 2) / (2 ** n_count)
        except ValueError:
            print("⚠️ Invalid measurement string. Skipping trial.")
            continue


        frac = Fraction(phase).limit_denominator(N)
        r = frac.denominator
        print(f"  ↪ Measured: {measured} → phase = {phase:.4f} → Estimated r = {r}")

        if r % 2 == 0 and pow(a, r // 2, N) not in [1, N - 1]:
            x = pow(a, r // 2, N)
            factor1 = gcd(x - 1, N)
            factor2 = gcd(x + 1, N)
            if factor1 not in [1, N] and factor2 not in [1, N]:
                print(f"✅ Success! {factor1} * {factor2} = {N} (a = {a}, r = {r})")
                return factor1, factor2, a, r

        print("  ✖ Failed for this a.")

    print("❌ No non-trivial factors found after all trials.")
    return None, None, None, None

    if r % 2 == 0 and pow(a, r // 2, N) not in [1, N - 1]:
        x = pow(a, r // 2, N)
        factor1 = gcd(x - 1, N)
        factor2 = gcd(x + 1, N)
        if factor1 not in [1, N] and factor2 not in [1, N]:
            print(f"✅ Success! {factor1} * {factor2} = {N} (a = {a}, r = {r})")
            return factor1, factor2, a, r

        print("  ✖ Failed for this a.")

    print("❌ No non-trivial factors found after all trials.")
    return None, None, None, None
