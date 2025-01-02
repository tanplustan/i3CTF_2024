import string
import hashlib
from Crypto.Util.number import bytes_to_long, long_to_bytes


enc = b"\x12\x16\x0b\x1c&\x11\x18&\x1f\x15\x18\x1e&\x1d\x1c\n\x0c&\x18\x17\x18\r\x18&\x11\x18&\r\x18\x1d\x16\x0b\x10&\r\x0c\x10\r\x18&\x17\x16&\x1d\x18&?58>\x02\x03J\x1b\x0bM\n&\x18\x0bJ&\x18\x15\nI&\x01I\x0b\x04"
hash = "50806af7b4cb65abe94969ce3a3f8792d8205bb250b12117e56dcd79b048205aa74d7087ed1984e8a8d071ce9606f9e56e9cd1a5ebd19057a47d49a3c2ee291b"

for i in string.printable:
    key = i.encode()
    dec = b""

    for j in range(len(enc)):
        a = enc[j] ^ bytes_to_long(key)
        dec += long_to_bytes(a)

    if hashlib.blake2b(dec).hexdigest() == hash:
        print(dec)
        exit()
