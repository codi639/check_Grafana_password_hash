import hashlib
import binascii
import argparse
from hashlib import pbkdf2_hmac

# Setup argument parser
parser = argparse.ArgumentParser(description="Check a clear-text password using hash and salt.")
parser.add_argument('-p', '--password', type=str, default="admin", help="Clear-text password (default: 'admin').")
parser.add_argument('-s', '--salt', type=str, default="F3FAxVm33R", help="Salt in bytes (default: 'F3FAxVm33R').")
parser.add_argument('-g', '--given-hash', type=str, default="59acf18b94d7eb0694c61e60ce44c110c7a683ac6a8f09580d626f90f4a242000746579358d77dd9e570e83fa24faa88a8a6", help="Given hash to verify against (default: provided hash).")

# Parse arguments
args = parser.parse_args()

# Assign parsed arguments or default values
password = args.password
salt = args.salt.encode()  # Ensure salt is in bytes
given_hash = args.given_hash

# PBKDF2 parameters
iterations = 10000

# Error handling for odd-length hash string
try:
    dklen = len(binascii.unhexlify(given_hash))  # Match length of the given hash
except binascii.Error as e:
    print(f"Error: Invalid hash string '{given_hash}'. Hexadecimal strings must have an even number of characters.")
    exit(1)

# Derive the key using PBKDF2
dk = pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen)

# Encode the derived key in hexadecimal format
hashed_password = binascii.hexlify(dk).decode()

# Compare the hashes
is_match = hashed_password == given_hash

# Print the result
if is_match:
    print(f"OH YEAH! {password} is the password.\n")
#   print("Password is correct and matches the given hash and salt.")
else:
    print("NOTHING'S GOOD, FAILURE IS THE ONLY SOLUTION.\n")
#   print("Password is incorrect or does not match the given hash and salt.")
