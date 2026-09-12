from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests
import pandas as pd
from sqlalchemy import create_engine

# 1. ETL İşlemimizi Bir Fonksiyon Haline Getiriyoruz
def run_kripto_etl():
    url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=50&page=1&sparkline=false"
    ham_veri = requests.get(url).json()

    df = pd.DataFrame(ham_veri)
    secilen_kolonlar = ['symbol', 'name', 'current_price', 'total_volume', 'price_change_percentage_24h']
    df = df[secilen_kolonlar]

    df.rename(columns={
        'symbol': 'sembol', 
        'name': 'coin_adi', 
        'current_price': 'fiyat_usd', 
        'total_volume': 'islem_hacmi_usd', 
        'price_change_percentage_24h': 'degisim_24s_yuzde'
    }, inplace=True)
    df.dropna(subset=['fiyat_usd', 'islem_hacmi_usd'], inplace=True)

    # PostgreSQL veritabanı bağlantı motoru oluşturuluyor
    engine = create_engine('postgresql://postgres:admin123@localhost:5432/crypto_db') 
    
    # Veri PostgreSQL'e aktarılıyor
    df.to_sql('gunluk_piyasa_ozeti', engine, if_exists='replace', index=False)
    print("ETL Başarıyla Tamamlandı ve PostgreSQL Veritabanına Yazıldı!")

# 2. Airflow Kuralları (Hata yaparsa ne olacak? Süreç kime ait?)
default_args = {
    'owner': 'ceydauzn',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1, # Hata verirse 1 kere daha dene
    'retry_delay': timedelta(minutes=5), # Tekrar denemeden önce 5 dakika bekle
}

# 3. DAG Tanımlaması (Zamanlayıcı)
# schedule_interval='0 7 * * *' -> Her sabah saat 07:00'de çalıştır (Cron formatı)
dag = DAG(
    'kripto_piyasa_etl_pipeline',
    default_args=default_args,
    description='Kripto verilerini çeken günlük tam otomatik ETL boru hattı',
    schedule_interval='0 7 * * *',
    catchup=False
)

# 4. Görevi (Task) DAG içine ekleme
gorev_etl = PythonOperator(
    task_id='api_den_veriyi_cek_ve_kaydet',
    python_callable=run_kripto_etl,
    dag=dag,
)

gorev_etl