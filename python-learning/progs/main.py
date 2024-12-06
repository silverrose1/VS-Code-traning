from sys import path

path.append('F:\\Programming Installation\\VS Code traning\\Python Learning\\modules')
# path.append('C:\\Users\\Ahmed Nassar\\AppData\\Roaming\\Python\\Python312\\site-packages')

import module1

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module1.suml(zeroes))
print(module1.prodl(ones))
import sys

for p in sys.path:
  print(p)


