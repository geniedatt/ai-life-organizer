import streamlit as st


def upgrade_page():

    st.title("🚀 Upgrade to AI Life Pro")

    st.write(
        """
Unlock the full power of your **AI Strategic Command Center**.

Upgrade to **Pro** to activate advanced AI features designed to help you
execute your goals faster and stay strategically focused.
"""
    )

    st.divider()

    st.subheader("🔓 Pro Features")

    st.write("""
• AI Strategic Planner  
• AI Daily Schedule Generator  
• Chief of Staff AI  
• Adaptive Strategy Engine  
• AI Life Strategy System
""")

    st.divider()

    st.subheader("💰 Pricing")

    st.success("$15 / month")

    st.write(
        """
Cancel anytime.  
Start using the full AI Life System today.
"""
    )

    st.divider()

    stripe_link = "https://buy.stripe.com/test_cNi3coeYW91z8VC5IG4Vy00"

    st.link_button("🚀 Upgrade to Pro", stripe_link)

    from services.subscription import activate_pro


    st.divider()

    st.subheader("Developer Test Unlock")

    if st.button("Activate Pro (Testing)"):
        activate_pro()
        st.success("Pro features activated.")