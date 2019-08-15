import re
x=re.findall(r'\d+|\d+,\d+', 'Kshs 1,002 uiui')
print(x[0])