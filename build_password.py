import hashlib
import hmac
import binascii
import argparse

def pbkdf2(password, salt, iterations, dklen, hash_name='sha256'):
    # Get the length of the output hash in bytes
    hash_len = hashlib.new(hash_name).digest_size
    
    # Calculate the number of blocks needed for the derived key
    blocks = -(-dklen // hash_len)  # Ceiling division to ensure enough blocks

    derived_key = b''
    
    for i in range(1, blocks + 1):
        # Create the initial input for HMAC: salt concatenated with the block index (1-based)
        U = hmac.new(password, salt + i.to_bytes(4, 'big'), hash_name).digest()
        
        # Initialize F with the first block's HMAC result
        F = U
        
        # Apply the hash function `iterations` times
        for _ in range(1, iterations):
            # Compute HMAC with the result of the previous iteration
            U = hmac.new(password, U, hash_name).digest()
            # XOR the current block result with the previous block result
            F = bytes(x ^ y for x, y in zip(F, U))
        
        # Append the final result of this block to the derived key
        derived_key += F
    
    # Return the derived key truncated to the desired length
    return derived_key[:dklen]

def main():
    # For default value see EncodePassword(password string, salt string) (string, error) function from the Grafana source code
    parser = argparse.ArgumentParser(description="PBKDF2 Key Derivation")
    parser.add_argument('-p', '--password', type=str, default='admin', help='Password to hash')
    parser.add_argument('-s', '--salt', type=str, default='F3FAxVm33R', help='Salt value')
    parser.add_argument('-i', '--iterations', type=int, default=10000, help='Number of iterations')
    parser.add_argument('-dl', '--dklen', type=int, default=50, help='Desired length of the derived key in bytes')

    args = parser.parse_args()
    
    password = args.password.encode()
    salt = args.salt.encode()
    
    # Derive the key using PBKDF2
    derived_key = pbkdf2(password, salt, args.iterations, args.dklen)

    print(binascii.hexlify(derived_key).decode())

if __name__ == "__main__":
    main()
