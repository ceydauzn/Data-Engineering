import requests
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

print("1. EXTRACT: CoinGecko API'den veriler çekiliyor...")
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
response = requests.get(url)
ham_veri = response.json()

print("2. TRANSFORM: Veri temizleniyor ve dönüştürülüyor...")
# Ham JSON verisini Pandas tablosuna çeviriyoruz
df = pd.DataFrame(ham_veri)

# Sadece analizde kullanacağımız kolonları seçiyoruz
secilen_kolonlar = ['symbol', 'name', 'current_price', 'total_volume', 'price_change_percentage_24h']
df = df[secilen_kolonlar]

# Kolon isimlerini SQL standartlarına uygun (Türkçe ve küçük harf) hale getiriyoruz
df.rename(columns={
    'symbol': 'sembol',
    'name': 'coin_adi',
    'current_price': 'fiyat_usd',
    'total_volume': 'islem_hacmi_usd',
    'price_change_percentage_24h': 'degisim_24s_yuzde'
}, inplace=True)

# Boş (NULL) verileri temizliyoruz
df.dropna(subset=['fiyat_usd', 'islem_hacmi_usd'], inplace=True)

# Analiz için verinin sisteme giriş (kodun çalıştığı) anını kaydediyoruz
df['kayit_tarihi'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print("3. LOAD: Veritabanına yazılıyor (PostgreSQL)...")

# PostgreSQL veritabanına bağlanma motorunu oluşturuyoruz
engine = create_engine('postgresql://postgres:12345@localhost:5432/crypto_db')

# Veriyi 'gunluk_piyasa_ozeti' tablosuna üst üste ekleyerek (append) kaydeder
df.to_sql('gunluk_piyasa_ozeti', engine, if_exists='append', index=False)

print("ETL Süreci Tamamlandı! Veriler PostgreSQL'e kaydedildi.")