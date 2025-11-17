def main():
    first_input = input().strip()
    second_input = input().strip()
    result = []

    for i, char in enumerate(second_input):
        result.append(ord(char) ^ ord(first_input[i % len(first_input)]))

    print(bytes(result).hex())

if __name__ == "__main__":
    main()