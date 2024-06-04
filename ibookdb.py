from abc import ABC, abstractmethod
from queryresult import QueryResult
from author import Author
from book import Book
from author_of import Author_of
from publisher import Publisher

class IBOOKDB(ABC):

    @abstractmethod
    def initialize(self):
        pass

    @abstractmethod
    def createTables(self):
        """
         Tanimlanan semaya gore tum tablolari olusturacaksiniz (create).
        
         Bu fonksiyon basariyla olusturulan tablo sayisini dondurmelidir
        """   
        pass

    @abstractmethod
    def dropTables(self):
        """
        Olusturduğunuz (create) tum tablolari siliniz (drop)
        
        @Basariyla silinen (drop edilen) tablo sayisini dondurunuz.
     
        """
        pass

    @abstractmethod
    def insertAuthor(self, authors: list[Author]) -> int:
        """
        Veritabanina Author listesi eklenmelidir
        
        Basariyla eklenen kayit sayisini dondurunuz.

        """

        pass

    @abstractmethod
    def insertBook(self, books: list[Book]) -> int:
        """     
        Veritabanina Book listesi eklenmelidir
        
        @Basariyla eklenen kayit sayisini dondurunuz.
        """
        pass

    @abstractmethod
    def insertPublisher(self, publishers: list[Publisher]) -> int:
        """     
        Veritabanina Publisher listesi eklenmelidir
        
        Basariyla eklenen kayit sayisini dondurunuz.
        """
        pass

    @abstractmethod
    def insertAuthor_of(self, author_ofs: list[Author_of]) -> int:
        """
        Veritabanina Author_of listesi eklenmelidir
        
        @Basariyla eklenen kayit sayisini dondurunuz.   
        """
        pass

    @abstractmethod
    def functionQ1(self) -> list[QueryResult.ResultQ1]:
        """
        * En fazla sayfaya sahip olan kitabin(kitaplarin) isbn, first_publish_year, page_count ve publisher_name 
        * bilgilerini listeleyeceksinz.
        * Sonuçlari isbn'ye gore artan sirada siralamalisiniz.
        * @return [QueryResult.ResultQ1]
        """
        pass

    @abstractmethod
    def functionQ2(self, author_id1: int, author_id2: int) -> list[QueryResult.ResultQ2]:
        """     
        Verilen iki yazarin  birlikte yazdiği kitaplari yayimlayan yayinevlerinin; publisher_id'lerini ve bu yayinevlerinin yayimladiği 
        tum kitaplarin ortalama sayfa sayisini (page_count) listeleyeceksiniz.
        Sonuçlari publisher_id'ye gore artan sirada siralamalisiniz.
        * @param author_id1
        * @param author_id2
        * @return [QueryResult.ResultQ2]
    
        """
        pass

    @abstractmethod
    def functionQ3(self, author_name: str) -> list[QueryResult.ResultQ3]:
        """
        Verilen author_name'e sahip yazar(lar)in en erken yayimlanan kitabinin(kitaplarinin) book_name, category ve first_publish_year bilgilerini listeleyeceksiniz.
        Sonuçlari book_name, category ve first_publish_year'a gore artan sirada siralamalisiniz.
        * @param author_name
        * @return [QueryResult.ResultQ3]
        """
        pass

    @abstractmethod
    def functionQ4(self) -> list[QueryResult.ResultQ4]:
        """
        En az 3 kelime içeren (ornek: "Koc Universitesi Yayinlari") isimlere sahip, en az 3 kitap yayimlamis olan 
        ve tum kitaplarinin ortalama rating'i 3'ten buyuk ($>$) olan yayinevlerinin publisher_id'lerini 
        ve yayinladiklari farkli kategorileri (category) listeleyeceksiniz.
        Not: publisher_name içindeki her kelimenin bir boslukla ayrildiğini varsayabilirsiniz.
        Sonuçlari publisher_id ve category'e gore artan sirada siralamalisiniz.

        * @return [QueryResult.ResultQ4]
        """
        pass

    @abstractmethod
    def functionQ5(self, author_id: int) -> list[QueryResult.ResultQ5]:
        """
        Verilen author_id'nin çalistiği tum yayinevleriyle çalismis yazarlarin  author_id ve author_name bilgilerini listeleyeceksiniz.
        Sonuçlari author_id'ye gore artan sirada siralamalisiniz.
        * @param author_id
        * @return [QueryResult.ResultQ5]
        """
        pass

    @abstractmethod
    def functionQ6(self) -> list[QueryResult.ResultQ6]:
        """
        'Seçici' yazarlarin author_id, isbn(ler)ini listeleyin.
        "Seçici" yazarlar;" yalnizca  kendi kitaplarini yayimlayan yayinevleriyle çalismis olan yazarlardir. (yani, farkli yazarlarin kitaplarini yayinlamamislardir).
        Sonuçlari author id ve ISBN numarasina gore artan sirada siralamalisiniz.
        * @return [QueryResult.ResultQ6]
        """
        pass

    @abstractmethod
    def functionQ7(self, rating: float) -> list[QueryResult.ResultQ7]:
        """
        'Roman' kategorisinde en az 2 kitap yayimlamis olan ve kitaplarinin ortalama rating'i verilen değerden buyuk ( > ) olan yayinevlerinin  
        publisher_id ve publisher_name'lerini  listeleyeceksiniz.
        Sonuçlari publisher_id'ye gore artan sirada siralamalisiniz.
        * @param rating
        * @return [QueryResult.ResultQ7]
        """
        pass

    @abstractmethod
    def functionQ8(self) -> list[QueryResult.ResultQ8]:
        """
        Mağazadaki bazi kitaplar birden fazla kez yayimlanmis olabilir: ayni isimlere (book_name) sahip olmalarina rağmen, 
        farkli isbn'lerle yayimlanmis olabilirler. Bu kitaplarin her biri için, en kuçuk rating'e sahip olanlarinin 
        isbn, book_name ve rating'lerini bulun ve bunlari tek bir BULK insert sorgusu kullanarak phw1 tablosuna kaydedin. 
        Eğer en dusuk puanli birden fazla kitap varsa, o zaman hepsini kaydedin.

        Toplu ekleme isleminden sonra, phw1 tablosundaki tum satirlarin isbn, book_name ve rating'lerini listeleyiniz.
        Isbn'e gore artan sirada siralamalisiniz.
        * @return [QueryResult.ResultQ8]
        """
        pass

    @abstractmethod
    def functionQ9(self, keyword: str) -> float:
        """
        Isimlerinin (book_name) içerisinde verilen anahtar kelime(keyword) olan kitaplarin rating'lerini bir (1) artirin. 
        Maksimum rating 5'ten fazla olamaz, bu nedenle değistirmeden onceki rating 4'ten buyukse, o kitabin rating'ini guncellemeyiniz.
        Guncelleme isleminden sonra, tum kitaplarin rating'lerinin toplamini dondurunuz.
        * @param keyword
        * @return sum of the ratings of all books
        """        
        pass

    @abstractmethod
    def function10(self) -> int:
        """
        Henuz hiç kitap yayimlamamis yayinevlerini publisher tablosundan siliniz.
        Silme isleminden sonra, yayinevleri tablosundaki kayitlarin sayisini dondurunuz.
        """
        pass
