from passlib.context import CryptContext

pwd_hash = CryptContext(
    schemes = ["bcrypt"],
    deprecated = "auto"
) 

def password_hash(password:str):
    return pwd_hash.hash(password)

def password_verify(main_password,hash_password):
    return pwd_hash.verify(main_password,hash_password)