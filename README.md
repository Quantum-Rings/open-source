# open-source
Community supported Quantum Rings projects.

# Toy Shor's Algorithm using QuantumRingsLib

This is a simplified demonstration of [Shor's Algorithm] using the QuantumRingsLib backend.  
It is designed for experimentation and education within the Quantum Rings environment.

## 💡 Features

- Modular exponentiation using approximated `cx`-based construction
- Lightweight inverse QFT (swap + Hadamard only)
- Avoids optimization to preserve phase interference
- Runs on QuantumRingsLib `scarlet_quantum_rings` backend

## 📦 Requirements

This script is intended to run in the Quantum Rings environment with the following:

- `QuantumRingsLib`
- Access to the `scarlet_quantum_rings` backend
- QuantumRings API token and email

## 🚀 Usage

1. Clone this repo and go to the directory:

   ```bash
   cd code/algorithms/shor
2. Edit the file shors_toy_qrings.py, replacing:
    token='YOUR_TOKEN'
    name='YOUR_EMAIL'
3. Run the algorithm:
    from shors_toy_qrings import shors_algorithm_toy
    shors_algorithm_toy(15)

