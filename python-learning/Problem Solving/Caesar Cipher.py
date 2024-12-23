text = input('Enter your message: ')
num= int(input('Enter the shift value: '))
cipher = ''
for char in text:
    if not char.isalpha():
        cipher += char
        continue
			
    # char = char.upper()
    code = ord(char) + num

    # if code > ord('Z'):
    #     code = ord('A')

    cipher += chr(code)
    
# reverse the upper and lower case letters
cipher2 = ''
for i in cipher:
    if i.isupper():
        i = i.lower()
    elif i.islower():
        i = i.upper()
    else:
        i= i
    cipher2 += i

print(cipher)
    