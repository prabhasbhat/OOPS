class Book:
    def __init__(self, title, author, ISBN, description, available_copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.description = description
        self.available_copies = available_copies

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.ISBN}\nDescription: {self.description}\nAvailable Copies: {self.available_copies}"


class Journal:
    def __init__(self, title, editor, ISSN, description, available_copies):
        self.title = title
        self.editor = editor
        self.ISSN = ISSN
        self.description = description
        self.available_copies = available_copies

    def display_info(self):
        return f"Title: {self.title}\nEditor: {self.editor}\nISSN: {self.ISSN}\nDescription: {self.description}\nAvailable Copies: {self.available_copies}"


class Magazine:
    def __init__(self, title, editor, ISSN, description, available_copies):
        self.title = title
        self.editor = editor
        self.ISSN = ISSN
        self.description = description
        self.available_copies = available_copies

    def display_info(self):
        return f"Title: {self.title}\nEditor: {self.editor}\nISSN: {self.ISSN}\nDescription: {self.description}\nAvailable Copies: {self.available_copies}"


class ResearchPaper:
    def __init__(self, title, author, publication_date, abstract):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.abstract = abstract

    def display_info(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nPublication Date: {self.publication_date}\nAbstract: {self.abstract}"


class Vendor:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def display_info(self):
        return f"Vendor Name: {self.name}\nAddress: {self.address}\nContact Info: {self.contact_info}"


class Publisher:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info

    def display_info(self):
        return f"Publisher Name: {self.name}\nAddress: {self.address}\nContact Info: {self.contact_info}"

from datetime import datetime, timedelta

class Borrowing:
    def __init__(self, patron, item, due_date):
        self.patron = patron
        self.item = item
        self.due_date = due_date
        self.returned = False

    def return_item(self):
        self.returned = True

    def calculate_penalty(self):
        if not self.returned:
            # Calculate penalty based on due date
            days_overdue = (datetime.now() - self.due_date).days
            if days_overdue > 0:
                return days_overdue * 5  # Assuming $5 per day penalty
        return 0  # No penalty if returned on time


class Issuing:
    def issue_book(self, patron, book):
        if book.available_copies > 0:
            book.available_copies -= 1
            due_date = datetime.now() + timedelta(days=14)  # Assuming a 14-day borrowing period
            borrowing_record = Borrowing(patron, book, due_date)
            return borrowing_record
        else:
            return None  # No available copies

    def issue_journal(self, patron, journal):
        # Similar logic as issuing a book
        if journal.available_copies > 0:
            journal.available_copies -= 1
            due_date = datetime.now() + timedelta(days=7)  # Assuming a 7-day borrowing period for journals
            borrowing_record = Borrowing(patron, journal, due_date)
            return borrowing_record
        else:
            return None  # No available copies

    def issue_magazine(self, patron, magazine):
        # Similar logic as issuing a book
        if magazine.available_copies > 0:
            magazine.available_copies -= 1
            due_date = datetime.now() + timedelta(days=7)  # Assuming a 7-day borrowing period for magazines
            borrowing_record = Borrowing(patron, magazine, due_date)
            return borrowing_record
        else:
            return None  # No available copies


class Returning:
    def return_item(self, borrowing_record):
        borrowing_record.return_item()
        penalty = borrowing_record.calculate_penalty()
        return penalty


class Recommendation:
    def recommend_book(self, patron, book_title, author, description):
        # Create a new book recommendation in the system
        recommended_book = Book(book_title, author, None, description, 0)
        # Additional logic for recording recommendations and notifying library staff

        return recommended_book


class LibraryManagement:
    def add_new_book(self, book):
        # Add a new book to the library catalog
        # Additional logic for catalog management

    def discard_book(self, book):
        # Remove an existing book from the library catalog
        # Additional logic for catalog management

    def search_availability(self, title):
        # Search for the availability of a particular book in the catalog
        # Additional logic for searching and displaying results


class Penalty:
    def impose_penalty(self, patron, amount):
        # Process and record a penalty for a defaulter
        # Additional logic for managing penalties
        
class Search:
    def search_item_by_title(self, catalog, title):
        # Search for an item by title in the catalog
        matching_items = []
        for item in catalog:
            if item.title.lower() == title.lower():
                matching_items.append(item)
        return matching_items

    def search_item_by_author(self, catalog, author):
        # Search for items by author in the catalog
        matching_items = []
        for item in catalog:
            if item.author.lower() == author.lower():
                matching_items.append(item)
        return matching_items

    def search_available_items(self, catalog):
        # Search for available items in the catalog
        available_items = []
        for item in catalog:
            if item.available_copies > 0:
                available_items.append(item)
        return available_items

class Reporting:
    def report_issue(self, student, issue_description):
        # Functionality for a student to report an issue to the admin
        admin_email = "admin@example.com"  # Replace with actual admin contact
        # Send an email or create a support ticket with the issue description
        # Additional logic for notifying the admin
        return f"Issue reported to admin. You will be contacted at {admin_email}."
class StudentBoundary:
    def __init__(self, library_system):
        self.library_system = library_system
        self.borrowing = Borrowing()
        self.search = Search()
        self.reporting = Reporting()

    def borrow_book(self, student, book_title):
        return self.borrowing.borrow_book(student, book_title)

    def return_book(self, student, book_title):
        return self.borrowing.return_book(student, book_title)

    def search_availability(self, title):
        return self.search.search_item_by_title(self.library_system.catalog, title)

    def report_issue(self, student, issue_description):
        return self.reporting.report_issue(student, issue_description)


class Borrowing:
    def __init__(self, patron, item, due_date):
        self.patron = patron
        self.item = item
        self.due_date = due_date
        self.returned = False

    def return_item(self):
        self.returned = True

    def calculate_penalty(self):
        if not self.returned:
            # Calculate penalty based on due date
            days_overdue = (datetime.now() - self.due_date).days
            if days_overdue > 0:
                return days_overdue * 5  # Assuming $5 per day penalty
        return 0  # No penalty if returned on time

class Returning:
    def return_item(self, borrowing_record):
        borrowing_record.return_item()
        penalty = borrowing_record.calculate_penalty()
        return penalty

class Search:
    def search_item_by_title(self, catalog, title):
        # Search for an item by title in the catalog
        matching_items = []
        for item in catalog:
            if item.title.lower() == title.lower():
                matching_items.append(item)
        return matching_items

    def search_item_by_author(self, catalog, author):
        # Search for items by author in the catalog
        matching_items = []
        for item in catalog:
            if item.author.lower() == author.lower():
                matching_items.append(item)
        return matching_items

    def search_available_items(self, catalog):
        # Search for available items in the catalog
        available_items = []
        for item in catalog:
            if item.available_copies > 0:
                available_items.append(item)
        return available_items

class Reporting:
    def report_issue(self, student, issue_description):
        # Functionality for a student to report an issue to the admin
        admin_email = "admin@example.com"  # Replace with actual admin contact
        # Send an email or create a support ticket with the issue description
        # Additional logic for notifying the admin
        return f"Issue reported to admin. You will be contacted at {admin_email}."

class BoundaryFaculty:
    def __init__(self, library_system):
        self.library_system = library_system

    def search_availability(self, title):
        # Functionality for a faculty member to search for the availability of a book
        available_books = self.library_system.search_availability(title)
        return available_books

    def recommend_book(self, faculty, book_title, author, description):
        # Functionality for a faculty member to recommend a new book to the library
        recommended_book = self.library_system.recommend_book(faculty, book_title, author, description)
        return f"Book '{recommended_book.title}' has been recommended to the library."

    def borrow_book(self, faculty, book_title):
        # Functionality for a faculty member to borrow a book
        book = self.library_system.search_item_by_title(book_title)
        if book:
            borrowing_record = faculty.borrow_book(book)
            if borrowing_record:
                return f"Successfully borrowed '{book_title}' with due date {borrowing_record.due_date}."
            else:
                return "No available copies of the book."
        else:
            return "Book not found in the catalog."

    def return_book(self, faculty, book_title):
        # Functionality for a faculty member to return a book
        book = self.library_system.search_item_by_title(book_title)
        if book:
            penalty = faculty.return_book(book)
            if penalty > 0:
                return f"Book '{book_title}' returned with a penalty of ${penalty}."
            else:
                return f"Book '{book_title}' returned successfully."

    def report_issue(self, faculty, issue_description):
        # Functionality for a faculty member to report an issue to the admin
        admin_email = "admin@example.com"  # Replace with actual admin contact
        # Send an email or create a support ticket with the issue description
        # Additional logic for notifying the admin
        return f"Issue reported to admin. You will be contacted at {admin_email}."

class BoundaryLibraryStaff:
    def __init__(self, library_system):
        self.library_system = library_system

    def search_availability(self, title):
        # Functionality for a library staff member to search for the availability of a book
        available_books = self.library_system.search_availability(title)
        return available_books

    def issue_book(self, student_faculty, book_title):
        # Functionality for a library staff member to issue a book to a student or faculty
        book = self.library_system.search_item_by_title(book_title)
        if book:
            borrowing_record = student_faculty.borrow_book(book)
            if borrowing_record:
                return f"Successfully issued '{book_title}' to {student_faculty.name} with due date {borrowing_record.due_date}."
            else:
                return "No available copies of the book."
        else:
            return "Book not found in the catalog."

    def collect_book(self, student_faculty, book_title):
        # Functionality for a library staff member to collect a book returned by a student or faculty
        book = self.library_system.search_item_by_title(book_title)
        if book:
            penalty = student_faculty.return_book(book)
            if penalty > 0:
                return f"Book '{book_title}' collected with a penalty of ${penalty}."
            else:
                return f"Book '{book_title}' collected successfully."
        else:
            return "Book not found in the catalog."

    def receive_recommendations(self):
        # Functionality for a library staff member to receive book recommendations from students/faculty
        recommendations = self.library_system.receive_recommendations()
        return recommendations

    def add_book(self, book):
        # Functionality for a library staff member to add a new book to the LMS
        self.library_system.add_new_book(book)
        return f"Book '{book.title}' has been added to the library."

    def remove_book(self, book_title):
        # Functionality for a library staff member to remove a book from the LMS
        removed_book = self.library_system.remove_book(book_title)
        if removed_book:
            return f"Book '{book_title}' has been removed from the library."
        else:
            return "Book not found in the catalog."

    def penalize_defaulter(self, student_faculty):
        # Functionality for a library staff member to penalize defaulters
        penalty = student_faculty.calculate_penalty()
        if penalty > 0:
            return f"{student_faculty.name} has been penalized with a fine of ${penalty}."
        else:
            return f"{student_faculty.name} is not a defaulter."

    def report_issue(self, issue_description):
        # Functionality for a library staff member to report an issue to the admin
        admin_email = "admin@example.com"  # Replace with actual admin contact
        # Send an email or create a support ticket with the issue description
        # Additional logic for notifying the admin
        return f"Issue reported to admin. You will be contacted at {admin_email}."
class BoundaryLibraryAdmin:
    def __init__(self, library_system):
        self.library_system = library_system

    def monitor_dashboard(self):
        # Functionality for the administrator to monitor the overall status of the library
        dashboard_data = self.library_system.monitor_dashboard()
        return dashboard_data

    def search_availability(self, title):
        # Functionality for the administrator to search for the availability of a book
        available_books = self.library_system.search_availability(title)
        return available_books

    def add_book(self, book):
        # Functionality for the administrator to add a new book to the LMS
        self.library_system.add_new_book(book)
        return f"Book '{book.title}' has been added to the library."

    def remove_book(self, book_title):
        # Functionality for the administrator to remove a book from the LMS
        removed_book = self.library_system.remove_book(book_title)
        if removed_book:
            return f"Book '{book_title}' has been removed from the library."
        else:
            return "Book not found in the catalog."

    def receive_issues(self):
        # Functionality for the administrator to receive all the issues reported by students, faculty, and library staff
        issues = self.library_system.receive_issues()
        return issues

    def library_analytics(self):
        # Functionality for the administrator to view various analytics of the library
        analytics_data = self.library_system.library_analytics()
        return analytics_data

class BoundaryLibrary:
    def __init__(self):
        self.books = []
        self.students = []
        self.faculty = []
        self.library_staff = []
        self.issues = []
        self.vendors = []
        self.publishers = []
        # Other initialization for the library system

    # Define methods for various library operations
