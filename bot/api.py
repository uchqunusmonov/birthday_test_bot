import requests

BASE_URL = 'https://5e07-92-63-204-109.ngrok-free.app/api/'


def create_user(name, user_id, username):
    url = BASE_URL + 'users/'
    post = requests.post(url, data={
        'username': username,
        'user_id': user_id,
        'name': name
    })


def get_birthdays():
    url = BASE_URL + 'birthdays/'
    response = requests.get(url)
    return response.json()


def get_admins():
    url = BASE_URL + 'admins/'
    response = requests.get(url)
    return response.json()
