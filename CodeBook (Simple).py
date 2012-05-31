## Creates a dictionary wherein numerical keys are paired with letters

def buildCodeBook():
    letters = 'abcdefghijklmnopqrstuvwxyz.'
    CodeBook = {}
    key = 1
    for i in letters:
        CodeBook[key] = i
        key += 1
    return CodeBook

## Checks dictionary for corresponding values and prints decrypted message 

def decode(encrypted, CodeBook):
    decrypted = ''
    for m in encrypted:
        if m in CodeBook:
            decrypted += CodeBook[m]
        else:
            decrypted += '@'
    return decrypted
    
CodeBook = buildCodeBook()
encrypted = (15, 3, 15, 14, 14, 15, 18, 23, 15, 18, 11, 0,
             7, 13, 1, 9, 12, 27, 3, 15, 13)

print decode(encrypted, CodeBook)
