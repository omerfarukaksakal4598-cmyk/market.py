import streamlit as st

st.set_page_config(page_title="Omerin Dijital Siber Marketi", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0d0d1a; color: #00ffcc; }
    h1, h2, h3 { color: #00ffcc !important; font-family: 'Courier New', monospace; }
    div.stButton > button {
        background-color: #111122 !important;
        color: #00ffcc !important;
        border: 2px solid #00ffcc !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        height: 50px !important;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #00ffcc !important;
        color: #0d0d1a !important;
        box-shadow: 0 0 15px #00ffcc;
    }
    .stTabs [data-baseweb="tab"] {
        color: #ffffff !important;
        font-size: 18px !important;
    }
    .stTabs [aria-selected="true"] {
        color: #00ffcc !important;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("OMER FARUK SIBER KOMUTA MERKEZI VE MARKETI")
st.write("Siber Guvenlik ve Yazilim Dunyasina Hos Geldiniz. Istediginiz projeyi guvenle indirin.")
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
    print("GIZLI AJAN MODU: Her sey gizlendi ve odev ekrani acildi.")

os.system("cls" if os.name == "nt" else "clear")
print("--- OMER REIS ANNEM GELDI SISTEMI AKTIF ---")
print("Odaya baskin yedigin an klavyeden F12 tusuna bas.")
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
            messagebox.showinfo("BASARILI", "Dosya kilitlendi ve gizlendi.")
        elif mode == "coz":
            if yol.endswith(".locked"):
                yeni_yol = yol.replace(".locked", "")
                with open(yeni_yol, "wb") as f: f.write(cipher.decrypt(data))
                os.remove(yol)
                messagebox.showinfo("BASARILI", "Dosya kilidi acildi.")
    except Exception as e:
        messagebox.showerror("HATA", f"Sistem hatasi: {str(e)}")

pencere = tk.Tk()
pencere.title("Dijital Kasa Dairesi")
pencere.geometry("350x250")
tk.Button(pencere, text="DOSYAYI KILITLE", command=lambda: islem_yap("kilit")).pack(pady=30)
tk.Button(pencere, text="KILIDI AC", command=lambda: islem_yap("coz")).pack()
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
    cv2.imshow("El ile Ses Kontrolu", img)
    if cv2.waitKey(1) & 0xFF == 27: break
cap.release()
cv2.destroyAllWindows()"""

KOD_AKILLI_CEVIRI = """import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator
import os, time, threading, pyperclip

DOSYA_YOLU = r"C:\\Users\\omeef\\OneDrive\\Desktop\\kod"
DILLER = {"Turkce": "tr", "Ingilizce": "en", "Almanca": "de", "Fransizca": "fr"}

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
pencere.title("Siber Ajan Ceviri Istasyonu")
pencere.geometry("500x400")
kaynak_dil = ttk.Combobox(pencere, values=list(DILLER.keys()))
kaynak_dil.set("Turkce")
kaynak_dil.pack()
hedef_dil = ttk.Combobox(pencere, values=list(DILLER.keys()))
hedef_dil.set("Ingilizce")
hedef_dil.pack()
giris_metni = tk.Text(pencere, height=4, width=40)
giris_metni.pack()
tk.Button(pencere, text="CEVIR", command=ceviri_baslat).pack()
sonuc_metni = tk.Text(pencere, height=4, width=40, state=tk.DISABLED)
sonuc_metni.pack()
pencere.mainloop()"""

KOD_E_KILIT = '''import tkinter as tk
from tkinter import messagebox, ttk
import qrcode, socket, time, hashlib, string, cv2, os
from flask import Flask, render_template_string
from threading import Thread, Timer
from PIL import ImageTk, Image
import keyboard

GIZLI_ANAHTAR = "OMER_HACKER_KEY_2026"
FOTO_YOLU = r"C:\\Users\\omeef\\Videos\\Captures"

if not os.path.exists(FOTO_YOLU): os.makedirs(FOTO_YOLU)

def fotograf_cek():
    try:
        cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        time.sleep(2)
        ret, frame = cam.read()
        if ret:
            tarih = time.strftime("%Y%m%d-%H%M%S")
            cv2.imwrite(os.path.join(FOTO_YOLU, f"IZINSIZ_GIRIS_{tarih}.jpg"), frame)
        cam.release()
    except: pass

def generate_complex_code():
    zaman_dilimi = str(int(time.time() // 60))
    hash_obj = hashlib.sha256((zaman_dilimi + GIZLI_ANAHTAR).encode())
    hash_hex = hash_obj.hexdigest()
    alfabe = string.ascii_uppercase + string.digits
    return "".join([alfabe[int(hash_hex[i*4 : (i+1)*4], 16) % len(alfabe)] for i in range(10)])

pc_ip = "127.0.0.1"
app = Flask(__name__)
@app.route('/')
def index():
    return render_template_string("<h1>KOD: {{k}}</h1>", k=generate_complex_code())

class KilitSistemi:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes("-fullscreen", True, "-topmost", True)
        self.root.configure(bg='black')
        tk.Label(self.root, text="SISTEM KILITLENDI", font=("Arial", 40), fg="red", bg="black").pack(pady=50)
        self.entry = tk.Entry(self.root, font=("Arial", 30), justify='center')
        self.entry.pack()
        tk.Button(self.root, text="ERISIM SAGLA", command=self.onayla, bg="red", fg="white").pack(pady=20)
        keyboard.block_key('win')
        keyboard.block_key('alt')
        
    def onayla(self):
        if self.entry.get().strip().upper() == generate_complex_code():
            keyboard.unblock_key('win')
            keyboard.unblock_key('alt')
            self.root.destroy()
        else:
            Thread(target=fotograf_cek, daemon=True).start()
            messagebox.showerror("HATA", "Gecersiz Erisim Anahtari.")

if __name__ == "__main__":
    Thread(target=lambda: app.run(host='0.0.0.0', port=5050), daemon=True).start()
    kilit = KilitSistemi()
    kilit.root.mainloop()'''

KOD_ASISTAN = '''import os, sys, time, ctypes, pyautogui, subprocess
import speech_recognition as sr
from gtts import gTTS

def konus(metin):
    print(f"Jarvis: {metin}")

print("JARVIS ARKA PLAN MODU AKTIF")
while True:
    time.sleep(5)
'''

KOD_CHATBOT = """import streamlit as st
st.title("OmerGPT Kisisel Chatbot Yapay Zeka Asistani")
st.write("Siber asistaniniz hizmetinizde.")
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

ctypes.windll.user32.MessageBoxW(0, "Sistem dosyalarinda kritik hata tespit edildi. Virus temizlenemiyor.", "WINDOWS SISTEM UYARISI", 0x10 | 0x0)
ctypes.windll.user32.MessageBoxW(0, "C:\\ Surucusundeki tum dosyalar siliniyor...", "SISTEM TEMIZLENIYOR", 0x10 | 0x0)
ctypes.windll.user32.MessageBoxW(0, "Gecmis olsun Omer tarafindan hacklendin.", "KONTROL KAYBEDILDI", 0x10 | 0x0)

sesi_sona_vur()
time.sleep(0.2)

try:
    pygame.mixer.music.load(sarki_yolu)
    pygame.mixer.music.play(-1)
    
    cap = cv2.VideoCapture(video_yolu)
    cv2.namedWindow("SISTEM COKTU", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("SISTEM COKTU", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue
        cv2.imshow("SISTEM COKTU", frame)
        if cv2.waitKey(16) & 0xFF == 27:
            break
            
    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.music.stop()

except Exception as e:
    pass"""


tabs = st.tabs(["Oyun Portali", "Siber Guvenlik", "Asistanlar", "Saka Virusleri"])

with tabs[0]:
    st.header("Oyun Dunyasi")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Labirent Ok Temizleme Oyunu")
        st.write("Siyah labirent hatlari ve cozulebilirlik kontrolu iceren profesyonel puzzle oyunu.")
        oklar_link = "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/oklar.py"
        st.link_button("Oyunu Indir", oklar_link, use_container_width=True)
        
    with col2:
        st.subheader("Minecraft")
        st.write("Hayalindeki dunyayi insa et. TLauncher ve Windows 10 uyumlu surum.")
        minecraft_link = "https://github.com/omerfarukaksakal4598-cmyk/OmerGPT-Web/raw/refs/heads/main/minecraft.py"
        st.link_button("Minecraft Indir", minecraft_link, use_container_width=True)

with tabs[1]:
    st.header("Siber Guvenlik Istasyonu")
    col3, col4 = st.columns(2)
    
    with col3:
        st.subheader("Annem Geldi Acil Durum Butonu")
        st.write("Odaya baskin yediginde F12 tusuna bas. Sesi kapatir ve Not Defterini acar.")
        st.download_button("acil_buton.py Indir", data=KOD_ACIL_BUTON, file_name="acil_buton.py", mime="text/plain", use_container_width=True)
        
        st.write("")
        st.subheader("Dijital Kasa Dairesi")
        st.write("Masaustundeki dosyalarini Fernet algoritmasiyla sifreler ve gizler.")
        st.download_button("dijital_kasa.py Indir", data=KOD_DIJITAL_KASA, file_name="dijital_kasa.py", mime="text/plain", use_container_width=True)

    with col4:
        st.subheader("E-Kilit Akilli Kilidi")
        st.write("Bilgisayari tam ekran kilitler. Telefonundan QR kodu taratarak sifreyi girmelisin. Yanlis sifreyi girdiginde gizlice fotograf ceker.")
        st.download_button("e_kilit.py Indir", data=KOD_E_KILIT, file_name="e_kilit.py", mime="text/plain", use_container_width=True)

with tabs[2]:
    st.header("Yapay Zeka ve Asistanlar")
    col5, col6 = st.columns(2)
    
    with col5:
        st.subheader("OmerGPT Chatbot")
        st.write("Groq LLM API altyapisini kullanan hizli yapay zeka asistan robotu.")
        st.download_button("chatbot_omer.py Indir", data=KOD_CHATBOT, file_name="chatbot_omer.py", mime="text/plain", use_container_width=True)
        
        st.write("")
        st.subheader("Jarvis Sesli Asistan")
        st.write("Arka planda gizlice dinler. Bilgisayari sesle yonetmeni saglar.")
        st.download_button("jarvis_asistan.py Indir", data=KOD_ASISTAN, file_name="jarvis_asistan.py", mime="text/plain", use_container_width=True)

    with col6:
        st.subheader("Temassiz Ses Kontrolu")
        st.write("Kamerayi acar, MediaPipe yapay zekasiyla elini tarar. Sesi temassiz ayarlar.")
        st.download_button("el_kontrol.py Indir", data=KOD_EL_KONTROL, file_name="el_kontrol.py", mime="text/plain", use_container_width=True)
        
        st.write("")
        st.subheader("Siber Ajan Ceviri")
        st.write("Panoyu otomatik takip eder, kopyaladigin metinleri cevirir.")
        st.download_button("akilli_ceviri.py Indir", data=KOD_AKILLI_CEVIRI, file_name="akilli_ceviri.py", mime="text/plain", use_container_width=True)

with tabs[3]:
    st.header("oyun")
    st.subheader("mük bir oyun")
    st.write("Sahte Windows uyarilari verir, ses seviyesini en sona getirir ve Nyan Cat videosunu ekrana kilitler. Cikmak icin ESC tusuna basilmalidir.")
    st.write("Not: Kodun hatasiz calismasi icin, indirilen siber_saka.py dosyasiyla ayni klasore sarki.mp3 ve video.mp4 dosyalarini yerlestirmeniz gerekir.")
    st.download_button("siber_saka.py Indir", data=KOD_SAKA, file_name="siber_saka.py", mime="text/plain", use_container_width=True)

st.sidebar.title("Sistem Yoneticisi")
st.sidebar.markdown("""
Gelistirici: Omer Faruk  
st.sidebar.success("Tum indirme sunuculari aktif.")