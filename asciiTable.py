character_to_covert = str(input("Enter character: "))
CovertedCHAR = ord(character_to_covert)
print("ASCII code for {} is {}".format(character_to_covert, CovertedCHAR))
ASCIItocovert = int(input("Enter a ASCII number between 32 and 128: "))
if ASCIItocovert <= 127 or ASCIItocovert >= 33:
    CovertedASCII = chr(ASCIItocovert)
    print("The char for {} is {}".format(ASCIItocovert, CovertedASCII))
else:
    print("Between 32 and 128 please")
for i in range(33, 127, 1):
    print("{} {:>6}".format(i, chr(i)))
