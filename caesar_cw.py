import string

LETTERS_COUNT: int = 26
LETTERS = string.ascii_uppercase
KEY: int = 7854

words = ["ASSURANCE", "CYBERSECURITY", "INFINITY", "SAMPLING", "MORNING", "EXAMINATION", "MASTER",
         "SYSTEM", "VISUAL STUDIO", "BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY"]
results = [] # store encrypted result


def encrypt(msg: str, key: int) -> str:
    output = ""
    
    for character in msg:
        if character.isalpha():
            # retrieve the unicode val equivalent of the character "A" as starting
            unicode_point = ord("A") 
            # get the unicode val equivalent of the current character minus
            # the unicode point of A to get their from as 0=A, 1=B, C=3 etc..
            # then adds the shift key to the current index
            index = ord(character) - unicode_point + key
            # get the modulo of the index based on the given range (letter_counts)
            # then add the unicode point of our starting letter "A"
            # 65 - 67 + key
            # get the range using modulus then add that to the unicode
            # 2 + 65 = 67 
            index = index % LETTERS_COUNT + unicode_point
            # converts the index to a character
            # index is based on
            output += chr(index)

        else:
            # if the current character is a space or the likes
            output += character
    return output

def decrypt(msg: str, key: int) -> str:
    output = ""
    
    for character in msg:
        if character.isalpha():
            unicode_point = ord("A") 
            index = ord(character) - unicode_point - key
            index = index % LETTERS_COUNT + unicode_point
            output += chr(index)
        else:
            output += character
    return output

def main():
    for word in words:
        results.append(encrypt(word, KEY))
    
    for index in range(len(words)):
        isSame = decrypt(results[index], KEY) == words[index]
        print(f"Test Result: {isSame}")


if __name__ == "__main__":
    main()