# Carry-Lookahead or Parallel Multipliers (Quantum Adaptations)

### Concept

* In classical computing, we use carry-lookahead techniques to reduce carry-propagation time.
* The quantum analog aims to parallelize or reduce the overhead of successive carry bits.
* Some references adapt “Wallace tree” or other parallel classical multipliers to a quantum circuit.

### Pros

* Potentially lower circuit depth than naive ripple-carry-based multipliers.
* Good for large integer multiplication where speed is key.

### Cons

* Usually complex to design in a fully reversible manner.
* May require more ancillas.