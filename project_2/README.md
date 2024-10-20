# Project 2 Code

For Project 2, we implemented the BB84 protocol in the Qiskit framework. By implementing it in Qiskit, it's now one step
closer to being able to run on a physical quantum computer—for now, though, we just use Qiskit's built-in simulators to
simulate using the BB84 protocol.

Our implementation follows the following structure:

1. Generate Alice's bits to be transmitted.
2. Generate Alice's bases to be used to encode the bits.
3. Generate Bob's bases to measure the encoded bits.
4. Measure the encoded bits using Bob's bases.
5. Compare Bob's measurement bases with Alice's encoding bases.
6. Determine the resulting agreed-upon bits.

The Qiskit simulation we use runs without any simulated noise; it is an ideal quantum computer.

## Usage

Install requirements (Qiskit dependencies) with `pip install -r requirements.txt`.

Run the Project 2 code with `python project_2.py`.

## Example Output

First, we see the bases, chosen individually by Alice and Bob. We see which ones match (the matching bases will be used
to determine and agree on the final data).

```
Alice bases:            [1, 1, 1, 1, 0, 1, 0, 0, 0, 1]
Bob bases:              [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
                         ^     ^  ^  ^                 
Matching base indices:  [0,    2, 3, 4,              ]
```

Then, we see the measured values. We see:

- The full list of bits that Alice transmits encoded as qubits.
- The full list of bits that Bob measures.
- Which bits Bob measured in Alice's chosen base—these make up the final result.

```
Alice bits:             [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
Bob measured:           [1, 0, 1, 1, 0, 0, 0, 0, 0, 0]
                         ^     ^  ^  ^                 
```

Putting all this together, we can see the final data that Alice and Bob agree on.

```
Final data, agreed upon by both Alice and Bob: [1, 1, 1, 0]
```

### All Together

```
Alice bases:            [1, 1, 1, 1, 0, 1, 0, 0, 0, 1]
Bob bases:              [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]
                         ^     ^  ^  ^                 
Matching base indices:  [0,    2, 3, 4,              ]

Alice bits:             [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
Bob measured:           [1, 0, 1, 1, 0, 0, 0, 0, 0, 0]
                         ^     ^  ^  ^                 
Final data, agreed upon by both Alice and Bob: [1, 1, 1, 0]
```
