def translate(cipher, key):
    scale = 16
    num_of_bits = 8
    final = "["

    for i in range(0, 128, 2):
        cipherPortion = cipher[i:i+2]
        cipherBinary = bin(int(cipherPortion, scale))[2:].zfill(num_of_bits)
        keyPortion = key[i:i+2]
        keyBinary = bin(int(keyPortion, scale))[2:].zfill(num_of_bits)

        finalBinary = int(cipherBinary, 2) ^ int(keyBinary, 2)
        finalBinary = '{0:b}'.format(finalBinary)
        finalBinary = int(finalBinary, 2)
        final += finalBinary.to_bytes((finalBinary.bit_length() + 7) // 8, 'big').decode()

    return final+"]"

def main():
    n = int(input())

    for i in range(n):
        numKeys = int(input())
        cipher = input()
        for j in range(numKeys):
            print(translate(cipher, input()))

main()
