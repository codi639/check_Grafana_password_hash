import hashlib
import binascii
from hashlib import pbkdf2_hmac

# This script is actually running on the combination admin/admin where Grafana generate randomly the salt on the first connection.

print("Remember to change the hash, the password and the salt.\n")

# Given hash to verify
given_hash = "59acf18b94d7eb0694c61e60ce44c110c7a683ac6a8f09580d626f90f4a242000746579358d77dd9e570e83fa24faa88a8a6"

# Password and provided salt
password = "admin"
salt = b"F3FAxVm33R"  # Ensure salt is in bytes

# PBKDF2 parameters
iterations = 10000
dklen = len(binascii.unhexlify(given_hash))  # Match length of the given hash

# Derive the key using PBKDF2
dk = pbkdf2_hmac('sha256', password.encode(), salt, iterations, dklen)

# Encode the derived key in hexadecimal format
hashed_password = binascii.hexlify(dk).decode()

# Compare the hashes
is_match = hashed_password == given_hash

# Print the result
if is_match:
    print("OH YEAH!\n")
#    print("Password is correct and matches the given hash and salt.")
else:
    print("NOTHING'S GOOD, FAILURE IS THE ONLY SOLUTION.\n")
#    print("Password is incorrect or does not match the given hash and salt.")
