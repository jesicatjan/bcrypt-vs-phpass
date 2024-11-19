import bcrypt
from passlib.hash import phpass
import time

# Define a common password
password = "SecurePassword123"

# Generate bcrypt hash
bcrypt_salt = bcrypt.gensalt(rounds=12)
bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt_salt)

# Generate phpass hash
phpass_hash = phpass.using(rounds=8).hash(password)

print(f"bcrypt hash: {bcrypt_hash}")
print(f"phpass hash: {phpass_hash}")

# Simulate brute force attack (dummy for illustration)
def brute_force_attack(hash_func, hash_value, password_list):
    for candidate in password_list:
        if hash_func.verify(candidate, hash_value):
            return candidate
    return None

# Brute force using a small password list
password_list = ["password", "123456", "SecurePassword123", "letmein"]

# Test bcrypt
start = time.time()
for candidate in password_list:
    if bcrypt.checkpw(candidate.encode(), bcrypt_hash):
        bcrypt_result = candidate
        break
bcrypt_time = time.time() - start

# Test phpass
start = time.time()
phpass_result = brute_force_attack(phpass, phpass_hash, password_list)
phpass_time = time.time() - start

print(f"bcrypt cracked in: {bcrypt_time} seconds, result: {bcrypt_result}")
print(f"phpass cracked in: {phpass_time} seconds, result: {phpass_result}")


# import hashlib
# import bcrypt
# import time

# def hash_without_salt(password: str):
#     return hashlib.sha256(password.encode()).hexdigest()

# def hash_with_salt(password: str):
#     salt = bcrypt.gensalt()
#     hashed_password = bcrypt.hashpw(password.encode(), salt)
#     return hashed_password

# password = "password"

# # Hash without salt
# start_time = time.time()
# hashed_password_without_salt = hash_without_salt(password)
# end_time = time.time()
# print(f"Time to hash without salt: {end_time - start_time} seconds")

# # Hash with salt
# start_time = time.time()
# hashed_password_with_salt = hash_with_salt(password)
# end_time = time.time()
# print(f"Time to hash with salt: {end_time - start_time} seconds")

# # Display the hashes
# print(f"Hash without salt: {hashed_password_without_salt}")
# print(f"Hash with salt: {hashed_password_with_salt}")
