# Project 1

Our goal for this project is to investigate the quantum key distribution scheme BB84, developing a solid mathematical
and conceptual understanding. We will later apply these concepts towards specific applications relevant to government
and military communications in the form of later projects.

## Usage

Run `project_1.py`: `python3 project_1.py`. Follow the prompts, and see the results printed to the terminal.

## Example Output

First, enter configuration information. You are prompted for:

- The number of qubits Alice should initially transmit (the starting size of the key).
- How many times to repeat the simulation (to see how results change with the system's inherent randomness).
- Whether the final simulation's states and measurements should be shown, to let you see the details.

```
How long should Alice's message be? 4
How many times should the simulation be repeated? 1
Do you want to view each party's key and bases for the last iteration? (y/yes): y
```

When the simulation's details are shown, you see:

- Alice's original message, comprised of the initial key's states.
- Bob's chosen measurement bases.
- Bob's resulting intermediate result, based on his measurements of the received states.
- The final keys, determined by combining Bob's measurements with Alice's states and preserving the valid bits.

```
Alice sent:  [<State V (value=0)>, <State V (value=0)>, <State H (value=1)>, <State D (value=1)>]
Bob measured in: [<Basis DA>, <Basis HV>, <Basis HV>, <Basis HV>]
Bob's full string:  [0, 0, 1, 0]
Alice's key:  [0, 1]
Bob's Key:  [0, 1]
```

When running multiple simulations, the average key length may be of interest. This may help you determine the starting
key size to ensure you have a strong enough final shared key.

```
The average key length was:  2.0
```