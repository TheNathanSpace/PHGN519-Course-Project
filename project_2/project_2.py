from random import randint

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# Define bitstring type for convenience
bitstring = list[0 | 1]


def gen_bit_string(num_bits: int) -> bitstring:
    """Generate a list of bits (as integers, either 0 or 1) of size num_bits."""
    return [randint(0, 1) for _ in range(num_bits)]


def compare_bases(bases_1: bitstring, bases_2: bitstring) -> list[int]:
    """Return a list of indices where Alice's base and Bob's measurement base match."""
    return [i for i in range(len(bases_1)) if bases_1[i] == bases_2[i]]


def get_final_data(measured: bitstring, valid_bases: list[int]) -> bitstring:
    """Return the valid bits where Alice's and Bob's measurement bases matched."""
    return [measured[i] for i in valid_bases]


def encode_data(data: bitstring, bases: bitstring) -> QuantumCircuit:
    """"""
    # Create the quantum circuit with the proper number of qubits and classical bits
    circuit = QuantumCircuit(len(data), len(data))

    for i in range(len(data)):
        bases_bit = bases[i]
        data_bit = data[i]

        # 0/1 basis
        if bases_bit == 0:
            if data_bit == 0:
                # Qubit should be initialized at 0
                pass
            elif data_bit == 1:
                # Qubit should be initialized at 1
                circuit.x(i)
        # +/- basis
        elif bases_bit == 1:
            if data_bit == 0:
                # Qubit should be initialized at other basis' '0'
                circuit.h(i)
            elif data_bit == 1:
                # Qubit should be initialized at other basis' '1'
                circuit.x(i)
                circuit.h(i)

    return circuit


def measure_bits(circuit: QuantumCircuit, bases: bitstring):
    for i in range(len(bases)):
        base_bit = bases[i]

        if base_bit == 0:
            # Measure qubit i, storing it in classical bit i
            circuit.measure(i, i)
        elif base_bit == 1:
            # Apply Hadamard gate, flipping the basis of the qubit
            circuit.h(i)
            # Measure qubit i, storing it in classical bit i
            circuit.measure(i, i)

    # Prepare the simulator. This simulator has no noise (it is ideal).
    simulator = AerSimulator()

    # Run and get results
    result = simulator.run(circuit).result()
    counts = result.get_counts(circuit)
    # Return the measured bits
    return [int(ch) for ch in list(counts.keys())[0]][::-1]


if __name__ == '__main__':
    # length > 10 just means the output gets misaligned, but the functionality should still work fine
    length = 10

    # Generate starting data
    alice_bits: bitstring = gen_bit_string(length)  # The data Alice is encoding
    alice_bases: bitstring = gen_bit_string(length)  # The 'correct' bases Alice uses to measure the data
    bob_bases: bitstring = gen_bit_string(length)  # The bases Bob uses to measure the data

    # Encode the data as qubits in the circuit
    circuit: QuantumCircuit = encode_data(alice_bits, alice_bases)

    # Measure the qubits with Bob's chosen bases
    bob_measured: bitstring = measure_bits(circuit, bob_bases)

    # Determine the matching bases and get the results
    matching_bases: list[int] = compare_bases(alice_bases, bob_bases)
    final_data = get_final_data(bob_measured, matching_bases)

    # Output results
    print(f"Alice bases:            {alice_bases}")
    print(f"Bob bases:              {bob_bases}")

    matching_viz = ""
    for i in range(length):
        if i in matching_bases:
            matching_viz += "^  "
        else:
            matching_viz += "   "
    print("                         " + matching_viz)

    matching_nums = ""
    for i in range(length):
        if i in matching_bases:
            matching_nums += f"{i}, "
        else:
            matching_nums += "   "
    print(f"Matching base indices:  [{matching_nums[:-2]}]")
    print()
    print(f"Alice bits:             {alice_bits}")
    print(f"Bob measured:           {bob_measured}")
    print("                         " + matching_viz)
    print()
    print(f"Final data, agreed upon by both Alice and Bob: {final_data}")
