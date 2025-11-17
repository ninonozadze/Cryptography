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

def calculated_score(decrypted_string):
    result = 0
    for char in decrypted_string.lower():
        if char in FREQUENCIES:
            result += FREQUENCIES[char]
        elif char.isalpha():
            result -= 0.05
        elif not char.isprintable():
            result -= 0.10
    return result


def find_output(hex_strings):
    final_decryption = ""
    final_score = -float('inf')

    for hex_string in hex_strings:
        hex_string = hex_string.strip()
        if not hex_string:
            continue

        for key in range(NUM_BYTE_VALUES):
            decrypted_string = bytes(b ^ key for b in bytes.fromhex(hex_string)).decode('ascii', errors='ignore')
            if bytes(b ^ key for b in bytes.fromhex(hex_string)).decode('ascii', errors='ignore'):
                if calculated_score(decrypted_string) > final_score:
                    final_decryption = decrypted_string
                    final_score = calculated_score(decrypted_string)

    return final_decryption


def main():
    number_of_input_strings = int(input().strip())
    input_strings = []
    for _ in range(number_of_input_strings):
        input_string = input().strip()
        input_strings.append(input_string)
    print(find_output(input_strings))


if __name__ == "__main__":
    main()