# Demonstration of the usage of the BB84 protocol
# based on Quantum Communication iwth photons by Krenn et al.
# largely using section 1.6 Quantum Key Distribution

from enum import Enum
from random import randint


# Enum to represent the basis types for measurements
class Basis(Enum):
    HV = 1  # Horizontal/Vertical basis
    DA = 0  # Diagonal/Anti-Diagonal basis

    def __str__(self):
        return f"<Basis {self.name}>"

    def __repr__(self):
        return str(self)


# Enum to represent the possible states {V, A, H, D}
class State(Enum):
    V = 1  # Vertical state (0)
    A = 2  # Anti-Diagonal state (0)
    H = 3  # Horizontal state (1)
    D = 4  # Diagonal state (1)

    def __str__(self):
        value = 0 if self in [State.V, State.A] else 1
        return f"<State {self.name} (value={value})>"

    def __repr__(self):
        return str(self)


# Helper function to return the basis of a given state
def get_basis(state: State):
    return Basis(state.value % 2)


# Simulate Alice randomly choosing a state to create a message
def alice_send(message_length: int):
    return [State(randint(1, 4)) for _ in range(message_length)]


# Simulate the measurement of received information in a given basis
def measure(value: State, measurement_basis: Basis):
    if measurement_basis == Basis.HV:
        return 1 if value == State.H else 0
    elif measurement_basis == Basis.DA:
        return 1 if value == State.D else 0


# Simulate Bob receiving a message and choosing a basis for measurement
def bob_receive(message: list):
    received_values = []
    measurement_bases = []
    for value in message:
        chosen_basis = Basis(randint(0, 1))  # Bob chooses which basis to measure in
        received_values.append(measure(value, chosen_basis))
        measurement_bases.append(chosen_basis)
    return received_values, measurement_bases


# simulate Bob telling Alice which basis he measured in
# and Alice returning which basis matched up with how she sent the message
def alice_compare_bases(message: list, measurement_bases: list):
    correct_indices = []
    alice_key = []
    for i in range(len(message)):
        if get_basis(message[i]) == measurement_bases[i]:
            correct_indices.append(i)
            alice_key.append(measure(message[i], measurement_bases[i]))
    return correct_indices, alice_key


# Main entry point for the simulation
def main():
    # ask the user to input the length of Alice's message
    # ask the user to input how many times the simulation should be repeated for averaging
    # ask the user if they want to print out one iteration of each users key/basis used
    length = 0
    iterations = 0
    while True:
        try:
            message_length = int(input("How long should Alice's message be? "))
            iterations = int(input("How many times should the simulation be repeated? "))
            if message_length <= 0 or iterations <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter positive integers. Try again.")

    print_final_key = input("Do you want to view each party's key and bases for the last iteration? (y/yes): ")
    print()

    # repeat in a loop of the specified length to get an average resulting key length
    total_matching_indices = 0
    for i in range(iterations):
        # Alice sends a message
        message = alice_send(message_length)
        # Bob receives Alice's message
        received_values, measurement_bases = bob_receive(message)
        # Bob communicates which bases he measured in,
        # Alice informs Bob which matched up with her sending bases
        same_basis_indices, alice_key = alice_compare_bases(message, measurement_bases)
        total_matching_indices += len(same_basis_indices)

        if print_final_key in ["yes", "y"] and i == iterations - 1:
            print("Alice sent: ", message)
            print("Bob measured in:", measurement_bases)
            print("Bob's full string: ", received_values)
            print("Alice's key: ", alice_key)
            bob_key = [received_values[i] for i in same_basis_indices]
            print("Bob's key: ", bob_key)

    print()
    print("The average key length was: ", total_matching_indices / iterations)


if __name__ == "__main__":
    main()
