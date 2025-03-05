from fastapi import APIRouter, Response, HTTPException

from utils.jwt import jwt_verify

from env import COOKIE_DOMAIN

router = APIRouter()

@router.get('/verify')
async def verify_token(token: str , response: Response):
    if not token: raise HTTPException(status_code = 401, detail = 'Token not found')

    is_valid = jwt_verify(token)
    response.status_code = 204

    if not is_valid:
        response.delete_cookie('HOST_OWNER_TOKEN', domain = COOKIE_DOMAIN)
        response.status_code = 498

    return response
