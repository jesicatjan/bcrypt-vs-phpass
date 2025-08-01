import bcrypt

def bcrypt_hash(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

display_hashed_password("password")
display_hashed_password("jesicatjan")
