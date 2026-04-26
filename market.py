import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Ömer Software Market", page_icon="🚀", layout="wide")

# Arka plan ve stil için küçük bir dokunuş
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #262730;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ Ömer Software Market")
st.info("Kendi geliştirdiğim tüm oyun, kod ve projeler burada. Güle güle kullan kanka!")

# --- 1. BÖLÜM: OYUNLAR VE ANA PROJELER ---
st.header("🎮 Oyunlar ve Uygulamalar")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Ömer'in Turnuva Oyunu")
    st.write("Full Paket: Exe dosyası, ses efektleri ve kayıt sistemi dahildir.")
    st.link_button("🎁 Oyunu İndir (ZIP)", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/Omer_Game_Paket.zip")

with col2:
    st.subheader("Minecraft Clone (Python)")
    st.write("Ursina motoru ile geliştirdiğim dünya yaratma oyunu.")
    st.link_button("🐍 Oyun Kodunu İndir", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/main.py")

st.divider()

# --- 2. BÖLÜM: PYTHON & YAPAY ZEKA ---
st.header("🤖 Python & Chatbot")
c1, c2 = st.columns(2)

with c1:
    st.subheader("Akıllı Chatbot (GUI)")
    st.write("Arayüzlü, hesap makinesi ve oyun menüsü olan klasik sürüm.")
    st.link_button("📥 Chatbot'u İndir", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/chatbot_gui.py")

with c2:
    st.subheader("ÖmerGPT Web (Şu Anki)")
    st.write("Tarayıcı üzerinden çalışan yapay zeka kodunun ham hali.")
    st.link_button("💻 Web Kodunu Al", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/web_gpt.py")

st.divider()

# --- 3. BÖLÜM: BLOK KODLAMA (MBLOCK & SCRATCH) ---
st.header("🧩 Blok Kodlama Projeleri")
b1, b2, b3 = st.columns(3)

with b1:
    st.write("**ÖMERf mBlock**")
    st.link_button("Dosyayı İndir", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/%C3%96MERf.mblock")

with b2:
    st.write("**mBlocky Ana**")
    st.link_button("Dosyayı İndir", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/mblocky.mblock")

with b3:
    st.write("**Scratch Projesi (sb3)**")
    st.link_button("Dosyayı İndir", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/mblocky%20-%20Kopya.sb3")

st.sidebar.title("👤 Yapımcı: Ömer")
st.sidebar.write("6. Sınıf Yazılım Geliştiricisi")
st.sidebar.success("Market linkini arkadaşlarınla paylaşmayı unutma!")