# Kitabevi Veritabanı Yönetim Sistemi

Bu proje, bir **kitabevi** için MySQL tabanlı bir veritabanı oluşturma, sorgulama ve veri yönetimi işlemlerini gerçekleştiren Python programıdır.

## 📋 Görevler ve Özellikler

1. **Veritabanı Tablolarını Oluşturma**  
   - Tablolar: `author`, `publisher`, `book`, `author_of`, `phw1`
   - Tablolar, belirtilen şemaya uygun şekilde oluşturulmaktadır.

2. **Tablolara Veri Ekleme**  
   - Veriler `data` klasöründeki `.txt` dosyalarından eklenir.

3. **SQL Sorguları**  
   - **Sorgu 1-7**: Belirli kitap, yazar ve yayınevi bilgilerini içeren sorgular gerçekleştirilir.  
   - **Toplu Ekleme**: `phw1` tablosuna en düşük puanlı kitaplar BULK ekleme yöntemiyle eklenir.  
   - **Update ve Delete İşlemleri**: Kitapların `rating` güncellemesi ve yayınevi kayıtlarının silinmesi.

4. **Veritabanı Tablolarını Silme**  
   - Oluşturulan tabloların tamamı silinir.

## 📁 Dosya Yapısı

- **bookdb.py**: Proje kodlarının tamamı bu dosyada yer almaktadır.  
- **data/**: Tabloları doldurmak için kullanılan veri dosyalarını içerir.  

## 🚀 Çalıştırma Adımları

1. **MySQL Kurulumu**  
   MySQL sunucusu kurulmalı ve veritabanı bağlantısı yapılandırılmalıdır.  
   [Kurulum Linki](https://dev.mysql.com/downloads/installer/)

2. **Python Ortamını Kurun**  
   Gerekli Python paketlerini yükleyin:  
   ```bash
   pip install mysql-connector-python
3. **Programı Çalıştırın** 
evaluation.py dosyasını çalıştırarak kodunuzu test edebilirsiniz.
📝 Kurallar
Programlama dili: Python
Kodun bookdb.py dosyasında yer alması gerekmektedir.
Veritabanı sorguları MySQL kullanarak çalıştırılacaktır.
Sonuçlar belirtilen formatta döndürülmelidir.
