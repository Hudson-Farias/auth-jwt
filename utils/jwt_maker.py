from jwt import encode
from env import JWT_SECRET, JWT_ALGORITHM

def jwt_maker():
    jwt_payload = {}
    jwt_header = {"alg": JWT_ALGORITHM, "typ": "JWT"}

    token = encode(jwt_payload, JWT_SECRET, algorithm = JWT_ALGORITHM, headers = jwt_header)
    return {"token": token}
