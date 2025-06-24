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

> 📸 *Buraya uygulamanın birkaç ekran görüntüsünü koyarsan şov olur!*  
> Örn: `assets/screens/homepage.png`, `cart.png`, `admin-panel.png` gibi

---

## ⚙️ Kurulum

# 1. Repoyu Klonla
git clone https://github.com/GoktugGok/Shoes_Shop.git
cd shoes-house

# 2. Sanal Ortam Oluştur ve Aktif Et
# Windows:
python -m venv venv
venv\Scripts\activate

# Mac/Linux:
python3 -m venv venv
source venv/bin/activate

# 4. Veritabanını Hazırla
python manage.py migrate

# 5. Admin Kullanıcısı Oluştur (opsiyonel ama tavsiye edilir 😎)
python manage.py createsuperuser

# 6. Sunucuyu Başlat
python manage.py runserver

# Tarayıcıya yaz:
# http://127.0.0.1:8000/
# http://127.0.0.1:8000/admin/


