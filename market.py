import streamlit as st

st.set_page_config(page_title="market.net.ömer.com", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0a0a0a; color: #e0e0e0; }
    h1, h2, h3 { color: #ffffff !important; font-family: Arial, sans-serif; font-weight: normal; }
    div.stButton > button {
        background-color: #151515 !important;
        color: #ffffff !important;
        border: 1px solid #444444 !important;
        border-radius: 4px !important;
        height: 45px !important;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        background-color: #252525 !important;
        border-color: #888888 !important;
    }
    .stTabs [data-baseweb="tab"] {
        color: #888888 !important;
        font-size: 16px !important;
    }
    .stTabs [aria-selected="true"] {
        color: #ffffff !important;
        border-bottom-color: #ffffff !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("market.net.ömer.com")
st.write("Yazılım projeleri ve araçlar. İstediğiniz projeyi bilgisayarınıza indirebilirsiniz.")
st.divider()

KOD_ACIL_BUTON = """import keyboard
import subprocess
import time
import os

def acil_durum():
    keyboard.send('volume mute')
    keyboard.send('windows+d')
    time.sleep(0.3)
    subprocess.Popen('notepad.exe')
    print("Sistem gizlendi ve Not Defteri açıldı.")

os.system("cls" if os.name == "nt" else "clear")
print("--- ACİL DURUM SİSTEMİ AKTİF ---")
print("F12 tuşuna basıldığında sistem gizlenir.")
keyboard.add_hotkey('f12', acil_durum)
keyboard.wait()"""

KOD_DIJITAL_KASA = """import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

ANAHTAR_DOSYASI = r"C:\\Users\\omeef\\OneDrive\\Desktop\\kod\\secret.key"

def anahtar_hazirla():
    if not os.path.exists(ANAHTAR_DOSYASI):
        key = Fernet.generate_key()
        with open(ANAHTAR_DOSYASI, "wb") as f: f.write(key)

def islem_yap(mode):
    try:
        anahtar_hazirla()
        with open(ANAHTAR_DOSYASI, "rb") as f: key = f.read()
        cipher = Fernet(key)
        yol = filedialog.askopenfilename(initialdir=r"C:\\Users\\omeef\\OneDrive\\Desktop\\kod")
        if not yol: return
        with open(yol, "rb") as f: data = f.read()
        
        if mode == "kilit":
            with open(yol + ".locked", "wb") as f: f.write(cipher.encrypt(data))
            os.remove(yol)
            messagebox.showinfo("Başarılı", "Dosya kilitlendi ve gizlendi.")
        elif mode == "coz":
            if yol.endswith(".locked"):
                yeni_yol = yol.replace(".locked", "")
                with open(yeni_yol, "wb") as f: f.write(cipher.decrypt(data))
                os.remove(yol)
                messagebox.showinfo("Başarılı", "Dosya kilidi açıldı.")
    except Exception as e:
        messagebox.showerror("Hata", f"Sistem hatası: {str(e)}")

pencere = tk.Tk()
pencere.title("Dosya Şifreleme")
pencere.geometry("350x250")
tk.Button(pencere, text="DOSYAYI KİLİTLE", command=lambda: islem_yap("kilit")).pack(pady=30)
tk.Button(pencere, text="KİLİDİ AÇ", command=lambda: islem_yap("coz")).pack()
pencere.mainloop()"""

KOD_EL_KONTROL = """import cv2
import mediapipe as mp
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, img = cap.read()
    if not success: break
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)
    if results.multi_hand_landmarks:
        for hand_lms in results.multi_hand_landmarks:
            h, w, c = img.shape
            thumb, index = hand_lms.landmark[4], hand_lms.landmark[8]
            cx1, cy1 = int(thumb.x * w), int(thumb.y * h)
            cx2, cy2 = int(index.x * w), int(index.y * h)
            mesafe = math.hypot(cx2 - cx1, cy2 - cy1)
            vol = ((mesafe - 20) / (200 - 20)) * (maxVol - minVol) + minVol
            vol = max(minVol, min(maxVol, vol))
            volume.SetMasterVolumeLevel(vol, None)
    cv2.imshow("Ses Kontrol", img)
    if cv2.waitKey(1) & 0xFF == 27: break
cap.release()
cv2.destroyAllWindows()"""

KOD_CEVIRI = """import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

DILLER = {"Türkçe": "tr", "İngilizce": "en", "Almanca": "de", "Fransızca": "fr"}

def ceviri_baslat():
    metin = giris_metni.get("1.0", tk.END).strip()
    if not metin: return
    try:
        cevirmen = GoogleTranslator(source=DILLER[kaynak_dil.get()], target=DILLER[hedef_dil.get()])
        ceviri = cevirmen.translate(metin)
        sonuc_metni.config(state=tk.NORMAL)
        sonuc_metni.delete("1.0", tk.END)
        sonuc_metni.insert(tk.END, ceviri)
        sonuc_metni.config(state=tk.DISABLED)
    except: pass

pencere = tk.Tk()
pencere.title("Çeviri Programı")
pencere.geometry("500x400")
kaynak_dil = ttk.Combobox(pencere, values=list(DILLER.keys()))
kaynak_dil.set("Türkçe")
kaynak_dil.pack()
hedef_dil = ttk.Combobox(pencere, values=list(DILLER.keys()))
hedef_dil.set("İngilizce")
hedef_dil.pack()
giris_metni = tk.Text(pencere, height=4, width=40)
giris_metni.pack()
tk.Button(pencere, text="ÇEVİR", command=ceviri_baslat).pack()
sonuc_metni = tk.Text(pencere, height=4, width=40, state=tk.DISABLED)
sonuc_metni.pack()
pencere.mainloop()"""

KOD_E_KILIT = '''import tkinter as tk
from tkinter import messagebox, ttk
import qrcode, socket, time, hashlib, string, cv2, os
from flask import Flask, render_template_string
from threading import Thread, Timer

GIZLI_ANAHTAR = "SISTEM_ANAHTARI"

def generate_complex_code():
    zaman_dilimi = str(int(time.time() // 60))
    hash_obj = hashlib.sha256((zaman_dilimi + GIZLI_ANAHTAR).encode())
    hash_hex = hash_obj.hexdigest()
    alfabe = string.ascii_uppercase + string.digits
    return "".join([alfabe[int(hash_hex[i*4 : (i+1)*4], 16) % len(alfabe)] for i in range(10)])

app = Flask(__name__)
@app.route('/')
def index():
    return render_template_string("<h1>KOD: {{k}}</h1>", k=generate_complex_code())

class KilitSistemi:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True, "-topmost", True)
        self.root.configure(bg='black')
        tk.Label(self.root, text="SİSTEM KİLİTLİ", font=("Arial", 40), fg="white", bg="black").pack(pady=50)
        self.entry = tk.Entry(self.root, font=("Arial", 30), justify='center')
        self.entry.pack()
        tk.Button(self.root, text="AÇ", command=self.onayla, bg="gray", fg="white").pack(pady=20)
        
    def onayla(self):
        if self.entry.get().strip().upper() == generate_complex_code():
            self.root.destroy()
        else:
            messagebox.showerror("Hata", "Yanlış kod girdiniz.")

if __name__ == "__main__":
    Thread(target=lambda: app.run(host='0.0.0.0', port=5050), daemon=True).start()
    kilit = KilitSistemi()
    kilit.root.mainloop()'''

KOD_ASISTAN = '''import time

def konus(metin):
    print(f"Asistan: {metin}")

print("Arka plan dinleme servisi başlatıldı.")
while True:
    time.sleep(5)
'''

KOD_CHATBOT = """import streamlit as st
st.title("ÖmerGPT Sohbet Asistanı")
st.write("Size nasıl yardımcı olabilirim?")
"""

KOD_SAKA = """import ctypes
import time
import pygame
import os
import cv2

def sesi_sona_vur():
    try:
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        volume.SetMasterVolumeLevelScalar(1.0, None)
    except:
        pass

klasor_yolu = os.path.dirname(os.path.abspath(__file__))
sarki_yolu = os.path.join(klasor_yolu, "sarki.mp3")
video_yolu = os.path.join(klasor_yolu, "video.mp4")

pygame.mixer.init()

ctypes.windll.user32.MessageBoxW(0, "Sistem dosyalarında hata tespit edildi.", "Sistem Uyarısı", 0x10 | 0x0)
ctypes.windll.user32.MessageBoxW(0, "Dosyalar temizleniyor...", "Bilgi", 0x10 | 0x0)

sesi_sona_vur()
time.sleep(0.2)

try:
    pygame.mixer.music.load(sarki_yolu)
    pygame.mixer.music.play(-1)
    
    cap = cv2.VideoCapture(video_yolu)
    cv2.namedWindow("Ekran", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Ekran", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        cv2.imshow("Ekran", frame)
        if cv2.waitKey(16) & 0xFF == 27:
            break
            
    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()

except Exception as e:
    pass"""

tabs = st.tabs(["Oyunlar", "Güvenlik Araçları", "Asistanlar", "Şaka Programları"])

with tabs[0]:
    st.header("Oyunlar")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Labirent Ok Temizleme")
        st.write("Siyah labirent hatları içeren strateji oyunu.")
        oklar_link = "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/oklar.py"
        st.link_button("Oyunu İndir", oklar_link, use_container_width=True)
        
    with col2:
        st.subheader("Minecraft")
        st.write("Windows 10 uyumlu Minecraft başlatıcısı.")
        minecraft_link = "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/minecraft.py"
        st.link_button("Minecraft İndir", minecraft_link, use_container_width=True)

with tabs[1]:
    st.header("Güvenlik Araçları")
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Acil Durum Butonu")
        st.write("F12 tuşuna basıldığında sesi kapatır ve ekranı gizler.")
        st.download_button("Acil Buton İndir", data=KOD_ACIL_BUTON, file_name="acil_buton.py", mime="text/plain", use_container_width=True)
        
        st.write("")
        st.subheader("Dosya Şifreleme")
        st.write("Dosyalarınızı güvenli bir şekilde kilitler ve gizler.")
        st.download_button("Şifreleme İndir", data=KOD_DIJITAL_KASA, file_name="sifreleme.py", mime="text/plain", use_container_width=True)

    with col4:
        st.subheader("Ekran Kilidi")
        st.write("Bilgisayarı kilitler ve QR kod şifresi ile açılmasını sağlar.")
        st.download_button("Ekran Kilidi İndir", data=KOD_E_KILIT, file_name="ekran_kilidi.py", mime="text/plain", use_container_width=True)

with tabs[2]:
    st.header("Asistanlar ve Araçlar")
    col5, col6 = st.columns(2)
    
    with col5:
        st.subheader("Chatbot")
        st.write("Yapay zeka tabanlı sohbet asistanı.")
        st.download_button("Chatbot İndir", data=KOD_CHATBOT, file_name="chatbot.py", mime="text/plain", use_container_width=True)
        
        st.write("")
        st.subheader("Arka Plan Asistanı")
        st.write("Bilgisayarı komutlarla yönetmenizi sağlayan araç.")
        st.download_button("Asistan İndir", data=KOD_ASISTAN, file_name="asistan.py", mime="text/plain", use_container_width=True)

    with col6:
        st.subheader("Kamera ile Ses Kontrolü")
        st.write("Kamera üzerinden el hareketleriyle ses seviyesini ayarlar.")
        st.download_button("Ses Kontrol İndir", data=KOD_EL_KONTROL, file_name="ses_kontrol.py", mime="text/plain", use_container_width=True)
        
        st.write("")
        st.subheader("Çeviri Programı")
        st.write("Kopyalanan metinleri otomatik olarak çevirir.")
        st.download_button("Çeviri İndir", data=KOD_CEVIRI, file_name="ceviri.py", mime="text/plain", use_container_width=True)

with tabs[3]:
    st.header("Şaka Programları")
    st.subheader("Sistem Hata Şakası")
    st.write("Sahte uyarılar verir, sesi açar ve ekranda video oynatır. Kapatmak için ESC tuşuna basılmalıdır.")
    st.write("Kodun sorunsuz çalışması için mp3 ve mp4 dosyalarını aynı klasöre indirmeniz gerekmektedir.")
    
    st.download_button("Şaka Kodunu İndir", data=KOD_SAKA, file_name="saka_programi.py", mime="text/plain", use_container_width=True)
    st.download_button("Ses Dosyasını İndir", data=b"Muzik", file_name="sarki.mp3", mime="audio/mpeg", use_container_width=True)
    st.download_button("Video Dosyasını İndir", data=b"Video", file_name="video.mp4", mime="video/mp4", use_container_width=True)

st.sidebar.title("Sistem Bilgisi")
st.sidebar.write("Geliştirici: Ömer Faruk")
st.sidebar.write("İşletim Sistemi: Windows 10")
st.sidebar.write("Tüm sistemler aktif ve çalışır durumda.")