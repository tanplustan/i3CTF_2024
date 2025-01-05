# fermat:Crypto
I'd like to write the problem statement here, but this margin is too narrow to contain.  

# Solution
nが大きいので片っ端からの素因数分解は現実的ではない。https://factordb.com/index.php?query=
でも素数の組が見つからないので``chall.py``を確認する。
``` Python
p = getStrongPrime(2048)
q = gmpy2.next_prime(p)
```
ここからp,qが近いことがわかる。[このサイト](https://qiita.com/Anko_9801/items/14a45eddfa2c29a571d1#その3-近い値の素数を用いてはいけない-fermats-method)
で近い値の素数の組の調べ方があるので参考にして[decode.py](https://github.com/tanplustan/i3CTF_2024/blob/main/fermat/decode.py)で解読。fermat関数以外はrsaのコピペ。

## FLAG{H4nc_m4rg1n1s_3x1gu1t45_n0n_c4p3r3t}
