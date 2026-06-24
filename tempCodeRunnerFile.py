from passlib.context import CryptContext

pwd_Context = CryptContext(
    schemes=["bcrypt"],
    deprecated = "auto"
)

password = "123456"

hash_password = pwd_Context.hash(password)