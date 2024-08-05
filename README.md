# Password Hash Verification Script

Welcome to the Password Hash Verification Script! This Python tool helps you check if a given password matches a hash stored in a Grafana `.db` file. Think of it as your trusty sidekick in the world of password security.

## Purpose

Grafana uses PBKDF2 with HMAC-SHA-256 to hash passwords, ensuring that even if someone intercepts the hash, it’s tough to crack. When a user changes their password, Grafana generates a random salt (not the kind you sprinkle on your food) and combines it with the password to create a hash. This script allows you to verify if the password matches the hash by replicating this process.

For example purposes (in the python script), we use the combination `admin/admin` (don't do this in production please), where:
- The password is `"admin"`
- The salt and hash values are extracted from Grafana's `.db` file.

This script demonstrates how to use PBKDF2 with the provided password and salt to check if it matches the stored hash. It’s built using the hashing logic found in the [Grafana codebase](https://github.com/grafana/grafana/blob/master/pkg/util/encoding.go).

## Prerequisites

- Python 3.x
- `hashlib` (included in Python’s standard library)
- `binascii` (also included in Python’s standard library)

## Instructions

1. **Extract Hash and Salt**:
   - Obtain the `given_hash` and `salt` from the `user` table in the Grafana `.db` file.

2. **Update Script**:
   - Replace the `given_hash` variable with the hash you want to verify.
   - Update the `salt` variable with the extracted salt, ensuring it is in bytes format.

3. **Run the Script**:
   - Ensure Python 3 is installed on your system.
   - Save the script to a file, e.g., `verify_password.py`.
   - Execute the script with `python verify_password.py`.

## Notes

- **Security**: Handle sensitive information such as passwords, hashes, and salts with care. Follow best practices to ensure data integrity and security.
- **Grafana**: This script assumes Grafana’s default hashing mechanism. If Grafana uses a different hashing algorithm or parameters, adjustments to the script may be needed.

## License

This script is provided for educational and informational purposes. Use it at your own discretion. No warranties are provided, so please use responsibly.

Enjoy cracking those hashes and may the security force be with you!

Feel free to reach out if you have any questions or need further assistance!
