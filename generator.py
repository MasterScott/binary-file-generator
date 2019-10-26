#!/usr/local/bin/python3
import sys
import secrets, random, string  
  
def main():
  for i in range(10):
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    with open(filename, 'wb') as f:
      result = generate_bin_file()
      print(result)
      
      # f.write(result)

def generate_bin_file():
  r = random.randint(50, 100)
  token = secrets.token_hex(r)
  return bytes.fromhex(token)
      
if __name__ == "__main__":
  main()
  
