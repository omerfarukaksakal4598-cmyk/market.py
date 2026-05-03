import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Ömer'in Dijital Marketi", page_icon="🛍️", layout="centered")

st.title("🛍️ Ömer'in Dijital Marketi")
st.markdown("---")

# --- 1. ÜRÜN: LABİRENT OK TEMİZLEME OYUNU ---
st.header("🎮 Oyunlar")
st.subheader("🏹 Labirent: Ok Temizleme")
st.write("Profesyonel labirent tasarımı ve bölümlü yapısıyla yeni oyunumuzu deneyin!")

# GitHub'daki direkt indirme linkin
oklar_link = "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/oklar.py"

st.link_button("📥 Oyunu Bilgisayarına İndir", oklar_link, use_container_width=True)

st.divider()

# --- 2. ÜRÜN: MINECRAFT OYUNU ---
st.header("⛏️ Minecraft Dünyası")
st.subheader("Minecraft (Full Versiyon)")
st.write("Bloklarla hayalindeki dünyayı inşa et!")

# Minecraft oyun dosyası için indirme linki (Buraya oyunun linkini koyabilirsin)
minecraft_link = "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/minecraft.py"

st.link_button("📥 Minecraft Oyunu İndir", minecraft_link, use_container_width=True)

st.divider()

# --- 3. ÜRÜN: AKILLI CHATBOT ---
st.header("🤖 Yapay Zeka Araçları")
st.subheader("Akıllı Chatbot (ÖmerGPT)")
st.write("Groq altyapısını kullanan hızlı ve zeki bir asistan.")

chatbot_kod = """
# ÖmerGPT Chatbot Kodları
import streamlit as st
from groq import Groq
st.title('ÖmerGPT Asistan')
"""

# Kodun ekranda görünmemesi için download_button kullanıldı
st.download_button(
    label="📥 Chatbot Kodunu İndir (.py)",
    data=chatbot_kod,
    file_name="chatbot_omer.py",
    mime="text/plain",
    use_container_width=True
)

st.divider()

# --- İLETİŞİM VE BİLGİ ---
st.sidebar.title("🏪 Market Bilgisi")
st.sidebar.info("Bu marketteki tüm içerikler Ömer tarafından geliştirilmiştir.")
st.sidebar.write("📌 **Sürüm:** 1.0.5")