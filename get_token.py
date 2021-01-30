"""
You should run this script to get your token and token-secret, then add them to config.py.
"""
from config import *
from trello.util import create_oauth_token


if __name__ == '__main__':
    create_oauth_token(key=api_key, secret=api_secret)
