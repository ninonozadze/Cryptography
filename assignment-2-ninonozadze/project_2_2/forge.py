import sys
from oracle import Oracle_Connect, Oracle_Disconnect, Mac, Vrfy

BLOCK_SIZE = 16

def get_block(message, block_index):
    start = block_index * BLOCK_SIZE
    end = start + BLOCK_SIZE
    return message[start:end]


def forge_function(message):
    Oracle_Connect()
    tag = bytearray()
    num_blocks = len(message) // BLOCK_SIZE

    for i in range(0, num_blocks, 2):

        first_start = i * BLOCK_SIZE
        first_end = (i + 1) * BLOCK_SIZE
        second_start = (i + 1) * BLOCK_SIZE
        second_end = None if i == num_blocks - 2 else (i + 2) * BLOCK_SIZE

        first_block = message[first_start:first_end]
        second_block = message[second_start:second_end]

        if len(tag) != 0:
            xor_result = ''.join(chr(tag[j] ^ ord(first_block[j])) for j in range(len(first_block)))
            tag = Mac(xor_result + second_block, len(xor_result + second_block))
        else:
            tag = Mac(first_block + second_block, len(first_block + second_block))

    if Vrfy(message, len(message), tag):
        print("Message verified successfully!")
    else:
        print("Message verification FAILED successfully! :)")

    tag_hex = tag.hex()
    print('Tag:', tag_hex)
    Oracle_Disconnect()


def main():
    if len(sys.argv) < 2:
        print("Usage: python sample.py <filename>")
        sys.exit(1)

    f = open(sys.argv[1])
    message = f.read()
    f.close()

    forge_function(message)

if __name__ == "__main__":
    main()
