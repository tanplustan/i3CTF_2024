# crack:Misc
John : Bob, what's wrong?  
Bob : I forgot the password to the zip file with all the important data!  
John : That's terrible!  
Bob : I thought I made the password easy...  
[crack.zip](https://github.com/tanplustan/i3CTF_2024/blob/main/crack/crack.zip)

# Solution
zipファイルを開こうとするとパスワードがかかっていた。問題文から総当たりで開くだろうと予想。  
John the Ripperを用いて辞書で総当たりすると
```password1122```
であることが分かった。zipを見るとImportant.txtにFLAGが記載されていた。  
```
zip2john crack.zip > hash.txt  
ver 2.0 crack.zip/important.txt PKZIP Encr: cmplen=38, decmplen=26, crc=3D4BD67
```  
```
john --wordlist=passwords.txt hash.txt
Using default input encoding: UTF-8
Loaded 1 password hash (PKZIP [32/64])
No password hashes left to crack (see FAQ)
```  
```
john --show hash.txt
crack.zip/important.txt:password1122:important.txt:crack.zip::crack.zip
```  

## FLAG{F1r57_P455w0rd_Cr4ck}
