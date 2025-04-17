from flask import Flask, request, Response  
from twilio.twiml.messaging_response import MessagingResponse  
import re  
import os  
from dotenv import load_dotenv  

# Load variabel lingkungan dari file .env  
load_dotenv()  

app = Flask(__name__)  

# Ambil kredensial dari variabel lingkungan (lebih aman)  
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")  
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")  
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")  

# Definisi pola kata kunci dan respons  
RESPONS_OTOMATIS = {  
    "harga|biaya|tarif": "Harga layanan CV kami mulai dari Rp150.000. Untuk info lengkap silakan balas 'DAFTAR HARGA'.",  
    "jam|buka|operasional": "Kami buka setiap hari Senin-Jumat (09.00-17.00) dan Sabtu (09.00-15.00).",  
    "lokasi|alamat|dimana": "Alamat kami: Jl. Patimura No. 15, Bandung. Maps: https://goo.gl/maps/abcde",  
    "promo|diskon": "Promo bulan ini: Diskon 20% untuk pembuatan CV Premium! Kode: CVPRO20",  
    "pembayaran|bayar": "Kami menerima pembayaran via transfer bank (BCA/Mandiri/BNI), QRIS, dan OVO/GoPay.",  
    "selesai|lama|durasi": "Pengerjaan CV standar: 2-3 hari kerja. CV Premium: 3-5 hari kerja.",  
    "terima kasih|makasih": "Sama-sama! Senang bisa membantu Anda."  
}  

@app.route('/whatsapp', methods=['POST'])  
def bot_whatsapp():  
    # Ambil pesan masuk dari pengguna  
    pesan_masuk = request.values.get('Body', '').lower()  
    pengirim = request.values.get('From', '')  
    
    # Buat respons Twilio  
    resp = MessagingResponse()  
    
    # Cek apakah pesan cocok dengan pola yang dikenal  
    respons_ditemukan = False  
    for kata_kunci, balasan in RESPONS_OTOMATIS.items():  
        if re.search(kata_kunci, pesan_masuk):  
            resp.message(balasan)  
            respons_ditemukan = True  
            break  
    
    # Jika tidak ada pola yang cocok, kirim pesan default  
    if not respons_ditemukan:  
        resp.message("Terima kasih sudah menghubungi kami. Untuk bantuan cepat, silakan tanyakan tentang: harga, jam operasional, lokasi, promo, metode pembayaran, atau durasi pengerjaan.")  
    
    # Catat interaksi dalam log  
    print(f"Pesan dari {pengirim}: {pesan_masuk}")  
    print(f"Respons: {str(resp)}")  
    
    return str(resp)  

if __name__ == '__main__':  
    app.run(debug=True)  
