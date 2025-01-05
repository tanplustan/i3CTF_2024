# rsa:Crypto
Do you know how the RSA cipher works?

# Solution
基本的なRSAの問題。nが与えられているので[このサイト](https://factordb.com/index.php?query=89765553359668267846115148791526510167)でnの素因数を見つけ以下のコードで解読。  
[【CTF/Crypto】RSAの復号手順メモ](https://qiita.com/usagi325/items/2023afbb4d2a8b1781c0)が参考になる。


``` python
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
```
## FLAG{0SS1FR4G3}


