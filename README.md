# 📊 Proyek Analisis Data E-Commerce

## 📌 Deskripsi Proyek
Proyek ini bertujuan untuk melakukan analisis data pada dataset e-commerce guna menjawab beberapa pertanyaan bisnis, yaitu:

1. Bagaimana tren jumlah pesanan (order) setiap bulan?
2. Metode pembayaran apa yang paling sering digunakan oleh pelanggan?

Analisis dilakukan melalui tahapan data wrangling, exploratory data analysis (EDA), hingga visualisasi data dalam bentuk dashboard interaktif menggunakan Streamlit.

---

## 📂 Dataset
Dataset yang digunakan merupakan E-Commerce Public Dataset yang terdiri dari beberapa tabel, seperti:
- customers_dataset
- orders_dataset
- order_items_dataset
- order_payments_dataset
- products_dataset

---

## 🔧 Tools & Library
Library yang digunakan dalam proyek ini:
- pandas==2.2.2
- matplotlib==3.8.4
- streamlit==1.33.0

---

## 🔍 Insight Utama

### 📈 Tren Pesanan
- Jumlah pesanan menunjukkan fluktuasi dari waktu ke waktu.
- Terdapat beberapa periode dengan peningkatan signifikan.
- Pola ini dapat dimanfaatkan untuk strategi bisnis.

### 💳 Metode Pembayaran
- Metode pembayaran didominasi oleh **credit card**.
- Diikuti oleh **boleto** dengan jumlah cukup tinggi.
- Metode lain seperti voucher dan debit card digunakan lebih sedikit.

---

## ⚙️ Setup Environment

### Menggunakan Anaconda
```bash
conda create --name ecommerce-env python=3.10
conda activate ecommerce-env
pip install -r requirements.txt
```

### ▶️ Menjalankan Dashboard

Untuk menjalankan dashboard secara lokal, ikuti langkah-langkah berikut:

1. Pastikan semua library sudah terinstall:
```bash
pip install -r requirements.txt
```
2. Masuk ke folder dashboard:
```bash
cd dashboard
```
4. Jalankan aplikasi Streamlit:
```bash
streamlit run dashboard.py
```
6. Buka di browser:
```bash
http://localhost:8501
```