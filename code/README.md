# Quantum Rings Code Examples

A curated collection of quantum‑computing examples targeting the **Quantum Rings** backend.  Whether you’re illustrating an algorithmic concept or benchmarking performance, all code here is designed to run on Quantum Rings.

---

## Quantum Rings SDKs

- **QuantumRingsLib** (core)  
  Direct, low‑level access to Quantum Rings backends. Stable and minimal.

- **quantumrings.toolkit.qiskit**  
  Build your circuits with Qiskit’s `QuantumCircuit` API, then dispatch to Quantum Rings.  Leverages Qiskit’s ecosystem, but follows its release schedule.

- **quantumrings.toolkit.cudaq** *(coming soon)*  
  Write GPU‑accelerated quantum kernels with cudaQ and execute them on Quantum Rings’ GPU backends.

> _Use the core `QuantumRingsLib` API for the simplest, most stable integration; opt into the “toolkit” modules if you need Qiskit or CUDAQ support._

---

## Example Guidelines

Each example should:

1. **Name** the file with a descriptinve name.
2. **Target** the Quantum Rings backend via one of the SDKs above.  
3. **Document** its environment (OS + version, Python version, SDK versions) and any known conflicts.  
4. **Describe**  
   - **Concept/Goal**: What algorithmic idea or performance metric is being demonstrated?  
   - **Usage**: How to install dependencies, run the example, and verify results.  
5. **Be self‑contained**: Include all code, comments, and minimal instructions so a newcomer can pick it up and run immediately.  The code can import modules from the subsystems or other folders.

---

## Contributing

We welcome fixes, new examples, and improvements:

1. **Fork** the repo and create a descriptive feature branch.  
2. **Write** your code or documentation, following the Example Guidelines above.  
3. **Test** locally to ensure it runs on Quantum Rings.  
4. **Commit** with a clear message and push your branch.  
5. **Open a Pull Request** against `main`—we’ll review, iterate, and merge.

See [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## Code of Conduct

Be friendly, supportive, and constructive.  Help us keep this project welcoming—thanks for being courteous and professional.

---

## License

All examples and documentation are released under the **MIT License**.  
