# Demonstration of the usage of the BB84 protocol
# based on Quantum Communication iwth photons by Krenn et al.
# largely using section 1.6 Quantum Key Distribution

from enum import Enum
from random import randint


# create a Enum to make usage of the H/V and D/A basis more readable
class basis(Enum):
    HV = 1  # horizontal/vertical basis
    DA = 0  # Diagonal/Anti-Diagonal Basis


# create a Enum to make usage of each possible state {V, A, H, D} more readable
class state(Enum):
    V = 1  # binary value 0
    A = 2  # binary value 0
    H = 3  # binary value 1
    D = 4  # binary value 1


# readability helper function
# returns the basis of a given state
def getBasis(state: state):
    return basis(state.value % 2)


# simulate Alice randomly choosing a state to create a message in
def aliceSend(length: int):
    # create message of length
    message = [0] * length
    for i in range(0, length):
        message[i] = state(randint(1, 4))  # initialize this bit in a random state {V,A,H,D}
    return message


# simulate the measuring of received information in a given basis
def measure(value: int, measurementBasis: basis):
    if measurementBasis == basis.HV:
        if value == state.H:
            return 1
        else:
            return 0
    elif measurementBasis == basis.DA:
        if value == state.D:
            return 1
        else:
            return 0


# simulate Bob receiving a message and having to choose a basis to measure each value in
def bobRecv(message: list):
    recVal = []
    measureBases = []
    for val in message:
        myBasis = basis(randint(0, 1))  # Bob chooses which basis to measure in
        recVal.append(measure(val, myBasis))
        measureBases.append(myBasis)
    return (recVal, measureBases)


# simulate Bob telling Alice which basis he measured in
# and Alice returning which basis matched up with how she sent the message
def aliceCompareBases(message: list, measurementBases: list):
    correctIndicies = []
    aliceKey = []
    for i in range(0, len(message)):
        if getBasis(message[i]) == measurementBases[i]:
            correctIndicies.append(i)
            aliceKey.append(measure(message[i], measurementBases[i]))
    return correctIndicies, aliceKey


# main entry point for the simulation
def main():
    # ask the user to input the length of Alice's message
    # ask the user to input how many times the simulation should be repeated for averaging
    # ask the user if they want to print out one iteration of each users key/basis used
    length = 0
    iterations = 0
    while True:
        lengthStr = input("How long of message should Alice send: ")
        iterationsStr = input("How many times should the simulation be repeated: ")
        try:
            length = int(lengthStr)
            iterations = int(iterationsStr)
            if length <= 0 or iterations <= 0:
                raise ValueError
            break
        except ValueError:
            print("Please enter a positive integer. Try again")
    printFinalKey = input("Do you want to view each parties key and bases for the last iteration? (y/yes): ")

    # repeat in a loop of the specified length to get an average reulting key length
    sum = 0
    for i in range(0, iterations):
        # Alice send and records a message:
        message = aliceSend(length)
        # Bob recieves Alice's message
        recVal, measurementBases = bobRecv(message)
        # Bob communicates which bases he measured in, 
        # Alices informs Bob which matched up with her sending bases
        sameBasisIndicies, aliceKey = aliceCompareBases(message, measurementBases)
        sum += len(sameBasisIndicies)
        if printFinalKey in ["yes", "y"] and i == iterations - 1:
            # print results on the last iteration to see an example
            print("Alice sent: ", message)
            print("Bob measured in:", measurementBases)
            print("Bob's full string: ", recVal)
            print("Alice's key: ", aliceKey)
            bobKey = []
            for i in sameBasisIndicies:
                bobKey.append(recVal[i])
            print("Bob's Key:   ", bobKey)

    print("The average key length was: ", sum / iterations)


if __name__ == "__main__":
    main()
