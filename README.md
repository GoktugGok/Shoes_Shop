# 👟 Shoes House – E-Ticaret Ayakkabı Mağazası

**Shoes House**, Django ve Bootstrap kullanılarak geliştirilmiş bir e-ticaret platformudur.  
Kullanıcılar ayakkabıları inceleyebilir, sepete ekleyebilir, sipariş verebilir ve hesaplarını yönetebilir.  
Görsel olarak şık, yapısal olarak sağlam! 😎💼

---

## ✨ Özellikler

### 👤 Kullanıcı İşlemleri
- ✅ Kayıt & Giriş sistemi
- ✅ Şifre doğrulama & güncelleme
- ✅ Profil bilgileri düzenleme
- ✅ Güvenli çıkış yapma

### 👟 Ürün Yönetimi
- ✅ Kategoriye göre listeleme (Erkek / Kadın / Çocuk)
- ✅ Filtreleme (renk, numara, topuk yüksekliği vs.)
- ✅ Sepete ekleme / çıkarma
- ✅ Sipariş geçmişi & detayları

### 💳 Ödeme Sistemi
- ✅ Kredi kartı ile ödeme (dummy)
- ✅ Fatura adresi düzenleme
- ✅ Sipariş özeti

### ✉️ İletişim
- ✅ Müşteri mesaj sistemi
- ✅ İletişim formu

---

## 🖼️ Ekran Görüntüleri

### 🏠 Ana Sayfa
![Ana Sayfa](screenshots/home.png)

### 🔐 Giriş Sayfası
![Giriş Sayfası](screenshots/login.png)

### 📝 Kayıt Sayfası
![Kayıt Sayfası](screenshots/register.png)

### 🛒 Sepet
![Sepet](screenshots/cart.png)

### 💳 Ödeme Sayfası
![Ödeme](screenshots/payment.png)

### 👤 Profil Sayfası
![Profil](screenshots/profile.png)

### 👟 Ürün Listesi
![Ürün Listesi](screenshots/products.png)

### 📬 İletişim
![İletişim](screenshots/contact.png)

### 🛠️ Admin Panel
![Admin Panel](screenshots/admin.png)


---

## ⚙️ Kurulum

- git clone https://github.com/GoktugGok/Shoes_Shop.git

- cd shoes-house

- python -m venv venv

- Windows: venv\Scripts\activate

- Mac/Linux: source venv/bin/activate


- python manage.py migrate

- python manage.py createsuperuser  # (Opsiyonel)

- python manage.py runserver



