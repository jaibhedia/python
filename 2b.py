def bin2Dec(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 2**i
        i += 1  # Indent this line to increment i inside the loop
    return dec

def oct2Hex(val):
    rev = val[::-1]
    dec = 0
    i = 0
    for dig in rev:
        dec += int(dig) * 8**i
        i += 1  # Indent this line to increment i inside the loop

    # Initialize an empty list to store remainders
    remainders = []
    
    while dec != 0:
        remainders.append(dec % 16)
        dec = dec // 16
    
    hex_digits = []
    
    for elem in remainders[::-1]:
        if elem <= 9:
            hex_digits.append(str(elem))
        else:
            hex_digits.append(chr(ord('A') + (elem - 10)))

    hex_val = "".join(hex_digits)
    
    return hex_val

num1 = input("Enter a binary number: ")
print(bin2Dec(num1))

num2 = input("Enter an octal number: ")
print(oct2Hex(num2))
