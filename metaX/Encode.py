def encode(password):
    def caesar(password, operation):
        shift = len(password) % 10 # returns number from 0 - 9 
        
        def crypt(char, shift, operation):
            if operation == "enc":
                return char + shift # When encrypting, shift the char by x units positively
            if operation == "dec":
                return char - shift # When decrypting, reverse the encryption     # (A true loading screen tip)
            pass
        
        out = []   # Array containing characters for final string
        
        for i in range(0, len(password) - 1):
            charcode = ord(password[i])   # charcode equals the code for the character 
            
            if charcode >= 48 and charcode <= 57:
                charcode = crypt(charcode, shift, operation) # charcode is shifted
            
                if charcode < 48:
                    charcode = charcode + 10   # With these two statements
                                               # the value of charcode
                if charcode > 57:              # is clamped between
                    charcode = charcode - 10   # 48 and 57 including the two
                """
                Clamped area is most likely 10 because of numbers from 0 to 9
                """
            
            elif charcode >= 65 and charcode <= 90: 
                charcode = crypt(charcode, shift, operation)
            
                if charcode < 65:              # Same here
                    charcode = charcode + 26
            
                if charcode > 90:              # Just clamped between
                    charcode = charcode - 26   # 65 and 90
                """
                Clamped area is most likely 26 because of the lowercase / uppercase alphabet
                """
            elif charcode >= 97 and charcode <= 122:
                charcode = crypt(charcode, shift, operation)
                
                if charcode < 97:              # Again
                    charcode = charcode + 26
                
                if charcode > 122:             # 97 and 122
                    charcode = charcode - 26
                """
                Clamped area is most likely 26 because of the lowercase / uppercase alphabet
                """

            out.append(chr(charcode))          # Append the character to the array 
            pass            
        
        return "".join(out)                    # Return a string, made from the array
    output = caesar(password, "enc")
    return output

while True:
    msg = input(">")
    print(encode(msg))
    

""" Notable stuff for decryption
Length of the string stays the same

if charcode = 68, shift = 6 and operation = "dec" then charcode is changed to 88.  68 -> 62 -> 88

Encryption / Decryption shifts uppercase letters to other uppercase, lowercase to other lowercase, and numbers to other numbers
"""