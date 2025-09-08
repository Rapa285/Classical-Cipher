import src.algorithm.utils as utils

class Vigenere:
    @staticmethod
    def encrypt(inputText, key):
        encrypted = ""
        for i in range(len(inputText)):
            p = utils.charToNum(inputText[i])
            k = utils.charToNum(key[i % len(key)])
            encrypted += utils.numToChar((p + k) % 26)
        return encrypted


    @staticmethod
    def decrypt(inputText, key):
        decrypted = ""
        for i in range(len(inputText)):
            c = utils.charToNum(inputText[i])
            k = utils.charToNum(key[i % len(key)])
            decrypted += utils.numToChar((c - k) % 26)
        return decrypted
    
if __name__ == "__main__":
    plaintext = '''Dinas Pendidikan Kota Ternate meminta kepada pihak sekolah dan
orang tua siswa untuk jenjang pendidikan SD dan SMP se-Kota Ternate
untuk melarang para siswa membawa permainan lato-lato yang sedang
tren itu ke sekolah, karena akan mengganggu kegiatan belajar mengajar
yang dinilai berbahaya sehingga mengantisipasi kecelakaan bagi anak di
daerah itu'''

    key = "selatsunda"
    ciphertext = Vigenere.encrypt(utils.removeNonAlpha(plaintext), key)
    print("Ciphertext:", ciphertext)  # Output: LVVQHZNGFHRVL

    decrypted_text = Vigenere.decrypt(ciphertext, key)
    print("Decrypted Text:", decrypted_text)  # Output: ATTACKATDAWN