# Instruction

This assignment consists of two parts. You may structure your code modularly.

_In these tasks, **you are not allowed** to use external libraries._

### Problem 1 - Meet-in-the-Middle Attack on the Discrete Logarithm

In this task, you must compute a discrete logarithm in Z<sub>p</sub><sup>*</sup>, where p is a prime number.
You will be given four arguments:

+ p - a prime number,
+ g - a generator of Z<sub>p</sub><sup>*</sup>,
+ h - an element of Z<sub>p</sub><sup>*</sup>; note that there exists some value x such that h ≡ g<sup>x</sup> (mod p),
+ max_x - the maximum possible value of x.

You must find the value of x that satisfies the equation h ≡ g<sup>x</sup> (mod p).

In the example used for testing your code, it is known that max_x ≤ 2<sup>40</sup>. A naive approach (trying all possible values of x) would require up to 2<sup>40</sup> multiplications, which is computationally expensive.
Instead, for this task you should use a more efficient method - meet-in-the-middle attack.

To understand how this attack works, observe the following:

If max_x = B<sup>2</sup> and x ≤ B<sup>2</sup>, then we can represent x as x = x<sub>0</sub>B + x<sub>1</sub>, where x<sub>0</sub> ≤ B and x<sub>1</sub> ≤ B.

From this, we get h ≡ g<sup>x</sup> ≡ g<sup>x<sub>0</sub>B + x<sub>1</sub></sup> ≡ g<sup>x<sub>0</sub>B</sup> ⋅ g<sup>x<sub>1</sub></sup> (mod p).
If we divide both sides by g<sup>x<sub>1</sub></sup>, we obtain:

h/g<sup>x<sub>1</sub></sup> ≡ (g<sup>B</sup>)<sup>x<sub>0</sub></sup> (mod p)

In this equation, all values except x<sub>0</sub> ​ and x<sub>1</sub> ​ are known. This allows us to proceed as follows:
1. Compute all possible values of h/g<sup>x<sub>1</sub></sup> (mod p)
   and store them in a hash table together with their corresponding x<sub>1</sub>
2. Then iterate over all x<sub>0</sub> and compute g<sup>B</sup>)<sup>x<sub>0</sub></sup> (mod p), checking whether this value appears in the hash table.

How many operations does this attack require (approximately)?

#### Technical Details:

You need to complete the file `dlog.py` by implementing the function `discrete_log`.
Your script will be executed as follows:
```
python3 dlog.py
```

The values of p, g, and h will be provided via stdin.
Your program should print the value of x to stdout.

Note: Your code must finish execution within **one minute**.
You can measure execution time in the terminal using the time command.

<br>

### Problem 2 - Forging an RSA‑based Signature
For 63‑byte messages, signatures are generated using the following scheme:
The public key is a standard RSA pair (N,e),
The private key is the standard (N,d),
N is a 128‑byte (1024‑bit) integer.
For a 63‑byte message m, the signature is computed as: σ ≡ M<sup>d</sup>(mod N), 
where the encoded value M is defined as:
M = 0x00 m 0x00 m
Make sure that the final value M is exactly 128 bytes long.


If m is shorter than 63 bytes, it is padded with leading zeros until it reaches 63 bytes.
(For example, the 1‑byte message "x" and the 2‑byte message "0x00 x" will result in the same signature.
This weakness is known and not relevant for this task.)

Your task is to forge the signature for the 63‑byte challenge message.

You are given:
Access to a server that returns signatures for any 63‑byte or shorter message except the challenge message itself.
Access to a verification server, which checks whether a given signature/message pair is valid.

To get started, you can verify that your connection code works by running `sample.py` file.

#### Technical Details:

rsa To run the RSA servers locally, use the following commands:
```
python3 rsa_signing_server.py 49104 

python3 rsa_verify_server.py 49105
```
You must complete the file `sign.py` by implementing the function `get_signature`.
Your script will be executed with:
```
python3 sign.py < input.txt
```
The file `input.txt` contains the RSA modulus and the message.
Your program should output the signature for that message to stdout.
