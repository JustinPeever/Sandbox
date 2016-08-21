def main():
    finish = False
    character_to_covert = str(input("Enter character: "))
    CovertedCHAR = ord(character_to_covert)
    print("ASCII code for {} is {}".format(character_to_covert, CovertedCHAR))
    ASCIItocovert = int(input("Enter a ASCII number between 32 and 128: "))



    if ASCIItocovert <= 127 or ASCIItocovert >= 33:
        CovertedASCII = chr(ASCIItocovert)
        print("The char for {} is {}".format(ASCIItocovert, CovertedASCII))
    else:
        print("Between 32 and 128 please")
    while finish == False:
        try:
            lower=int(input("Enter lower number"))
            upper=int(input("Enter upper number"))
        except ValueError:
            print("Oops!  That was no valid number range.  Try again...")
            finish = False
        finish = True
        get_number(lower, upper)




def get_number(lower, upper):
    if lower<33 or upper>127:
        print("Oops!  That was no valid number range.  Try numbers between 32 and 128")
    else:
        for i in range(lower, upper+1, 1):
            print("{} {:>6}".format(i, chr(i)))

main()
