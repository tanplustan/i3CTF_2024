# Matryoshka:Crypto
I can't read it as it is!  

# Solution
matryoshka.txtには  
```NjItPlU0TTJ3cFJER0NwNUI4cWtvdXdZaUhDVlF2a0lnZnRremh3NXBUemtZeDROWG96RENHV0J3MGZCQ0tVYWcxbmd3TFQzdHJHemswdmRQdjBSaVVDUkV2VUJSaWtZWHd4UnJNUkVLTW0xaXRaOUFMUXdvNXh6TVpBMU12MXM1VU81RmlTMFN5M1JURnUxOGZWQ2VkdEs2VEtOWllqcGFRWWswTkwycUhURGtCVU9nVGlGSHA3VWlydTJJZlV4QUJhMW5lM0p5c2QweDNTT0hEVGEyOVR5WGZrQW1ST2JjRHRYUGxHd2V4emZsc0N6Y2g1NVVSZ0ZQOWdNcXp2NjJGVGU3VHhLY3l0T05LQ2pKUjRYem1XNlA5blBGVDlwOHB2Smh6amFYSHlndzZHVXpLQkU1VU94cGNyZXpzZjhCNG1qeVVoYk9CWDNFdGVkVzRqWHpBZnFwblVSWFMxQTdYRWlpTTZxMk5VdE9iTHpMQ0lXVG9WOXBSVzM==```  
とあるのでパッと見base64を予想。base64でデコードすると  
```62->U4~~```  
が得られる。先頭の62が怪しいので次にbase62でデコードするとまた先頭に数字が出てくるので58, 45...と繰り返していくことでFLAGが得られる。  
base64以外にもあったんですね...

## FLAG{Mr_decode_master}
