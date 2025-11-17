from oracle import *
from helper import *

def get_signature(m, n):
  for k in range(2, m):
    if m % k == 0:
      break
  else:
    k = 1

  b = m // k

  partial_signature = (Sign(k) * Sign(b)) % n
  inverse_of_sign_one = pow(Sign(1), -1, n)

  forged_signature = (inverse_of_sign_one * partial_signature) % n
  return forged_signature


def main():
  with open('input.txt', 'r') as f:
    n = int(f.readline().strip())
    msg = f.readline().strip()

  Oracle_Connect()    

  m = ascii_to_int(msg)
  sigma = get_signature(m, n) 

  print(sigma)

  Oracle_Disconnect()

if __name__ == '__main__':
  main()
