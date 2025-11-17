import sys

def main():
    hex1 = sys.stdin.readline().strip()
    bytes1 = bytes.fromhex(hex1)

    hex2 = sys.stdin.readline().strip()
    bytes2 = bytes.fromhex(hex2)

    if len(bytes1) != len(bytes2):
        raise ValueError("Buffers should not have the different length")

    result_bytes = bytes(x ^ y for x, y in zip(bytes1, bytes2))
    result_hex = result_bytes.hex()

    print(result_hex)


if __name__ == "__main__":
    main()