#!/usr/local/bin/python3
import sys
import secrets, random, string  
import argparse

def main():
  print("Initializing...")
  args = init_args()
  
  file_count = 10
  max_hex = 100
  
  if args.n:
    file_count = args.n
  if args.x:
    max_hex = args.x
  
  print("Generating...")
  generate(file_count, max_hex)
  
  print("Complete")

def generate(file_count, max_hex):
  for i in range(file_count):
    filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    with open(filename, 'wb') as f:
      result = generate_bin_file(max_hex)
      
      f.write(result)

def generate_bin_file(max_hex):
  r = random.randint(50, max_hex)
  token = secrets.token_hex(r)
  return bytes.fromhex(token)

def init_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, help='define number of files')
  parser.add_argument('-x', type=int, help='define max hex for single file')
  
  return parser.parse_args()
      
if __name__ == "__main__":
  main()
  
