from random import randint
from enum import Enum

class basis(Enum):
    HV = 1
    DA = 0

class state(Enum):
    V = 1   # binary value 0
    A = 2   # binary value 0
    H = 3   # binary value 1
    D = 4   # binary value 1

def getBasis(state : state):
        return basis(state.value % 2)

def aliceSend(length : int):
    # create message of length
    message = [0]*length
    for i in range(0,length):
        message[i] = state(randint(1,4)) # initialize this bit in a random state {V,A,H,D}
    return message

def measure(value : int, measurementBasis : basis):
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
    
def bobRecv(message : list):
    recVal = []
    measureBases = []
    for val in message:
        myBasis = basis(randint(0,1)) # bob chooses which basis to measure in
        recVal.append(measure(val, myBasis))
        measureBases.append(myBasis)
    return (recVal, measureBases)

def aliceCompareBases(message : list, measurementBases : list):
    correctIndicies = []
    aliceKey = []
    for i in range(0, len(message)):
        if getBasis(message[i]) == measurementBases[i]:
            correctIndicies.append(i)
            aliceKey.append(measure(message[i], measurementBases[i]))
    return correctIndicies, aliceKey
            
def main():
    #alice send and records a message:
    message = aliceSend(10)
    recVal, measurementBases = bobRecv(message)
    sameBasisIndicies, aliceKey = aliceCompareBases(message, measurementBases)
    
    print("Alice sent: ", message)
    print("Measured in:", measurementBases)
    print("Bob's full string: ", recVal)
    print("Alice's Key: ", aliceKey)
    bobKey = []
    for i in sameBasisIndicies:
        bobKey.append(recVal[i])
    print("Bob's Key:   ", bobKey)
        
if __name__ == "__main__":
    main()