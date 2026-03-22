# los cuantificadores se utilizan para indicar cuantas ocurrencias de un caracter 
# o un grupo de caracteres hay

# * Puede aparecer 0 o mas veces

import re
text = "aaa, assdsa, lll"
pattern = r"a*"

find = re.findall(pattern, text)
print(find)