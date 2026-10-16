
import streamlit as st

st.set_page_config(
    page_title="You Made IT Girl!",
    page_icon="🎀",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Great+Vibes&display=swap');

.stApp {
    background: linear-gradient(135deg, #1a1028, #702454, #d64f91);
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding-top: 0;
    padding-bottom: 0;
    max-width: 100%;
}

.hero {
    min-height: 95vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 20px;
}

.subtitle {
    font-family: 'Playfair Display', serif;
    color: #ffd5eb;
    font-size: 18px;
    letter-spacing: 5px;
    margin-bottom: 25px;
}

.main-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(45px, 8vw, 100px);
    font-weight: 900;
    color: white;
    line-height: 1.2;
}

.highlight {
    font-family: 'Playfair Display', serif;
    font-size: clamp(65px, 12vw, 145px);
    font-weight: 900;
    line-height: 1.2;
    background: linear-gradient(90deg, #ffb6d9, #ffffff, #ff69b4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.script {
    font-family: 'Great Vibes', cursive;
    font-size: clamp(32px, 5vw, 55px);
    color: #ffe0ef;
    margin-top: 25px;
}

.decor {
    font-size: 30px;
    margin-top: 25px;
}

.footer-text {
    color: #fbcfe8;
    font-size: 13px;
    letter-spacing: 4px;
    margin-top: 25px;
}
</style>

<div class="hero">
    <div class="subtitle">✦ A LITTLE REMINDER ✦</div>
    <div class="main-title">YOU MADE</div>
    <div class="highlight">IT GIRL!</div>
    <div class="script">Look at you go...</div>
    <div class="decor">♡ ✦ 🎀 ✦ ♡</div>
    <div class="footer-text">
        DREAM BIG · SHINE BRIGHT · OWN IT
    </div>
</div>
""", unsafe_allow_html=True)
