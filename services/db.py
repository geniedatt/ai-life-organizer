import requests
from config.settings import SUPABASE_URL, SUPABASE_KEY

BASE_URL = f"{SUPABASE_URL}/rest/v1"

def _headers(token):
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

# -------------------------
# USER PROFILE
# -------------------------
def get_profile(token):
    res = requests.get(
        f"{BASE_URL}/profiles",
        headers=_headers(token)
    )
    return res.json()

def create_profile(token, user_id, email):
    data = {
        "id": user_id,
        "email": email,
        "is_pro": False
    }
    requests.post(
        f"{BASE_URL}/profiles",
        headers=_headers(token),
        json=data
    )

# -------------------------
# UPDATE PRO STATUS
# -------------------------
def set_pro_user(token, user_id):
    requests.patch(
        f"{BASE_URL}/profiles?id=eq.{user_id}",
        headers=_headers(token),
        json={"is_pro": True}
    )