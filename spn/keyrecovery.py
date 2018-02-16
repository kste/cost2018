"""
Example for key recovery using differential cryptanalysis for
simple SPN.

State is represented as 4 nibbles (x0, x1, x2, x3).
"""

from pairs import PT_CT_PAIRS
from simplecipher import inv_mix_columns, inv_sub_bytes

def print_state(state):
    """
    Print the state
    """
    for row in range(4):
        for col in range(4):
            print(hex(state[4*row + col]) + " ", end="")
        print("")

def diff(s1, s2):
    """
    Return the difference between two states
    """
    return [s1[i] ^ s2[i] for i in range(4)]


# Differential ((0x0, 0x1, 0x0, 0x0) -> (0x5, 0x0, 0x5, 0x5))

# 1) Guess parts of the secret key in last round.

# 2) Partially decrypt for each pair with guess.

# 3) Check if difference matches.

# 4) Recover last round key.
