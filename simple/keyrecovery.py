"""
Example for key recovery using differential cryptanalysis for
simple cipher.
"""

from pairs import PT_CT_PAIRS
from simplecipher import SBOX, INV_SBOX

# Differential (0x1 -> 0x5)

# 1) Guess the secret key in last round.

# 2) Partially decrypt for each pair with guess.

# 3) Check if difference matches.

# 4) Recover last round key.
