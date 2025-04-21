# Space‑Efficient & Noise‑Robust Quantum Factoring  
*(Ragavan & Vaikuntanathan)*

An improved variant of Regev’s quantum factoring algorithm that achieves the “best of both worlds” by  
1. **Reducing qubit overhead** to \(O(n\log n)\) while keeping gate count \(\tilde O(n^{3/2})\), via **reversible Fibonacci‑chain exponentiation**, and  
2. **Tolerating noisy runs** by **filtering out** corrupted period samples through lattice‑reduction diagnostics.

---

## Environment & Dependencies

- **Python**: 3.11  
- **QuantumRingsLib**: 0.10.0  
- **Operating System**: Windows 11 (or equivalent Linux/macOS/Windows)

---

## References

* [Space‑Efficient and Noise‑Robust Quantum Factoring](https://arxiv.org/abs/2310.00899), *Seyoon Ragavan, Vinod Vaikuntanathan* (2023) :contentReference[oaicite:0]{index=0}  
* [An Efficient Quantum Factoring Algorithm](https://arxiv.org/abs/2308.06572), *Oded Regev* (2023) :contentReference[oaicite:1]{index=1}  
* [Targeted Fibonacci Exponentiation](https://arxiv.org/abs/1711.02491), *Burton S. Kaliski Jr.* (2017) :contentReference[oaicite:2]{index=2}  
* [A new quantum ripple‑carry addition circuit](https://arxiv.org/abs/quant-ph/0410184), *Steven A. Cuccaro, Thomas G. Draper, Samuel A. Kutin, David Petrie Moulton* (2004) :contentReference[oaicite:3]{index=3}  
