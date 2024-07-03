import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        # add a book and test if it is in `book_list`.
        b = BookLover('Person', 'person@gmail.com', 'Fantasy')
        b.add_book("Harry Potter", 5)
        assert 'Harry Potter' in b.book_list['book_name'].values, 'Book added did not get put in book list'

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        b = BookLover('Person', 'person@gmail.com', 'Fantasy')
        b.add_book("Harry Potter", 5)
        b.add_book("Harry Potter", 5)
        assert len(b.book_list[b.book_list['book_name'] == 'Harry Potter']) == 1, 'Book added is not just in book list once'
                
    def test_3_has_read(self): 
        # pass a book in the list and test if the answer is `True`.
        b = BookLover('Person', 'person@gmail.com', 'Fantasy')
        b.add_book("Harry Potter", 5)
        b.has_read("Harry Potter")
        
    def test_4_has_read(self): 
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        b = BookLover('Person', 'person@gmail.com', 'Fantasy')
        b.has_read("Harry Potter")
        
    def test_5_num_books_read(self): 
        # add some books to the list, and test num_books matches expected.
        b = BookLover('Person', 'person@gmail.com', 'Fantasy')
        b.add_book("Harry Potter", 5)
        b.add_book("Lord of the Rings", 4)
        b.add_book("Game of Thrones",2)
        b.add_book("Narnia", 1)
        assert b.num_books_read() == 4, 'num_books not working properly'

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3. 
        # Your test should check that the returned books have rating  > 3
        b = BookLover('Person', 'person@gmail.com', 'Fantasy')
        b.add_book("Harry Potter", 5)
        b.add_book("Lord of the Rings", 4)
        b.add_book("Game of Thrones",2)
        b.add_book("Narnia", 1)
        fav = b.fav_books()
        fav_ratings = fav['book_rating']
        assert all(r > 3 for r in fav_ratings)
        
                
if __name__ == '__main__':
    
    unittest.main(verbosity=3)