from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, JSONResponse

from httpx import get, post
from datetime import timedelta

from utils.jwt_maker import jwt_maker
from utils.redis import set_cache, get_cache

from env import DISCORD_REDIRECT_URI, DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET, COOKIE_DOMAIN

API_ENDPOINT = 'https://discord.com/api'

data = {
    'grant_type': 'authorization_code',
    'redirect_uri': DISCORD_REDIRECT_URI
}

router = APIRouter()


@router.get('/discord')
async def discord_auth(code: str):
    target_url = get_cache('JWT-LAST-URL')
    data['code'] = code

    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    response = post(f'{API_ENDPOINT}/oauth2/token', data = data, headers = headers, auth = (DISCORD_CLIENT_ID, DISCORD_CLIENT_SECRET))
    payload = response.json()

    access_token = payload['access_token']
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': f'Bearer {access_token}'
    }
    response = get(f'{API_ENDPOINT}/users/@me', headers = headers)
    payload = response.json()

    if not True: return {}

    response = JSONResponse(content = {'message': 'Redirecting and setting cookie'})
    response.set_cookie(
        key = 'my_cookie',
        value = jwt_maker(),
        max_age = timedelta(days = 7),
        expires = timedelta(days = 7),
        domain = COOKIE_DOMAIN,
    )

    return RedirectResponse(url = target_url, headers = response.headers)


@router.get('/discord/redirect')
async def discord_redirect(request: Request):
    referer = request.headers.get('Referer')
    set_cache('JWT-LAST-URL', referer)

    target_url = f'https://discord.com/oauth2/authorize?client_id=1346521666007728268&response_type=code&scope=email+identify&redirect_uri={DISCORD_REDIRECT_URI}'
    return RedirectResponse(url = target_url)
