# Import library yang diperlukan  
from twilio.rest import Client  
from dotenv import load_dotenv  
import os  

# Load kredensial dari file .env  
load_dotenv()  

# Kredensial Twilio  
account_sid = os.getenv("TWILIO_ACCOUNT_SID")  
auth_token = os.getenv("TWILIO_AUTH_TOKEN")  
twilio_number = os.getenv("TWILIO_NUMBER")  
recipient_number = os.getenv("RECIPIENT_NUMBER")  # Tambahkan ini di .env Anda  

# Inisialisasi klien Twilio  
client = Client(account_sid, auth_token)  

# 1. PENGIRIMAN GAMBAR  
def kirim_gambar(url_gambar, pesan=""):  
    message = client.messages.create(  
        from_=twilio_number,  
        to=recipient_number,  
        media_url=[url_gambar],  
        body=pesan  
    )  
    return f"Gambar terkirim dengan SID: {message.sid}"  

# 2. PENGIRIMAN PDF  
def kirim_pdf(url_pdf, pesan=""):  
    message = client.messages.create(  
        from_=twilio_number,  
        to=recipient_number,  
        media_url=[url_pdf],  
        body=pesan  
    )  
    return f"PDF terkirim dengan SID: {message.sid}"  

# 3. PENGIRIMAN MULTI-MEDIA  
def kirim_multi_media(url_list, pesan=""):  
    message = client.messages.create(  
        from_=twilio_number,  
        to=recipient_number,  
        media_url=url_list,  
        body=pesan  
    )  
    return f"Multiple media terkirim dengan SID: {message.sid}"  

# Contoh penggunaan  
if __name__ == "__main__":  
    # Contoh URL (ganti dengan URL publik Anda)  
    url_gambar = "https://example.com/gambar.jpg"  
    url_pdf = "https://example.com/dokumen.pdf"  
    
    print("Hasil pengujian pengiriman gambar:")  
    print(kirim_gambar(url_gambar, "Berikut adalah logo perusahaan kami"))  
    
    print("\nHasil pengujian pengiriman PDF:")  
    print(kirim_pdf(url_pdf, "Berikut adalah dokumen penting untuk Anda"))  
    
    print("\nHasil pengujian pengiriman multi-media:")  
    print(kirim_multi_media([url_gambar, url_pdf], "Berikut beberapa file untuk Anda"))  
