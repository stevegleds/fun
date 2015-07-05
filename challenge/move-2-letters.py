""" Write a function called that takes a string and an integer as parameters, and that
returns a new string that contains the letters from the original string moved to the right by the given amount.
You might want to use the built-in functions ord,
which converts a character to a numeric code,
and chr, which converts numeric codes to characters.
Potentially offensive jokes on the Internet are sometimes encoded in ROT13. If you are not easily
offended, find and decode some of them. Solution: http://thinkpython.com/code/rotate.
py ."""

def rotate_word(word, n):
    new_word = "" 
    count = 0
    for c in word:
        value = ord(c) #stores numeric value of letter c
        if value + n > ord('z'): # the encrypted value would yield a letter after z
            value -= 26 # 'loops' back to start of alphabet
        new_word += chr(value + n) # adds the encrypted char
        count += 1 # move on to next letter in new word
    return new_word
print("enter the text")
coded_text = input()
print(rotate_word(coded_text, 2))

        
        
        
