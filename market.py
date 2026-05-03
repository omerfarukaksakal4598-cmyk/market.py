import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Ömer'in Dijital Portalı", page_icon="🛍️", layout="wide")

# --- TASARIM (Market Şıklığı) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { border-radius: 20px; height: 3em; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🛍️ Ömer'in Dijital Marketi ve Oyun Portalı")
st.write("Hoş geldin! Aşağıdan tüm projelerime ulaşabilir ve bilgisayarına indirebilirsin.")
st.divider()

# --- KATEGORİ: OYUNLAR ---
st.header("🎮 Oyun Dünyası")
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏹 Labirent: Ok Temizleme")
    st.write("Profesyonel labirent tasarımı ve bölümlü yapısıyla yeni nesil puzzle oyunu.")
    # GitHub'dan direkt indirme linki
    oklar_link = "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/oklar.py"
    st.link_button("📥 Ok Oyununu İndir", oklar_link, use_container_width=True)

with col2:
    st.subheader("⛏️ Minecraft (Ömer Edition)")
    st.write("Hayalindeki dünyayı inşa et! TLauncher ve Windows 10 uyumlu versiyon.")
    # Minecraft dosyası linki
    minecraft_link = "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/minecraft.py"
    st.link_button("📥 Minecraft İndir", minecraft_link, use_container_width=True)

st.divider()

# --- KATEGORİ: YAZILIM VE EĞİTİM ---
st.header("💻 Yazılım ve Rehberler")
col3, col4 = st.columns(2)

with col3:
    st.subheader("🤖 ÖmerGPT Chatbot")
    st.write("Hızlı, zeki ve Groq altyapılı kişisel asistan.")
    chatbot_kod = "import streamlit as st\n# ÖmerGPT Chatbot Kodları buraya gelecek"
    # Kodun ekranda açılmasını engelleyen güvenli indirme butonu
    st.download_button(
        label="📥 Chatbotu (.py) Olarak İndir",
        data=chatbot_kod,
        file_name="omer_chatbot.py",
        mime="text/plain",
        use_container_width=True
    )

with col4:
    st.subheader("📝 Okula Alışma Kılavuzu")
    st.write("Yeni başlayanlar için hazırladığım hikayeleştirilmiş rehber.")
    rehber_metni = "Okulun ilk günü heyecanlıdır... (Rehberin tam metni)"
    st.download_button(
        label="📥 Okul Rehberini İndir",
        data=rehber_metni,
        file_name="okul_rehberi.txt",
        mime="text/plain",
        use_container_width=True
    )

st.divider()

# --- KATEGORİ: KODLAMA PROJELERİ ---
st.header("🧩 mBlock & Scratch Projeleri")
col5, col6 = st.columns(2)

with col5:
    st.subheader("🌀 Labirent Oyunu (mBlock)")
    st.write("Can sistemli ve hız değişkenli özel mBlock projesi.")
    st.info("Bu proje yakında markete eklenecek!")

with col6:
    st.subheader("⚙️ Sistem Hızlandırıcı")
    st.write("Windows 10 için RAM temizleme ve hızlandırma ipuçları.")
    st.write("- Chrome yerine daha az RAM kullanan tarayıcıları dene.")
    st.write("- Arka plan uygulamalarını kapat.")

# --- ALT BİLGİ ---
st.sidebar.title("🏪 Market Bilgisi")
st.sidebar.write("**Geliştirici:** Ömer Faruk")
st.sidebar.write("**İşletim Sistemi:** Windows 10")
st.sidebar.success("Tüm projeler günceldir!")