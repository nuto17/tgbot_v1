import logging.config
import requests
from rauth import OAuth2Service
import logging
import os 
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

id_genius=os.getenv('genius_client_id')
secret_genius=os.getenv('genius_client_secret')
access_genius=os.getenv('genius_acess_token')


genius=OAuth2Service(
    client_id=id_genius,
    client_secret=secret_genius,
    name='genius',
    authorize_url='https://api.genius.com/oauth/authorize',
    access_token_url='https://api.genius.com/oauth/token',
    base_url='https://api.genius.com/' 
)
redirect_uri='http://localhost:8000/callback'
params={
    'redirect_uri':redirect_uri,
    'response_type':'code',
    'scope':'me'
}
authorize_url=genius.get_authorize_url(**params)
print(f'перейди по ссылке: {authorize_url}')
