# SVG:Forensics
svg, svg... I hear that a lot.

# Solution
svgファイルが与えられ開くとQRコードとなっており、読み込むとExtensible Markup Languageのウキィペディアのページへいく。  
そんなこと気にせずにいったんstringsコマンドをたたくと``<Flag content="print(''.join(base64.b64decode(encoded_flag).decode()))"/>``
といった怪しい文字列がでてきたので``flag``が含まれている個所を抽出してみた。
```
$ strings image.svg | grep -i flag
<Flag content="import base64"/>
<Flag content="parts = ["/>
<Flag content="[70, 76, 65, 71],"/>
<Flag content="[123, 53, 86, 71],"/>
<Flag content="[95, 52, 110, 100],"/>
<Flag content="[95, 88, 77, 49],"/>
<Flag content="[95, 52, 114, 51],"/>
<Flag content="[95, 102, 52, 109],"/>
<Flag content="[49, 108, 121, 125]"/>
<Flag content="]"/>
<Flag content="flag = ''.join(chr(x) for part in parts for x in part)"/>
<Flag content="encoded_flag = base64.b64encode(flag.encode()).decode()"/>
<Flag content="print(''.join(base64.b64decode(encoded_flag).decode()))"/>
```
Pythonのように書かれているので  
```Python
import base64
parts = [
[70, 76, 65, 71],
[123, 53, 86, 71],
[95, 52, 110, 100],
[95, 88, 77, 49],
[95, 52, 114, 51],
[95, 102, 52, 109],
[49, 108, 121, 125]
]
flag = ''.join(chr(x) for part in parts for x in part)
encoded_flag = base64.b64encode(flag.encode()).decode()
print(''.join(base64.b64decode(encoded_flag).decode()))
```
として実行するとFLAGがでてきた。

## FLAG{5VG_4nd_XM1_4r3_f4m1ly}
