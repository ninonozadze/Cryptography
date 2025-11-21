# Instruction

### Problem 1 - Block cipher decryption

Source files in [project_2_1](project_2_1).

In this assignment, you must decrypt the message found in ([ctext.txt](project_2_1/ctext.txt)), which was encrypted using AES-128 in CBC mode with [PKCS #7](https://en.wikipedia.org/wiki/Padding_(cryptography)) padding and a random IV.

You have access to a server that attempts to decrypt any ciphertext you send. However, the server’s response only tells you whether a decryption error occurred:
1 - the ciphertext decrypted successfully
0 - a padding or decryption error occurred

The decrypted message (plaintext), once converted to ASCII, will be human-readable, so you can easily tell whether your solution is correct.
Write your code in the file [decipher.py](project_2_1/decipher.py), which will be executed using the command:
```
python3 decipher.py ctext.txt
```
and it should print the decrypted message (the plaintext) to stdout, with all padding removed.

#### Test instructions:
1) Run the server locally on any port you choose. For example:
```
./server 6667
```
2) In `oracle.py`, set the IP address to localhost and use the same port you chose. Example:
`s.connect(('127.0.0.1', 6667))`
3) Verify that the servers and oracle work properly:
```
python3 sample.py ctext.txt
```
4) Test your implementation:
```
python3 decipher.py ctext.txt
```

### Problem 2 - CBC-MAC

Source files in [project_2_2](project_2_2).

In this assignment, you will demonstrate that raw CBC-MAC is insecure for messages of variable length by performing a forgery attack.
For an x-block message, CBC-MAC works as shown:

![CBC-MAC](https://media.cheggcdn.com/media/409/40944253-8cc8-4d0d-90eb-85321a95ad8a/phprlvpCN.png)

You are given access to an oracle that returns tags (computed under an unknown key) only for 2-block messages (32 bytes).
Your goal is to construct a valid tag for a message of __any even number of blocks__, up to 255 bytes.

You can verify your forged tag using the provided server-side Verifier.

First, make sure the MAC and Verifier servers work correctly by testing them on the 2-block message in [test_message](project_2_2/test_message.txt). Once everything is set up, you can test your forging code on the 4-block message in [challenge_message](project_2_2/challenge_message.txt): “I, the server, hereby agree that I will pay $100 to this student” (4-block message). 

Your code should be written in [forge.py](project_2_2/forge.py).
When run as:
```
python3 forge.py challenge_message.txt
```
it must output the forged tag as a *hex string* to stdout.

#### Test instructions:
1) Run the MAC server and the Verifier locally, on any ports you choose. Example:
```
./mac-server 6667
```
```
./vrfy-server 6668
```
2)  In `oracle.py`, set the IP address to localhost and use the same port you chose. Example:
`mac_sock.connect(('127.0.0.1', 6667))` <br>
`vrfy_sock.connect(('127.0.0.1', 6668))`

3) Verify that the servers and oracle work properly:
```
python3 sample.py test_message.txt
```
4) Test your implementation:
```
python3 forge.py challenge_message.txt
```
