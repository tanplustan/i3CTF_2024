from Crypto.Util.number import *

n = 89765553359668267846115148791526510167
e = 65537
c = 43726401623720020767763547639229741559
p = 7188697477892891021
q = 12487040056383040627

phi = (p - 1) * (q - 1)
d = pow(e, -1, phi)
m = pow(c, d, n)
print(long_to_bytes(m).decode())
