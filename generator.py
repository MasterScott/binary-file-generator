#!/usr/local/bin/python3
import sys, os
import secrets, random, string  
import argparse

def main():
  print("Initializing...")
  args = init_args()
  
  file_count = 10
  max_hex = 100
  folder_count = 1
  
  if args.n:
    file_count = args.n
  if args.x:
    max_hex = args.x
  if args.f:
    folder_count = args.f
  
  print("Generating...")
  generate(file_count, max_hex, folder_count)
  
  print("Complete")

def generate(file_count, max_hex, folder_count):
  for f in range(folder_count):
    folder_name = str(f)
    os.mkdir(folder_name)
  
    current_path = folder_name + '/'
  
    for i in range(file_count):
      filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
      with open(current_path + filename, 'wb') as f:
        result = generate_bin_file(max_hex)
        
        f.write(result)

def generate_bin_file(max_hex):
  base = 50
  if max_hex < 50:
    base = 0
  
  r = random.randint(base, max_hex)
  token = secrets.token_hex(r)
  return bytes.fromhex(token)

def init_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-n', type=int, help='define number of files')
  parser.add_argument('-x', type=int, help='define max hex for single file')
  parser.add_argument('-f', type=int, help='define number of folders')
  
  return check_args(parser.parse_args())

def check_args(args):
  # check -n
  if args.n < 0:
    print("invalid value for number of files (-n)")
    print("Program aborted")
    sys.exit()
  
  # check -x
  if args.x < 0:
    print("invalid value for max hex (-x)")
    print("Program aborted")
    sys.exit()
  
  # check -f
  if args.f < 0:
    print("invalud value for number of folders (-f)")
    print("Program aborted")
    sys.exit()
  
  return args
  
if __name__ == "__main__":
  main()
  
