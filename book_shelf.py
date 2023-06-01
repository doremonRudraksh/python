class bookshelf:
    
    def __init__(self, name, author, price, pub_yr):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_pub_yr = pub_yr
        
    def add_block(self):
          print("Book Name : " + self.book_name)
          print("Book author : " + self.book_author)
          print("Book price : " + str(self.book_price) + "/ -")
          print("Book publishing year : " + str(self.book_pub_yr))
          print("book added")

    def year_sice_published(self):
        yrs_ago_pub  = 2022- self.book_pub_yr
        print("the book was published " + str(yrs_ago_pub) + " years ago " )

book1 = bookshelf("Harry Potter & The Philosopher's Stone", "J.K. Rowling", 1928, 1997)
book1.add_block()
book1.year_sice_published()

book2 = bookshelf("Diary Of A Wimpy Kid", "Jeff Kinney", 700, 2017)
book2.add_block()
book2.year_sice_published()