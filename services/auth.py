import requests
from config.settings import SUPABASE_URL, SUPABASE_KEY

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Content-Type": "application/json"
}

def sign_up(email, password):
    url = f"{SUPABASE_URL}/auth/v1/signup"
    payload = {"email": email, "password": password}
    res = requests.post(url, json=payload, headers=HEADERS)
    return res.json()

def sign_in(email, password):
    url = f"{SUPABASE_URL}/auth/v1/token?grant_type=password"
    payload = {"email": email, "password": password}
    res = requests.post(url, json=payload, headers=HEADERS)
    return res.json()

def get_user(token):
    url = f"{SUPABASE_URL}/auth/v1/user"
    headers = {**HEADERS, "Authorization": f"Bearer {token}"}
    res = requests.get(url, headers=headers)
    return res.json()