import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Ömer Software Market", page_icon="🚀", layout="wide")

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
st.header("🤖 Yapay Zeka Bölümü")
c1, c2 = st.columns(2)

with c1:
    st.subheader("Akıllı Chatbot (GUI)")
    st.write("Masaüstü için hesap makinesi ve oyun içeren klasik sürüm.")
    st.link_button("📥 Chatbot'u İndir", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/chatbot_gui.py")

with c2:
    st.subheader("ÖmerGPT (Web)")
    st.write("Şu an yayında olan yapay zekama geri dön.")
    # BURAYA YAPAY ZEKA SİTENİN LİNKİNİ YAZ KANKA:
    st.link_button("🌐 Yapay Zekayı Aç", "https://omer-gpt-web.streamlit.app")

st.divider()

# --- 3. BÖLÜM: BLOK KODLAMA ---
st.header("🧩 mBlock Projeleri")
b1, b2 = st.columns(2)

with b1:
    st.write("**ÖMERf mBlock**")
    st.link_button("Dosyayı İndir", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/%C3%96MERf.mblock")

with b2:
    st.write("**mBlocky Ana**")
    st.link_button("Dosyayı İndir", "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/mblocky.mblock")

st.sidebar.title("👤 Yapımcı: Ömer")
st.sidebar.write("6. Sınıf Yazılım Geliştiricisi")