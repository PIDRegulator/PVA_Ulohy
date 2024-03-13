def dosoustavy(number, soustava):
    if number < soustava:
        return [number]
    else:
        return dosoustavy(number//soustava,soustava) + [number%soustava]
    
def ispalindrom(number, soustava):
    number = dosoustavy(number, soustava)
    return number == number[::-1]

def reseni(number,soustava):
    while number < 2**64:
        number += 1
        if ispalindrom(number, soustava):
            return number, 1
    return number, 0
        
print(reseni(10, 2))        