def charToNum(letter):
    return ord(letter.lower()) - ord('a')


def numToChar(num):
    return chr(num + ord('a')).upper()

def removeNonAlpha(text):
    return ''.join(filter(str.isalpha, text))

if __name__ == "__main__":
    array = 'abcdefghijklmnopqrstuvwxyz'
    for i in array:
        print(charToNum(i), end=' ')
    print(numToChar(0))