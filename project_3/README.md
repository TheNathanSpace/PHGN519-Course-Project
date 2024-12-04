# Project III

## Group: Qdoba

### Description

For our code, we implemented the E91 algorithm in the Qiskit quantum programming framework. The E91 protocol works by
sending entangled photons to two parties, Alice and Bob. Alice and Bob then measure their respective qubits in a random
basis. If they choose the same basis, they know they have a shared measurement result, and can use it to generate a
shared key.

### Usage

The implementation dependencies can be installed with `pip install -r requirements.txt`. The implementation can be run
with `python entanglement.py`.

Example output:

```
Enter number of qubits to transmit: 6
(0) Alice/Bob bases: 2 / 0
(1) Alice/Bob bases: 0 / 0 (shared bit: 1)
(2) Alice/Bob bases: 2 / 2 (shared bit: 0)
(3) Alice/Bob bases: 0 / 2
(4) Alice/Bob bases: 0 / 0 (shared bit: 1)
(5) Alice/Bob bases: 1 / 1 (shared bit: 1)

Final string: 1011
```

In this execution of the E91 implementation, 6 entangled quantum systems were instantiated, and so Alice and Bob each
received 6 entangled qubits. They each chose one of three random bases to measure each qubit in, and then, after
measuring, compared bases. If they each chose the same bases, their shared measurement is added to the final string,
which can then be used to generate a key.
