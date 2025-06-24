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
- ✅ Filtreleme (renk, numara, bilek yüksekliği vs.)
- ✅ Sepete ekleme / çıkarma
- ✅ Sipariş geçmişi & detayları

### 💳 Ödeme Sistemi
- ✅ Kredi kartı ile ödeme
- ✅ Fatura adresi düzenleme
- ✅ Sipariş özeti

### ✉️ İletişim
- ✅ Müşteri mesaj sistemi
- ✅ İletişim formu

---

## 🖼️ Ekran Görüntüleri

### 🏠 Ana Sayfa  
Kategorilere ayrılmış ürünler, kampanyalar ve öne çıkan ayakkabılar.

![Ana Sayfa](screenshots/home.png)

### 🔐 Giriş Sayfası  
Kullanıcı e-posta ve şifre ile giriş formu.

![Ana Sayfa](screenshots/home.png)

### 📝 Kayıt Sayfası  
Yeni kullanıcı oluşturma ekranı.

![Ana Sayfa](screenshots/home.png)

### 🛒 Sepet  
Kullanıcının sepete eklediği ürünleri ve toplam tutarı gösterir.

![Ana Sayfa](screenshots/home.png)

### 💳 Ödeme Sayfası  
Fatura bilgileri ve kredi kartı formu.

![Ana Sayfa](screenshots/home.png)

### 👤 Profil Sayfası  
Kullanıcı bilgileri, adres ve şifre yönetimi.

![Ana Sayfa](screenshots/home.png)

### 🔎 Arama  
Ürünler arasında isme göre arama yapılabilen sayfa.  
> 🔍 Kullanıcılar ürün adı yazarak arama yapabilir.

![Ana Sayfa](screenshots/home.png)

### 📦 Sipariş Geçmişi (My Orders)  
Kullanıcının daha önce verdiği siparişlerin listelendiği sayfa.  
> 📋 Sipariş numarası, tarih, toplam tutar ve durumu gösterilir.

![Ana Sayfa](screenshots/home.png)

### 👟 Ürün Detay Sayfası  
Seçilen ürünün büyük görseli, açıklaması, fiyatı ve sepete ekleme butonu.  
> 🧾 Numara, renk, stok durumu gibi bilgiler içerir.

![Ana Sayfa](screenshots/home.png)

### 📬 İletişim  
Müşteri mesaj formu ve iletişim bilgileri.

![Ana Sayfa](screenshots/home.png)

### 🛠️ Admin Panel  
Ürünleri, siparişleri ve kullanıcıları yöneten yönetici ekranı.

![Ana Sayfa](screenshots/home.png)


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



