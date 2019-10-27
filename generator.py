#!/usr/local/bin/python3
import sys
import secrets, random, string  
import argparse

def main():
  print("Initializing...")
  args = init_args()
  n = 10
  
  if args.n:
    n = args.n
  
  print("Generating...")
  for i in range(n):
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    with open(filename, 'wb') as f:
      result = generate_bin_file()
      
      f.write(result)
  
  print("Complete")

def generate_bin_file():
  r = random.randint(50, 100)
  token = secrets.token_hex(r)
  return bytes.fromhex(token)

def init_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, help='define number of files')
  
  return parser.parse_args()
      
if __name__ == "__main__":
  main()
  
