# Bot WhatsApp Bisnis  

Bot WhatsApp otomatis untuk bisnis dengan fitur respons otomatis dan pengiriman media.  

## Fitur Utama  

- Respons otomatis berdasarkan kata kunci  
- Pengiriman gambar, PDF, dan multi-media  
- Konfigurasi mudah dengan file .env  

## Cara Penggunaan  

1. Clone repository ini  
2. Install dependencies: `pip install -r requirements.txt`  
3. Salin file `.env.example` menjadi `.env` dan isi kredensial Anda  
4. Jalankan server: `python app.py`  
5. Siapkan webhook di Twilio yang mengarah ke endpoint `/whatsapp`  

## Pengiriman Media  

Untuk mengirim media, gunakan file `media_sender.py`:  

```python  
from media_sender import kirim_gambar  

kirim_gambar("https://example.com/logo.jpg", "Ini logo kami")  
