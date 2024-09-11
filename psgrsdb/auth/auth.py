import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from fastapi import HTTPException, status
from jwt import PyJWTError
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")

def create_token(payload: dict, expires_delta: timedelta = timedelta(hours=1)) -> str:
    expire = datetime.now() + expires_delta
    to_encode = payload.copy()
    to_encode.update({"exp": expire.timestamp()})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm="HS256")
    return encoded_jwt

def token_check(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithm="HS256")
        if datetime.now() > datetime.fromtimestamp(payload.get("exp")):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token has expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return True
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )