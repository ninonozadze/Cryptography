import base64

str_hex = input().strip()
# Cryptopals Rule
# Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.
# MARK: decode-ს მხოლოდ output-ის გამო ვიყენებ
# hex to raw bytes ->  raw bytes to base64 -> base64 to ASCII
str_base64 = base64.b64encode(bytes.fromhex(str_hex)).decode('ascii')
print(str_base64)
