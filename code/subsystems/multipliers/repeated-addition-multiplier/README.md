# Repeated-Addition (Shift-and-Add) Multiplier

### Concept

* The most straightforward approach: multiply 𝑎 by 𝑏 by repeatedly adding 𝑎 to an accumulator if the corresponding bit of 𝑏 is 1, while shifting.
* Often taught in classical computing courses as the simplest CPU-level multiplier, adapted to quantum by making ach addition reversible.

### Pros

* Easy to implement and reason about.
* Good for teaching or demonstration.

### Cons

* Not the most gate-efficient.
* Large circuit depth for bigger operands.