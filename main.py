import string
import random

def generate_password(length=8):
  password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
  return password

print(generate_password())
