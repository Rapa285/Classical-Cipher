import utils
class FairPlay:
    def __init__(self):
        self.grid = []
        self.pair_array = []
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        self.grid = [list(alphabet[i:i+5]) for i in range(0, len(alphabet), 5)]
    
    def setGrid(self, grid):
        self.grid = grid
    
    def generateGrid(self, key):
        if key is None:
            return
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        key = key.upper()
        seen = set()
        i = 0
        for char in key:
            if char not in seen and char in alphabet:
                seen.add(char)
                self.grid[i//5][i%5] = char
                i += 1
        for char in alphabet:
            if char not in seen:
                self.grid[i//5][i%5] = char
                i += 1
        print(self.grid)

    def pairs(self, text):
        self.pair_array = []
        i = 0
        while i < len(text):
            # print(i)
            a = text[i]
            b = text[i + 1] if i + 1 < len(text) else 'X'
            # print(a, b)
            i += 2
            if a == b:
                self.pair_array.append(a+'X')
                i -= 1
            else:
                self.pair_array.append(a+b)
                
        print(self.pair_array)
    
    def findPosition(self, char):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == char.upper():
                    return (i, j)
        return None

    def encrypt(self, plaintext, key=None):
        self.generateGrid(key)
        self.pairs(plaintext)
        encrypted = ""
        for i in self.pair_array:
            a = i[0]
            b = i[1]
            row_a, col_a = self.findPosition(a)
            row_b, col_b = self.findPosition(b)
            if row_a == row_b:
                encrypted += self.grid[row_a][(col_a + 1) % 5] + self.grid[row_b][(col_b + 1) % 5]
            elif col_a == col_b:
                encrypted += self.grid[(row_a + 1) % 5][col_a] + self.grid[(row_b + 1) % 5][col_b]
            else:
                encrypted += self.grid[row_a][col_b] + self.grid[row_b][col_a]
        return encrypted
        

    def decrypt(self, ciphertext, key=None):
        self.generateGrid(key)
        self.pairs(ciphertext)
        decrypted = ""
        for i in self.pair_array:
            a = i[0]
            b = i[1]
            row_a, col_a = self.findPosition(a)
            row_b, col_b = self.findPosition(b)
            if row_a == row_b:
                decrypted += self.grid[row_a][(col_a - 1) % 5] + self.grid[row_b][(col_b - 1) % 5]
            elif col_a == col_b:
                decrypted += self.grid[(row_a - 1) % 5][col_a] + self.grid[(row_b - 1) % 5][col_b]
            else:
                decrypted += self.grid[row_a][col_b] + self.grid[row_b][col_a]
        return self.postProcessing(decrypted)

    def postProcessing(self, text):
        for i in range(len(text)-1):
            if text[i] == 'X' and i < len(text)-1 and text[i-1] == text[i+1]:
                text = text[:i] + text[i+1:]

        if text[-1] == 'X':
            text = text[:-1]
        return text
        

if __name__ == "__main__":
    fairplay = FairPlay()
    encrypted = fairplay.encrypt(utils.removeNonAlpha("temui ibu nanti malam"), utils.removeNonAlpha("JALAN GANESHA SEPULUH"))
    print("Encrypted:", encrypted)
    decrypted = fairplay.decrypt(encrypted, utils.removeNonAlpha("JALAN GANESHA SEPULUH"))
    print("Decrypted:", decrypted)