import jwt
from typing import Optional
from datetime import datetime,timedelta
import jwt
import os
from dotenv import load_dotenv
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    load_dotenv()
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv("SECRET_KEY"), algorithm=os.getenv("ALGORITHM"))
    return encoded_jwt

oauth2_scheme = HTTPBearer()

def validate_token_and_role(required_roles: List[str]):
    def token_validator(token: HTTPAuthorizationCredentials = Depends(oauth2_scheme)):
        token = token.credentials