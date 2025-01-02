# xor:Crypto
Let's go warm up !

# Solution
chall.pyを確認すると、この問題では暗号化にXORが使用されていることが分かる。
XORの**同じkeyを再度適用すると元の値を復元できる**という特性を利用して復号する。  
```key = random.choice(string.printable.strip()).encode()```  
このコードからkeyは```string.printable```のうちの1文字であり、容易に全パターンを試せることが分かる。  
添付ファイルには暗号化された文字列encに加えてhashも記載されているのでencを全てのkeyで復号し、
復号した文字列のhashと```output.txt```のhashが等しくなるものを見つける。  
```python
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
```
```
b'kore_ha_flag_desu_anata_ha_tadori_tuita_no_da_FLAG{z3br4s_ar3_als0_x0r}'
```

## FLAG{z3br4s_ar3_als0_x0r}
