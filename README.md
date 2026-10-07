# Zhain Tour and Travel — Django Website

Website company profile + katalog paket wisata + layanan + galeri/testimoni + form booking WhatsApp.

## 1. Menjalankan di Windows

Pastikan Python sudah terpasang.

```powershell
cd zhain_tour_travel_django
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Buka: http://127.0.0.1:8000/

## 2. Admin

Buat akun admin:

```powershell
python manage.py createsuperuser
```

Lalu buka: http://127.0.0.1:8000/admin/

Form booking yang masuk akan tersimpan di menu **Booking Inquiries**.

## 3. Yang perlu diganti sebelum website dipakai sungguhan

1. Nomor WhatsApp admin di `zhain_project/settings.py` atau environment variable `WHATSAPP_NUMBER`.
2. Alamat, Instagram, dan kontak pada footer `core/templates/core/base.html`.
3. Company profile, visi, dan misi di `core/templates/core/home.html`.
4. Harga, fasilitas, itinerary, durasi, dan detail setiap paket di `core/views.py`.
5. Foto contoh pada `core/views.py` dan `home.html` dengan dokumentasi asli Zhain.
6. Testimoni contoh pada `home.html` dengan testimoni pelanggan yang benar-benar ada.

## 4. Struktur utama

- `core/views.py` → data paket, layanan, galeri dan proses form booking.
- `core/templates/core/home.html` → isi halaman utama.
- `core/static/core/css/style.css` → desain/responsive.
- `core/static/core/js/main.js` → menu mobile dan interaksi paket.
- `core/static/core/img/logo-zhain.png` → logo yang diberikan.
- `core/models.py` → menyimpan data inquiry booking.

## Catatan foto

Versi awal menggunakan foto online sebagai placeholder supaya tampilan website langsung terasa seperti website travel. Untuk website produksi, sebaiknya foto diganti dengan dokumentasi asli Zhain agar lebih terpercaya dan konsisten dengan brand.
