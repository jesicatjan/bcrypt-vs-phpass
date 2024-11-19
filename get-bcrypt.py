import bcrypt

def bcrypt_hash(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def display_hashed_password(password: str):
    print(f"Password to hash: {password}")
    hashed_password = bcrypt_hash(password)
    print(f"bcrypt hashed password: {hashed_password}\n")

display_hashed_password("password")
display_hashed_password("jesicatjan")