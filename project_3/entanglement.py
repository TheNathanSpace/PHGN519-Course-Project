from qiskit import QuantumCircuit, transpile
import random
from qiskit_aer import AerSimulator


# Step 1: Entanglement generation
def create_single_qubit_circuit():
    circuit = QuantumCircuit(2, 2)
    circuit.h(0)
    circuit.cx(0, 1)
    return circuit


# Step 2: Measurement
def measure_particle(circuit, qubit: int, basis: int):
    if basis == 0:
        # Measure in the standard basis (0°)
        circuit.measure(qubit, qubit)
    elif basis == 1:
        # Measure in the Hadamard basis (45°)
        circuit.h(qubit)
        circuit.measure(qubit, qubit)
    elif basis == 2:
        # Measure in the Pauli X basis (90°)
        circuit.x(qubit)
        circuit.h(qubit)
        circuit.measure(qubit, qubit)
    return circuit


def simulate_circuit(circuit, shots: int = 1):
    backend = AerSimulator()
    transpiled_qc = transpile(circuit, backend)
    result = backend.run(transpiled_qc, shots = shots).result()
    return result


def run_single_bit():
    try:
        # Generate entanglement circuit
        shared_circuit = create_single_qubit_circuit()

        # Alice's measurement
        alice_basis = random.randint(0, 2)
        shared_circuit = measure_particle(shared_circuit, 0, alice_basis)

        # Bob's measurement
        bob_basis = random.randint(0, 2)
        shared_circuit = measure_particle(shared_circuit, 1, bob_basis)

        # Get results
        results = simulate_circuit(shared_circuit)
        counts = results.get_counts()
        bitstring = list(counts.keys())[0]
        alice_bit = bitstring[1]
        bob_bit = bitstring[0]

        return (alice_basis, bob_basis), (alice_bit, bob_bit)
    except Exception as e:
        print(f"Error in run_single_bit: {e}")
        return None, None


def e91_qkd():
    try:
        num_qubits = int(input("Enter number of qubits to transmit: "))
        if num_qubits <= 0:
            raise ValueError("Number of qubits must be a positive integer.")

        shared_bits = ""
        for i in range(num_qubits):
            bases, bits = run_single_bit()
            if bases is None or bits is None:
                print(f"Skipping iteration {i} due to an error.")
                continue

            if bases[0] == bases[1]:
                print(f"[{i}] Alice/Bob bases: {bases[0]} / {bases[1]} (shared bit: {bits[0]})")
                shared_bits += bits[0]
            else:
                print(f"[{i}] Alice/Bob bases: {bases[0]} / {bases[1]}")
        return shared_bits
    except ValueError as ve:
        print(f"Input error: {ve}")
        return ""
    except Exception as e:
        print(f"Unexpected error in e91_qkd: {e}")
        return ""


if __name__ == '__main__':
    bitstring = e91_qkd()
    print(f"\nFinal string: {bitstring}")
