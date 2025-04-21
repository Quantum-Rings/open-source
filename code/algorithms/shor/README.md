# Shor's Algorithm

This folder hosts our implementation(s) of **Shor’s Algorithm** for integer factoring on a quantum computer. Shor’s algorithm famously demonstrates an exponential speedup over the best-known classical factoring algorithms under ideal conditions, making it a cornerstone example of quantum computing’s disruptive potential.

## 1. Overview of Shor’s Algorithm

- **Goal**: Factor a composite integer \\( N \\) into its prime factors using quantum phase estimation and modular arithmetic.
- **Key Components**:
  1. **Quantum Phase Estimation (QPE)**: Uses the [Quantum Fourier Transform](https://en.wikipedia.org/wiki/Quantum_Fourier_transform) (QFT) to estimate the order of \\( a \\) modulo \\( N \\).
  2. **Modular Exponentiation**: A sequence of controlled multiplications and modular reductions, typically built from lower-level circuits like _adders_ and _multipliers_.
  3. **Classical Post-Processing**: Once you measure a candidate for the period (the order), you use classical gcd checks to extract factors.

In practice, we break these tasks into smaller _building blocks_ (e.g., QFT, modular multiplication) that are reusable in many quantum algorithms.

---

## 2. Folder Structure

shor/
 ├── README.md <-- You are here. 
 ├── src/ 
 │ ├── shor_naive.py <-- A straightforward, reference implementation. 
 │ ├── shor_optimized.py <-- An optimized version using advanced tricks. 
 │ ├── shor_utils.py <-- Common helpers (gcd, continued fractions, etc.). 
 │ └── init.py <-- (Optional) Makes this a Python package. 
 └── notebooks/ 
   ├── shor_demo.ipynb <-- Jupyter notebook demonstration (naive). 
   └── advanced_shor_comparison.ipynb

- **`shor_naive.py`**: Demonstrates a classical approach to assembling Shor’s algorithm with basic building blocks (ripple-carry adders, standard QFT, etc.).  
- **`shor_optimized.py`**: A more advanced or “shortcut” approach (e.g., approximate QFT, windowed modular exponentiation).  
- **`shor_utils.py`**: Shared functions (e.g., classical gcd, continued fraction solvers, small prime checks, etc.).  

The **`notebooks/`** subfolder provides interactive tutorials and comparisons.

---

## 3. How the Code Orchestrates Subsystems

Code can be self contained examples or call in any of the available helper code.

Include code header describing the impmenentation.  Also include the tested module versions.

We delegate core arithmetic operations—like adders, multipliers, and modular arithmetic—to our `[subsystems](../subsystems)` folder. For example:

- **QFT**: Imported from `subsystems/qft/` (e.g., `from subsystems.qft.qft import qft_circuit`).
- **Adders/Multipliers**: From `subsystems/adders/` or `subsystems/multipliers/`.  
- **Modular Arithmetic**: From `subsystems/modular/` (e.g., `modexp.py`, `modular_multiply.py`).

### Example Flow (Naive Version)

1. **Register Setup**: Allocate qubits for QPE, and a “work” or “value” register to hold the modular states.
2. **Superposition**: Place the “exponent” register in superposition (`Hadamard` gates).
3. **Modular Exponentiation**: For each qubit in the exponent register, conditionally multiply the “work” register by \\( a^{2^i} \mod N \\).  
4. **Inverse QFT**: Apply the inverse QFT on the exponent register.
5. **Measurement**: Measure the exponent register to obtain the periodic information.
6. **Classical Post-Processing**: Compute gcd and check for nontrivial factors.

Each step calls into building blocks—e.g., `qft_circuit()`, `modular_multiply()`, or specific adder gates.

### Optimizations (Optimized Version)

- **Approximate QFT**: Reduces the number of small-phase gates.  
- **Windowed Exponentiation**: Splits exponent bits into chunks to reduce gate depth.  
- **Non-reversible Adders**: Potentially lowers gate counts at the cost of more ancilla management.

These improvements swap in different subsystem modules with minimal changes to the orchestration logic.

---

## 4. Usage / How to Run

**Example (Naive Implementation)**

```
cd algorithms/shor
python src/shor_naive.py --N 15 --a 2
```
This might print logs about the circuit construction, run a simulator, or query a quantum backend, then output found factors. For more usage details:

```
python src/shor_naive.py --help
```
Example (Optimized Implementation)

```
cd algorithms/shor
python src/shor_optimized.py --N 21 --a 2
```
Adjust flags if needed to select approximate QFT, window size, etc.

5. Notebooks and Demos
shor_demo.ipynb: Walks through Shor’s algorithm step by step, visualizing the circuit and measuring an example like \( N=15 \).

advanced_shor_comparison.ipynb: Compares naive vs. approximate QFT in terms of circuit depth, gate count, or runtime performance.

Open these notebooks in Jupyter or JupyterLab to interactively run them and see plots or circuit diagrams.

6. Extending or Contributing
Try new adders or multipliers: Implement them in subsystems/adders/ or subsystems/multipliers/, then import them in your Shor version to see how they impact performance.

Add more shortcuts: If you find a new trick for modular exponentiation or QFT optimization, you can create a new file (e.g., shor_experimental.py) and highlight the changes in README.md.

Notebook tutorials: If you develop a step-by-step explanation or advanced Shor variations, add a new notebook in the notebooks/ folder.

We welcome pull requests and feedback—see the CONTRIBUTING.md in the main docs/ folder for style guidelines and helpful references.

7. References
A few key references on Shor’s algorithm and relevant optimizations:

Peter W. Shor, “Algorithms for quantum computation: discrete logarithms and factoring,” Proceedings 35th Annual Symposium on Foundations of Computer Science, 1994.

Thomas G. Draper, “Addition on a Quantum Computer,” arXiv:quant-ph/0008033, 2000.

Beauregard, S. (2003). “Circuit for Shor’s Algorithm Using 2n+3 Qubits.” arXiv:quant-ph/0205095.

Nielsen & Chuang, Quantum Computation and Quantum Information, 10th Anniversary Edition.

For a deeper dive into the building blocks, see subsystems/README.md and the docs in each subfolder (adders, multipliers, qft, etc.).

Enjoy exploring Shor’s algorithm! If you have questions or want to propose an improvement, feel free to open an issue or start a discussion in this repository.

---

### Final Tips

- Adjust *paths*, *filenames*, and *scripts* to match your actual code.
- Add or remove **sections** to reflect your project’s real content—e.g., if you only have `shor.py` with a single approach, or if you have multiple advanced versions, rename them accordingly.
- Include **build instructions** or **installation steps** (like `conda` environment usage) if relevant to running Shor’s code in your environment.





