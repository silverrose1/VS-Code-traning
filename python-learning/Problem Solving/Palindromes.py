text = input('enter your text: ')
text = text.lower().replace(' ', '')
text2 = text[::-1]
if text == text2:
    print('This is a palindrome')
else:
    print('This is not a palindrome')
