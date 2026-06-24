from jose import jwt 

Secret_Key = "mysecretkey"

data = {
    "user_id":2
    }

token = jwt.encode(data,Secret_Key,algorithm="HS256")
print(token)

payload = jwt.decode(token,Secret_Key,algorithms="HS256")
print(payload)





