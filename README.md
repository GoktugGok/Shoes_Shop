Shoes House - E-ticaret Ayakkabı Mağazası
Proje Açıklaması
Shoes House, Django ve Bootstrap kullanılarak geliştirilmiş bir e-ticaret ayakkabı mağazası uygulamasıdır. Kullanıcıların çeşitli ayakkabı ürünlerini görüntüleyebileceği, satın alabileceği ve hesap yönetimi yapabileceği bir platform sunar.

Özellikler
Kullanıcı İşlemleri
✅ Kullanıcı girişi ve kayıt sistemi

✅ Şifre doğrulama

✅ Profil bilgileri yönetimi

✅ Çıkış yapma

Ürün Yönetimi
✅ Kategorilere göre ayakkabı görüntüleme (Erkek/Kadın/Çocuk)

✅ Filtreleme seçenekleri (renk, numara, yükseklik)

✅ Sepet işlemleri

✅ Sipariş takibi

Ödeme Sistemi
✅ Kredi kartı ile ödeme

✅ Fatura adresi yönetimi

✅ Sipariş özeti görüntüleme

İletişim
✅ Müşteri mesajları

✅ İletişim formu

Ekran Görüntüleri

Kurulum
Repoyu klonlayın:

bash
git clone https://github.com/kullaniciadi/shoes-house.git
cd shoes-house
Sanal ortam oluşturun ve etkinleştirin:

bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
Gerekli paketleri yükleyin:

bash
pip install -r requirements.txt
Veritabanını oluşturun:

bash
python manage.py migrate
Geliştirme sunucusunu başlatın:

bash
python manage.py runserver
Kullanılan Teknolojiler
Backend: Django

Frontend: Bootstrap, HTML, CSS

Veritabanı: SQLite (geliştirme), PostgreSQL (production)

Diğer: jQuery (etkileşimler için)
