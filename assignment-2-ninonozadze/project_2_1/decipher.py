import sys
from oracle import Oracle_Connect, Oracle_Disconnect, Oracle_Send

BYTE_VALUES = 256
BLOCK_SIZE = 16


def decrypt_cbc_block(previous_cipher_block, current_cipher_block):
    plaintext_bytes = [0] * BLOCK_SIZE
    intermediate_bytes = [0] * BLOCK_SIZE

    for byte_index in range(BLOCK_SIZE - 1, -1, -1):
        modified_previous_block = previous_cipher_block[:]
        padding_value = BLOCK_SIZE - byte_index
        for i in range(byte_index + 1, BLOCK_SIZE):
            modified_previous_block[i] = intermediate_bytes[i] ^ padding_value
        for guess_byte in range(BYTE_VALUES):
            modified_previous_block[byte_index] = guess_byte
            test_ctext = modified_previous_block + current_cipher_block
            result = Oracle_Send(test_ctext, 2)

            if result == 1:
                intermediate_byte = guess_byte ^ padding_value
                previous_cipher_byte = previous_cipher_block[byte_index]
                intermediate_bytes[byte_index] = intermediate_byte
                plaintext_bytes[byte_index] = intermediate_byte ^ previous_cipher_byte
                break
        else:
            print(f"[!] Decryption error: No valid padding found for byte index {byte_index}.")
            return None

    return plaintext_bytes

def read_ciphertext_file(filename):
    with open(filename, 'r') as f:
        hex_data = f.read().strip()
    return [int(hex_data[i:i + 2], BLOCK_SIZE) for i in range(0, len(hex_data), 2)]


def split_into_blocks(byte_array):
    total_blocks = len(byte_array) // BLOCK_SIZE
    return [
        byte_array[i * BLOCK_SIZE:(i + 1) * BLOCK_SIZE]
        for i in range(total_blocks)
    ]


def remove_pkcs7_padding(plaintext_bytes):
    if not plaintext_bytes:
        return plaintext_bytes

    padding_length = plaintext_bytes[-1]
    if 0 < padding_length <= BLOCK_SIZE and all(
        b == padding_length for b in plaintext_bytes[-padding_length:]
    ):
        return plaintext_bytes[:-padding_length]
    return plaintext_bytes


def decrypt_all_blocks(ciphertext_blocks):
    iv_block = ciphertext_blocks[0]
    encrypted_blocks = ciphertext_blocks[1:]
    decrypted_blocks = []

    previous_block = iv_block
    for index, current_block in enumerate(encrypted_blocks, start=1):
        decrypted_block = decrypt_cbc_block(previous_block, current_block)
        if decrypted_block is None:
            print(f"[!] Decryption failed at block {index}. Exiting.")
            sys.exit(-1)
        decrypted_blocks.append(decrypted_block)
        previous_block = current_block

    return [byte for block in decrypted_blocks for byte in block]



def main():
    if len(sys.argv) < 2:
        print("Usage: python3 decipher.py <filename>")
        sys.exit(-1)

    ciphertext_bytes = read_ciphertext_file(sys.argv[1])

    if Oracle_Connect() != 0:
        print("Error: Could not connect to the padding oracle.")
        sys.exit(-1)

    try:
        ciphertext_blocks = split_into_blocks(ciphertext_bytes)
        plaintext_bytes = decrypt_all_blocks(ciphertext_blocks)
        plaintext_bytes = remove_pkcs7_padding(plaintext_bytes)
        plaintext_str = ''.join(chr(b) for b in plaintext_bytes)
        print(f"Oracle returned: {plaintext_str}")
    finally:
        Oracle_Disconnect()


if __name__ == "__main__":
    main()