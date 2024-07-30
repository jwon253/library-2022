from PIL import Image, ImageTk
import textwrap

class Data:
    def __init__(self, book_title, book_author, book_cover, book_genre, book_blurb):
        '''Stores data in a list'''
        self.title = book_title
        self.author = book_author
        self.cover = book_cover
        self.genre = book_genre
        self.blurb = book_blurb

        self.image = Image.open(self.cover)
        self.resize_image = self.image.resize((125,185))
        self.img = ImageTk.PhotoImage(self.resize_image)

        self.paragraph = textwrap.fill(self.blurb,70)