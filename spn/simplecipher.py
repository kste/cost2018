"""
Implementation of simple SPN.
"""


SBOX = [0xc, 0x6, 0x9, 0x0, 0x1, 0xa, 0x2, 0xb,
        0x3, 0x8, 0x5, 0xd, 0x4, 0xe, 0x7, 0xf]

INV_SBOX = [0x3, 0x4, 0x6, 0x8, 0xc, 0xa, 0x1, 0xe,
            0x9, 0x2, 0x5, 0x7, 0x0, 0xb, 0xd, 0xf]


def sub_bytes(state):
    """
    Compute SubCells of state.
    """
    return [SBOX[state[i]] for i in range(4)]

def inv_sub_bytes(state):
    """
    Compute the inverse of SubCells of state.
    """
    return [INV_SBOX[state[i]] for i in range(4)]

def mix_columns(state):
    """
    Compute MixColumns of state.
    """
    return [state[0] ^ state[2] ^ state[3], \
            state[0], \
            state[1] ^ state[2], \
            state[0] ^ state[2]]

def inv_mix_columns(state):
    """
    Compute the inverse of MixColumns of state.
    """
    return [state[1], \
            state[1] ^ state[2] ^ state[3], \
            state[1] ^ state[3], \
            state[0] ^ state[3]]

def encrypt(plaintext, key, rounds):
    """
    Encrypt plaintext with the secret key.
    """
    if len(key) != 4*(rounds + 1):
        print("ERROR: Key is to short.")
        return 0

    # Copy plaintext to state
    state = [val for val in plaintext]

    for rnd in range(rounds):
        # Add Key
        state = [state[i] ^ key[4*rnd + i] for i in range(4)]
        state = sub_bytes(state)
        state = mix_columns(state)

    # Add Key
    state = [state[i] ^ key[4*rounds + i] for i in range(4)]

    return state
