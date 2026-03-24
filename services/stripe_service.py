import stripe
from config.settings import STRIPE_SECRET_KEY, STRIPE_PRICE_ID, APP_URL

stripe.api_key = STRIPE_SECRET_KEY

def create_checkout_session(user_id):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        mode="subscription",
        line_items=[{
            "price": STRIPE_PRICE_ID,
            "quantity": 1,
        }],
        success_url=f"{APP_URL}?success=true",
        cancel_url=f"{APP_URL}?canceled=true",
        metadata={
            "user_id": user_id
        }
    )
    return session.url