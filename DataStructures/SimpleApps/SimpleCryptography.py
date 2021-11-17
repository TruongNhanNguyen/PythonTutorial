class CaesarCipher:
    """ Class for doing encryption and decryption using CaesarCipher """

    def __init__(self, shift):
        """ Construct Caesar cipher using given interger shift for rotation """
        encoder = [None] * 26
        decoder = [None] * 26
        for k in range(26):
            encoder[k] = chr((k + shift) % 26 + ord('A'))
            decoder[k] = chr((k - shift) % 26 + ord('A'))
        self._forward = ''.join(encoder)
        self._backward = ''.join(decoder)

    def encrypt(self, message):
        """ Return string representing the encripted message """
        return self._tranform(message, self._forward)

    def decrypt(self, secrete):
        """ Return decrypted message given encrypted message """
        return self._tranform(secrete, self._backward)

    def _tranform(self, original, code):
        """ Utility to perform transformation based on given code string """
        msg = list(original)
        for k in range(len(msg)):
            if msg[k].isupper():
                j = ord(msg[k]) - ord('A')
                msg[k] = code[j]
        return ''.join(msg)


if __name__ == '__main__':
    cipher = CaesarCipher(4)
    message = "THE EAGLE IS IN PLAY; MEET AT JAME\'S HOUSE."
    coded = cipher.encrypt(message)
    print('Secrete: ', coded)
    answer = cipher.decrypt(coded)
    print('Message: ', answer)
    