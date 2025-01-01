# Gyukaku:OSINT
What is the name of the store one floor below this Gyukaku?  
Flag format: FLAG{store name}  
Store name should be capitalized, with no spaces.  
![gyukaku.png](https://github.com/tanplustan/i3CTF_2024/blob/main/Gyukaku/gyukaku.png)

# Solution
exif情報からも画像検索からもヒントになるようなことが得られなかったのでGoogle mapで店舗の看板を総当たりする作戦に。  
公式サイトで店舗一覧を見ると517件。画像から4Fであることがわかるので```4F```で検索をかけると13件に絞れた。
一つずつ見ていくと吉祥寺北口店で画像と同じ風景を確認できた。  
![ans.png](https://github.com/tanplustan/i3CTF_2024/blob/main/Gyukaku/ans.png)
下の階がビッグエコーなので

## FLAG{BIGECHO}
