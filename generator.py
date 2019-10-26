import secrets, random, string

def generate_bin_file():
  r = random.randint(50, 100)
  token = secrets.token_hex(r)
  return bytes.fromhex(token)

for i in range(10):
  filename = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
  with open(filename, 'wb') as f:
    result = generate_bin_file()
    
    f.write(result)