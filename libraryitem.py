from abc import ABC, abstractmethod

class LibraryItem(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    @property
    def is_checked_out(self):
        return self._is_checked_out

    @is_checked_out.setter
    def is_checked_out(self, value):
        if not isinstance(value, bool):
            raise ValueError("is_checked_out must be True or False")
        self._is_checked_out = value

    @abstractmethod
    def check_out(self):
        pass

    def return_item(self):
        self.is_checked_out = False
        print(f"'{self.title}' has been returned.")


class Book(LibraryItem):
    def check_out(self):
        if self.is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self.is_checked_out = True
            print(f"'{self.title}' checked out.")


class EBook(LibraryItem):
    def check_out(self):
        print(f"'{self.title}' checked out (unlimited digital copies available).")


class AudioBook(LibraryItem):
    def __init__(self, title, author, duration_minutes):
        super().__init__(title, author)
        self.duration_minutes = duration_minutes

    def check_out(self):
        if self.is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self.is_checked_out = True
            print(f"'{self.title}' checked out — you have it for {self.duration_minutes} minutes.")


book = Book("Atomic Habits", "James Clear")
book.check_out()
book.check_out()   # should refuse

ebook = EBook("Deep Work", "Cal Newport")
ebook.check_out()
ebook.check_out()   # should succeed anyway
ebook.check_out()   # should succeed anyway

audiobook = AudioBook("Dune", "Frank Herbert", 320)
audiobook.check_out()
audiobook.check_out()   # should refuse