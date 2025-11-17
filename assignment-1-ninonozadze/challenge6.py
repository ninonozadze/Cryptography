import base64
from itertools import zip_longest

FREQUENCIES = {
    'a': 0.08167, 'b': 0.01492, 'c': 0.02782,
    'd': 0.04253, 'e': 0.12702, 'f': 0.02228,
    'g': 0.02015, 'h': 0.06094, 'i': 0.06966,
    'j': 0.00153, 'k': 0.00772, 'l': 0.04025,
    'm': 0.02406, 'n': 0.06749, 'o': 0.07507,
    'p': 0.01929, 'q': 0.00095, 'r': 0.05987,
    's': 0.06327, 't': 0.09056, 'u': 0.02758,
    'v': 0.00978, 'w': 0.02360, 'x': 0.00150,
    'y': 0.01974, 'z': 0.00074, ' ': 0.13000
}

NUM_BYTE_VALUES = 256

def calculated_score(text):
    score = 0
    for char in text.lower():
        if char in FREQUENCIES:
            score += FREQUENCIES[char]
        elif char.isalpha():
            score -= 0.05
        elif not char.isprintable():
            score -= 0.10
    return score

def hamming_distance(a, b):
    return sum(bin(x ^ y).count('1') for x, y in zip(a, b))

def find_keysize(ciphertext, max_keysize=40):
    best_keysize, best_dist = 2, float('inf')
    for keysize in range(2, max_keysize+1):
        chunks = [ciphertext[i*keysize:(i+1)*keysize] for i in range(4)]
        dist = sum(hamming_distance(chunks[i], chunks[j])/keysize
                  for i in range(3) for j in range(i+1,4))/6
        if dist < best_dist:
            best_dist, best_keysize = dist, keysize
    return best_keysize

def transpose_blocks(ciphertext, keysize):
    blocks = [ciphertext[i:i+keysize] for i in range(0, len(ciphertext), keysize)]
    return [bytes([block[i] for block in blocks if i < len(block)])
            for i in range(keysize)]

def break_single_char_xor(ciphertext):
    best_key, best_score = 0, -float('inf')
    for key in range(NUM_BYTE_VALUES):
        try:
            plain = bytes(b ^ key for b in ciphertext).decode('ascii')
            score = calculated_score(plain)
            if score > best_score:
                best_score, best_key = score, key
        except:
            continue
    return best_key

def break_repeating_key_xor(ciphertext):
    keysize = find_keysize(ciphertext)
    blocks = transpose_blocks(ciphertext, keysize)
    key = bytes(break_single_char_xor(block) for block in blocks)
    return bytes(ciphertext[i] ^ key[i % len(key)] for i in range(len(ciphertext)))

def main():
    ciphertext = base64.b64decode(input().strip())
    print(break_repeating_key_xor(ciphertext).decode('ascii'))

if __name__ == "__main__":
    main()