from tkinter import *
from tkinter import ttk
from accounts import Accounts
from data import Data
import os
import Pmw

class Interface:
    def __init__(self, parent):
        '''Creates label, entry, button widgets'''
        
        self.details = []
        self.selected_books =[]
        self.selection = []
        self.historyinfo = 'historyinfo'
        self.user = ''

        #Objects in the blue sidebar
        self.blue_sidebar = Frame(parent, bg='#004ba8', padx=30, pady=20)
        self.blue_sidebar.grid(column=0, row=0, sticky=W)
 
        self.grey_sidebar = Frame(parent, bg='#172a3a', padx=30, pady=10)
        self.grey_sidebar.grid(column=0, row=1, sticky=W)
 
        self.library_label = Label(self.blue_sidebar, text='Library', bg='#004ba8', fg='#ffffff', font='roboto')
        self.library_label.grid(column=0, row=0)
 
        self.blue_label = Frame(self.blue_sidebar, bg='#004ba8')
        self.blue_label.grid(column=1, row=0)
  
        self.guest_label = Label(self.blue_label, text='Guest', bg='#004ba8', fg='#ffffff')
        self.guest_label.grid(column=1, row=0, padx=(800, 80))
 
        self.button_frame = Frame(self.blue_label, bg='#004ba8')
        self.button_frame.grid(column=2, row=0)

        self.login_btn_ui = Button(self.button_frame, text='Login', command=self.login_ui, fg='#ffffff', bg='#004ba8', borderwidth=0)
        self.login_btn_ui.grid(column=0, row=0, padx=(40,25))

        self.blue_line = ttk.Separator(self.button_frame, orient='vertical')
        self.blue_line.grid(column=1, row=0, ipady=16, padx=(0,25))

        self.signup_btn = Button(self.button_frame, text='Sign up', command=self.create_account_ui, fg='#ffffff', bg='#004ba8', borderwidth=0)
        self.signup_btn.grid(column=2, row=0)

        self.logout_btn = Button(self.blue_label, text='Logout', command=self.logout_ui, fg='#ffffff', bg='#004ba8', borderwidth=0) 

        #Objects in the grey sidebar
        self.search_entry = Entry(self.grey_sidebar, width= 30)
        self.search_entry.grid(column=0, row=0)
 
        self.search_btn = Button(self.grey_sidebar, text='Search', command=self.main_search_books, borderwidth=0)
        self.search_btn.grid(column=1, row=0, padx=(0,565))

        self.grey_label = Frame(self.grey_sidebar, bg='#172a3a') 
        self.grey_label.grid(column=2, row=0)
 
        self.home_btn = Button(self.grey_label, text='Home', command=lambda:self.switch_page_user(self.home_page, self.home_btn, self.home_page), width=15, pady=5, fg='#172a3a', bg='#34e5ff', borderwidth=0)
        self.home_btn.grid(column = 1, row=0)
 
        self.grey_line1 = ttk.Separator(self.grey_label, orient='vertical')
        self.grey_line1.grid(column=2, row=0, ipady=16, padx=(8,8))

        self.viewmore_btn = Button(self.grey_label, text='View More', command=lambda:self.switch_page_user(self.viewmore_page_outer, self.viewmore_btn, self.viewmore_page), width=15, pady=5, fg='#ffffff', bg='#172a3a', borderwidth=0)
        self.viewmore_btn.grid(column=3, row=0, padx=(0,0))
 
        self.grey_line2 = ttk.Separator(self.grey_label, orient='vertical')
        self.grey_line2.grid(column=4, row=0, ipady=16, padx=(8,8))
 
        self.bookmarks_btn = Button(self.grey_label, text='Bookmarks', command=lambda:self.switch_page_user(self.bookmark_page, self.bookmarks_btn, self.bookmark_page), width=15, pady=5, fg='#ffffff', bg='#172a3a', borderwidth=0)
        self.bookmarks_btn.grid(column=5, row=0)
        self.bookmarks_btn.grid_forget()

        self.bookmarks_btn_placeholder = Label(self.grey_label, bg='#172a3a', width=18)
        self.bookmarks_btn_placeholder.grid(column=5, row=0)

        self.viewmore_page_outer = Frame(parent, bg='#ffffff')
        self.viewmore_page_outer.grid(column=0, row=3)

        #Home Page
        self.home_page = Frame(parent, bg='#ffffff')
        self.home_page.grid(column=0, row=3, sticky=W)

        self.viewmore_alt_btn_top = Button(self.home_page, text='View more', command=lambda:self.switch_page_user(self.viewmore_page_outer, None, self.viewmore_page), bg='#ffffff', borderwidth=0)
        self.viewmore_alt_btn_top.grid(column=5, row=0, sticky=E, padx=(0,30))

        self.viewmore_alt_btn_bot = Button(self.home_page, text='View more', command=lambda:self.switch_page_user(self.viewmore_page_outer, None, self.viewmore_page), bg='#ffffff', borderwidth=0)
        self.viewmore_alt_btn_bot.grid(column=5, row=2, sticky=E, padx=(0,30))

        self.new_book_text = Label(self.home_page, text='New Books', bg='#ffffff')
        self.new_book_text.grid(column=0, row=0, sticky=W, padx=(30,0), pady=(5,0))

        self.popular_books = Label(self.home_page, text='Popular Books', bg='#ffffff')
        self.popular_books.grid(column=0, row=2, sticky=W, padx=(30,0))

        #View more page
        self.viewmore_page = Frame(self.viewmore_page_outer, bg='#ffffff')
        self.viewmore_page.grid(column=0, row=1, sticky=W)

        self.categories = Frame(self.viewmore_page_outer, bg='#d1faff', padx=30, pady=10)
        self.categories.grid(column=0, row=0, sticky=W)

        self.categories_label = Frame(self.categories, bg='#d1faff')
        self.categories_label.grid(column=1, row=0)

        self.categories_text = Label(self.categories, text='Categories', fg='#172a3a', bg='#d1faff')
        self.categories_text.grid(column=0, row=0, padx=(0,380))

        self.science = Button(self.categories_label, text='Science', command= lambda:self.book_categories('SCIENCE'), fg='#172a3a', bg='#d1faff', borderwidth=0)
        self.science.grid(column=0, row=0, padx=50)

        self.education = Button(self.categories_label, text='Education', command= lambda:self.book_categories('EDUCATION'), fg='#172a3a', bg='#d1faff', borderwidth=0)
        self.education.grid(column=1, row=0, padx=50)

        self.fantasy = Button(self.categories_label, text='Fantasy', command= lambda:self.book_categories('FANTASY'), fg='#172a3a', bg='#d1faff', borderwidth=0)
        self.fantasy.grid(column=2,row=0, padx=50)

        self.art = Button(self.categories_label, text='Art', command= lambda:self.book_categories('ART'), fg='#172a3a', bg='#d1faff', borderwidth=0)
        self.art.grid(column=3, row=0, padx=50)

        self.mystery = Button(self.categories_label, text='Mystery', command= lambda:self.book_categories('MYSTERY'), fg='#172a3a', bg='#d1faff', borderwidth=0)
        self.mystery.grid(column=4, row=0, padx=50)

        self.viewmore_page_outer.grid_forget()

        #Bookmarks Page
        self.bookmark_page = Frame(parent, bg='#ffffff')
        self.bookmark_page.grid(column=0, row=3, sticky=W)
        self.bookmark_page.grid_forget()

        # Read from external file
        info_file = open('books.txt')
        self.info_list = info_file.readlines()
        self.show_books()
        self.book_placement(self.home_page, self.details)

        #Create Account UI
        self.create_acc_frame = Frame(parent, padx=20, pady=20, bg='#ffffff', highlightbackground='#172a3a', highlightthickness=1)
        self.create_acc_frame.grid(columnspan=1, rowspan=3)

        self.create_acc_label = Label(self.create_acc_frame, text='Create Account', bg='#ffffff', font=40)
        self.create_acc_label.grid(column=0, row=0)

        self.username_label = Label(self.create_acc_frame, text='Username', bg='#ffffff')
        self.username_label.grid(column=0, row=1, sticky=W, pady=(10,0))

        self.username_entry = StringVar()
        self.username_entry = Entry(self.create_acc_frame, highlightthickness=1, width=25)
        self.username_entry.grid(column=0, row=2)    
        self.username_entry.config(highlightbackground='#172a3a', highlightcolor='#172a3a')

        self.username_invalid = Label(self.create_acc_frame, text='Invalid Username', fg='#fd151b', bg='#ffffff')
        self.username_invalid.grid_forget()

        self.password_label = Label(self.create_acc_frame, text='Password', bg='#ffffff')
        self.password_label.grid(column=0, row=4, sticky=W, pady=(10,0))

        self.password_entry = Entry(self.create_acc_frame, highlightthickness=1, width=25)
        self.password_entry.grid(column=0, row=5)
        self.password_entry.config(highlightbackground='#172a3a', highlightcolor='#172a3a')

        self.password_invalid = Label(self.create_acc_frame, text='Invalid Password', fg='#fd151b', bg='#ffffff')
        self.password_invalid.grid_forget()

        self.password_requirement = Label(self.create_acc_frame, text='Password Requires a Number, Symbol, Uppercase', bg='#ffffff', wraplength=200, borderwidth=1, relief="solid") 
        self.password_requirement.grid(column=0, row=7, pady=25)
        self.password_requirement.config(highlightbackground='#172a3a', highlightcolor='#172a3a')

        self.create_btn = Button(self.create_acc_frame, text='Create', command=self.create_account, bg='#3bc14a', fg='#ffffff', borderwidth=0)
        self.create_btn.grid(column=0, row=8, ipadx=15, ipady=5, padx=(0,90))

        self.exit_btn = Button(self.create_acc_frame, text='Exit', command=self.exit, bg='#fd151b', fg='#ffffff', borderwidth=0)
        self.exit_btn.grid(column=0, row=8, ipadx=15, ipady=5, padx=(90,0))
        self.create_acc_frame.grid_forget()

        #Login UI
        self.login_frame = Frame(parent, padx=20, pady=20, bg='#ffffff', highlightbackground='#172a3a', highlightthickness=1)
        self.login_frame.grid(columnspan=1, rowspan=3)

        self.login_label = Label(self.login_frame, text='Login', bg='#ffffff', font=40)
        self.login_label.grid(column=0, row=0)
        
        self.username_label = Label(self.login_frame, text='Username', bg='#ffffff')
        self.username_label.grid(column=0, row=1, sticky=W, pady=(10,0))

        self.username_entry_login = StringVar()
        self.username_entry_login = Entry(self.login_frame, highlightthickness=1, width=25)
        self.username_entry_login.grid(column=0, row=2)    
        self.username_entry_login.config(highlightbackground='#172a3a', highlightcolor= '#172a3a')

        self.username_invalid_login = Label(self.login_frame, text='Invalid Username', fg='#fd151b', bg='#ffffff') 
        self.username_invalid_login.grid_forget()

        self.password_label = Label(self.login_frame, text='Password', bg='#ffffff')
        self.password_label.grid(column=0, row=4, sticky=W, pady=(10,0))
    
        self.password_entry_login = StringVar()
        self.password_entry_login = Entry(self.login_frame, show='*', highlightthickness=1, width=25)
        self.password_entry_login.grid(column=0, row=5, pady=(0,25))
        self.password_entry_login.config(highlightbackground='#172a3a', highlightcolor='#172a3a')

        self.password_invalid_login = Label(self.login_frame, text='Invalid Password', fg='#fd151b', bg='#ffffff')
        self.password_invalid_login.grid_forget()

        self.login_btn = Button(self.login_frame, text='Login', command=self.login, bg='#3bc14a', fg='#ffffff', borderwidth=0)
        self.login_btn.grid(column=0, row=8, ipadx=15, ipady=5, padx=(0,90))
        
        self.exit_btn = Button(self.login_frame, text='Exit', command=self.exit, bg='#fd151b', fg='#ffffff', borderwidth=0)
        self.exit_btn.grid(column=0, row=8, ipadx=15, ipady=5, padx=(90,0))
        self.login_frame.grid_forget()

        #Logout UI
        self.logout_ui_frame = Frame(parent, padx=20, pady=20, bg='#ffffff', highlightbackground='#172a3a', highlightthickness=1)
        self.logout_ui_frame.grid(columnspan=1, rowspan=3)

        self.logout_label = Label(self.logout_ui_frame, text='Logout', bg='#ffffff', font=40)
        self.logout_label.grid(column=0, row=0)

        self.logout_text = Label(self.logout_ui_frame, text='Are you sure you want to Logout', bg='#ffffff')
        self.logout_text.grid(column=0, row=1, pady=(30,30))

        self.confirm_btn = Button(self.logout_ui_frame, text='Confirm', command=self.confirm_logout, bg='#3bc14a', fg='#ffffff', borderwidth=0)
        self.confirm_btn.grid(column=0, row=2, ipadx=15, ipady=5, padx=(0,90))

        self.cancel_btn = Button(self.logout_ui_frame, text='Cancel', command=self.cancel_logout, bg='#fd151b', fg='#ffffff', borderwidth=0)
        self.cancel_btn.grid(column=0, row=2, ipadx=15, ipady=5, padx=(90,0))
        self.logout_ui_frame.grid_forget()

        #Admin UI
        self.grey_label_admin = Frame(self.grey_sidebar, bg='#172a3a')
        self.grey_label_admin.grid(column=2, row=0, sticky=NE)

        self.returns_issues_btn = Button(self.grey_label_admin, text='Returns & Issues', command=lambda:self.switch_page_admin(self.return_issue_page, self.returns_issues_btn), width=13, pady=5, fg='#ffffff', bg='#172a3a', borderwidth=0)
        self.returns_issues_btn.grid(column=1, row=0, padx=(50,0))

        self.grey_line1 = ttk.Separator(self.grey_label_admin, orient='vertical')
        self.grey_line1.grid(column=2, row=0, ipady=16, padx=(8,8))

        self.history_btn = Button(self.grey_label_admin, text='History', command=lambda:self.switch_page_admin(self.history_page, self.history_btn), width=13, pady=5, fg='#ffffff', bg='#172a3a', borderwidth=0)
        self.history_btn.grid(column=3, row=0)

        self.grey_line2 = ttk.Separator(self.grey_label_admin, orient='vertical')
        self.grey_line2.grid(column=4, row=0, ipady=16, padx=(8,8))
 
        self.viewmore_btn_admin = Button(self.grey_label_admin, text='View More', command=lambda:self.switch_page_admin(self.viewmore_page_outer, self.viewmore_btn_admin), width=13, pady=5, fg='#ffffff', bg='#172a3a', borderwidth=0)
        self.viewmore_btn_admin.grid(column= 5,row=0, padx=(0,0))
        self.grey_label_admin.grid_forget()

        #Returns & Issues
        self.return_issue_page = Frame(parent, bg='#ffffff')
        
        self.search_user_frame = Frame(self.return_issue_page)
        self.search_user_frame.grid(column=0, row=0, pady=(30,30), sticky=W)

        self.search_user_entry = Entry(self.search_user_frame, width=100, highlightbackground='#172a3a', highlightthickness=1)
        self.search_user_entry.grid(column=0, row=0)
 
        self.search_user_btn = Button(self.search_user_frame, text='Search', command=self.search_user, borderwidth=0)
        self.search_user_btn.grid(column=1, row=0)

        self.check_user = Label(self.search_user_frame, text='Invalid User', fg='#fd151b', bg='#ffffff')

        self.issue_frame = Frame(self.return_issue_page, bg='#ffffff', highlightbackground='#172a3a', highlightthickness=1)
        self.issue_frame.grid(column=0, row=1)
 
        self.search_frame = Frame(self.issue_frame, bg='#004ba8', pady=10, padx=20)
        self.search_frame.grid(row=0, ipadx=358, sticky=W)
 
        self.search_book_entry = Entry(self.search_frame, width=50, highlightbackground='#172a3a', highlightthickness=1)
        self.search_book_entry.grid(column=0, row=0, sticky=W)
 
        self.search_book_btn = Button(self.search_frame, text='Search', command=self.search_book, borderwidth=0)
        self.search_book_btn.grid(column=1, row=0)

        self.issue_list = ttk.Treeview(self.issue_frame, height=8)
        self.issue_list['columns']=('books')
        self.issue_list.column('#0', width=0, minwidth=0)
        self.issue_list.column('books', width=1100, anchor=W)
        self.issue_list.heading('books', text='Book', anchor=W)
        self.issue_list.grid(column=0, row=2)
 
        self.issue_btn = Button(self.issue_frame, text='Issue', command=self.issue_book, bg='#7cea9c', width=10, borderwidth=0)
        self.issue_btn.grid(column=0, row=3, sticky=E, padx=(0,50), pady=10)
 
        self.return_frame = Frame(self.return_issue_page, bg='#ffffff', highlightbackground='#172a3a', highlightthickness=1)
        self.return_frame.grid(column=0, row=2, pady=(20,0))
 
        self.return_list = ttk.Treeview(self.return_frame, height=8)
        self.return_list['columns']=('books')
        self.return_list.column('#0', width=0, minwidth=0)
        self.return_list.column('books', width=1100, anchor=W)
        self.return_list.heading('books', text='Book', anchor=W)
        self.return_list.grid(column=0, row=0)
 
        self.return_btn = Button(self.return_frame, text='Return', command=self.return_book, bg='#7cea9c', width=10, borderwidth=0)
        self.return_btn.grid(column=0, row=1, sticky=E, padx=(0,50), pady=10)
        self.return_issue_page.grid_forget()

        #History
        self.history_page = Frame(parent, bg='#ffffff')
 
        self.history_list = ttk.Treeview(self.history_page, height=27)
        self.history_list['columns']=('user','book','status')
        self.history_list.column('#0', width=0, minwidth=0)
        self.history_list.column('user', anchor=W, width=300)
        self.history_list.column('book', anchor=W, width=500)
        self.history_list.column('status', anchor=W, width=300)
 
        self.history_list.heading('user', text='User', anchor=W)
        self.history_list.heading('book', text='Book', anchor=W)
        self.history_list.heading('status', text='Status', anchor=W)
        self.history_list.grid(column=0, row=0, pady=(30,0))
        self.history_page.grid_forget()

        for self.amount in range(len(self.details)): 
            self.selection.append(self.details[self.amount].title)

        file = open(self.historyinfo, 'r')
        info = file.read().splitlines()
        for line in info:
            items = line.split(',')
            self.history_list.insert(parent='', index='end', values=(items[0], items[1],))

        self.pagetype = self.home_page
        self.return_error = Label(self.return_frame, text='Search User', fg='#fd151b', bg='#ffffff')
        self.issue_error = Label(self.issue_frame, text='Search User', fg='#fd151b', bg='#ffffff')
        self.redlabel = Label(self.create_acc_frame, text='User Already Exist', fg='#fd151b', bg='#ffffff')

        self.user_files = os.listdir()  

    def show_books(self):
        for line in self.info_list:
            items = line.split('#')
            add_books = Data(items[0], items[1], items[2], items[3], items[4])
            self.details.append(add_books)

    def main_search_books(self):
        '''Displays books with common letters'''
        for books in self.selected_books:
            books.destroy()  
        self.details = []
        target = self.search_entry.get()
        self.search_entry.delete(0, END)
        self.button_change()
        label = self.guest_label.cget('text')        
        if label == 'Admin':
            self.viewmore_btn_admin.configure(fg='#172a3a', bg='#34e5ff')
        else:
            self.viewmore_btn.configure(fg='#172a3a', bg='#34e5ff')
        self.clear()
        self.viewmore_page_outer.grid()
        
        for line in self.info_list:
            if line[0:len(target)].lower() == target.lower():
                items = line.split('#')
                search_books = Data(items[0], items[1], items[2], items[3], items[4])
                self.details.append(search_books)
                self.book_placement(self.viewmore_page, self.details)

            else:
                items = line.split('#')
                for item in items:
                    if item[0:len(target)].lower() == target.lower():
                        items = line.split('#')
                        search_add_books = Data(items[0], items[1], items[2], items[3], items[4])
                        self.details.append(search_add_books)
                        self.book_placement(self.viewmore_page, self.details)          

        #Display books
    def book_placement(self, page, books):
        '''Displays books in rows and resizes book image'''
        for self.amount in range(len(books)):
            self.word_count_title = len(self.details[self.amount].title)
            self.word_count_author = len(self.details[self.amount].author)
            
            if self.amount < 6:
                self.book_border = Frame(page, bg='#eaf6ff', padx=8, pady=8)
                self.book_border.grid(column=self.amount, row=1, padx=25, pady=(15,0))
                self.selected_books.append(self.book_border)
                self.display_book()

            elif self.amount < 12:
                self.book_border = Frame(page, bg='#eaf6ff', padx=8, pady=8)
                self.book_border.grid(column=self.amount-6, row=3, padx=25, pady=15)
                self.selected_books.append(self.book_border)
                self.display_book()

            else:
                self.book_border = Frame(page, bg='#eaf6ff', padx=8, pady=8)
                self.book_border.grid(column=self.amount-12, row=4, padx=25, pady=15)
                self.selected_books.append(self.book_border)
                self.display_book()

    def bookmarks(self, book):
        '''Adds bookmarks to users if on user account'''
        repeat = False
        account = self.guest_label.cget('text')
        if account == 'Guest':
            pass
        else:
            file_check = open(account, 'r')
            info = file_check.readlines()
            for line in info:
                if book in line:
                    repeat = True

            if repeat:
                pass
            else:
                file = open(account, 'a')
                file.write(book)
                file.close()

    def search_user(self):
        '''Check if user exist'''
        target = self.search_user_entry.get()
        self.user = target

        for i in self.return_list.get_children():
            self.return_list.delete(i)

        if target in self.user_files:
            file = open(target, 'r')
            issued_books = file.read().splitlines()
            self.check_user.grid_forget()
            self.issue_error.grid_forget()
            self.return_error.grid_forget()
            for books in issued_books:
                if books in self.selection:
                    self.return_list.insert(parent='', index='end', values=(books,))

        else:
            self.check_user.grid(column=2,row=0)

    def search_book(self):
        '''Search for books in issues'''
        self.books = []
        target = self.search_book_entry.get()
        self.search_book_entry.delete(0, END)
        for i in self.issue_list.get_children():
            self.issue_list.delete(i)

        for line in self.info_list:
            if line[0:len(target)].lower() == target.lower():
                items = line.split('#')
                self.issue_list.insert(parent='', index='end', values=(items[0],))

            else:
                items = line.split('#')
                for item in items:
                    if item[0:len(target)].lower() == target.lower():
                        self.issue_list.insert(parent='', index='end', values=(items[0],))

    def book_categories(self, tag):
        '''Displays book with same tag'''
        for books in self.selected_books:
            books.destroy()
        self.details = []
        target = str(tag).upper()
        for line in self.info_list:
            if target in line:
                items = line.split('#')
                searchtags = Data(items[0], items[1], items[2], items[3], items[4])
                self.details.append(searchtags)
                self.book_placement(self.viewmore_page, self.details)

    def issue_book(self):
        '''Select then adds book to user'''
        if self.user == '':
            self.issue_error.grid(column=0,row=2)
        else:
            repeat = False
            selected_item = self.issue_list.focus()
            item_details = self.issue_list.item(selected_item)
            items_change = item_details.get('values')
            item_str = ''.join(items_change)
            
            file_check = open(self.user, 'r')
            info = file_check.readlines()
            for line in info:
                if item_str in line:
                    repeat = True
            if repeat:
                pass
            else:
                user_file = open(self.user, 'a')
                user_file.write(item_str + '\n')
                user_file.close()

            for book in self.history_list.get_children():
                self.history_list.delete(book)
    
            file = open(self.historyinfo, 'a')
            file.write(self.user + ',' + item_str + '\n')
            file.close()
    
            file = open(self.historyinfo, 'r')
            info = file.read().splitlines()
            for line in info:
                items = line.split(',')
                self.history_list.insert(parent='', index='end', values=(items[0], items[1],))

    def return_book(self):
        '''Select book then removes the book from user'''
        if self.user == '':
            self.return_error.grid(column=0,row=0)
        else:
            selected_book = self.return_list.focus()
            item_details = self.return_list.item(selected_book)
            items_change = item_details.get('values')
            item_str = ''.join(items_change)

            book = self.return_list.selection()[0]
            self.return_list.delete(book)

            file = open(self.user, 'r')
            return_books = []
            update = []
            return_books.append(item_str)

            for line in file:
                for book in return_books:
                    if book in line:
                        line = line.replace(book, '')
                update.append(line)
            file.close()
            file = open(self.user, 'w')
            
            for line in update:
                file.write(line)
            file.close()

    def create_account_ui(self):
        '''Loads the Create Account UI'''
        self.home_page.grid_forget()
        self.viewmore_page_outer.grid_forget()
        self.login_frame.grid_forget()
        self.invalid_message()
        self.create_acc_frame.grid()
        self.pagetype.grid()

    def create_account(self):
        check = 0
        username_info = self.username_entry.get()
        password_info = self.password_entry.get()
        create = Accounts(username_info, password_info)
        value = create.create_account_check(check)
        self.username_invalid.grid_forget()
        self.password_invalid.grid_forget()
        self.redlabel.grid_forget()
        if username_info in self.user_files:
            self.redlabel.grid(column=0, row=3)

        if value == 0:
            self.create_acc_frame.grid_forget()

        if value == 3:
            self.password_invalid.grid(column=0, row=6)

        else: 
            self.password_requirement.config(fg='#fd151b')
            self.username_invalid.grid(column=0, row=3)
            self.password_invalid.grid(column=0, row=6)

    def login_ui(self):
        '''Loads the Login UI'''
        self.home_page.grid_forget()
        self.viewmore_page_outer.grid_forget()
        self.create_acc_frame.grid_forget()
        self.invalid_message()
        self.login_frame.grid()
        self.pagetype.grid()

    def login(self):
        '''Check if input is valid'''
        check = 0
        self.username_info = self.username_entry_login.get()
        password_info = self.password_entry_login.get()
        login = Accounts(self.username_info, password_info)
        value = login.login_check(check)
        if value == 8:
            self.username_invalid_login.grid_forget()
            self.password_invalid_login.grid(column=0, row=6)    

        if value == 1:
            self.username_invalid_login.grid_forget()
            self.password_invalid_login.grid(column=0, row=6)    

        if value == 2:
            self.login_process()

        if value == 5:
            self.adminui()
            self.login_process()
        
        if value == 6:
            self.password_invalid_login.grid(column=0, row=6)    
    
        if value == 7:
            self.username_invalid_login.grid(column=0, row=3)
            self.password_invalid_login.grid(column=0, row=6)    

    def login_process(self):
        self.login_frame.grid_forget()
        self.bookmarks_btn.grid(column=5, row=0)
        self.bookmarks_btn_placeholder.grid_forget()
        self.guest_label.config(text=self.username_info)
        self.username_entry_login.delete(0, END)
        self.password_entry_login.delete(0, END)
        self.username_invalid_login.grid_forget()
        self.password_invalid_login.grid_forget()
        self.button_frame.grid_forget()
        self.logout_btn.grid(column=2, row=0, padx=(130,0))

    def logout_ui(self):
        '''Loads the Logout UI'''
        self.clear()
        self.logout_ui_frame.grid()
        self.pagetype.grid()
        # self.pagetype = self.home_page

    def confirm_logout(self):
        '''Goes back to Guest'''
        self.guest_label.config(text='Guest')
        self.button_frame.grid(column=2, row=0)
        self.logout_ui_frame.grid_forget()
        self.logout_btn.grid_forget()
        self.grey_label_admin.grid_forget()
        self.bookmarks_btn_placeholder.grid(column=5, row=0)
        self.clear()
        self.grey_label.grid(column=2, row=0)
        self.button_change()
        self.home_btn.configure(fg='#172a3a', bg='#34e5ff')
        self.username_invalid_login.grid_forget()
        self.password_invalid_login.grid_forget()
        self.details = []
        self.show_books()
        self.book_placement(self.home_page, self.details)
        self.home_page.grid()

    def cancel_logout(self):
        '''Exits out of the Logout UI'''
        self.logout_ui_frame.grid_forget()

    def exit(self):
        '''Exits out of the Create Account UI'''
        self.home_page.grid()
        self.password_requirement.config(fg='#172a3a')
        self.invalid_message()
        self.create_acc_frame.grid_forget()
        self.login_frame.grid_forget()

    def adminui(self):
        '''Goes to admin UI '''
        self.grey_label.grid_forget()
        self.home_page.grid_forget()
        self.clear()
        self.grey_label_admin.grid(column=2, row=0)
        self.returns_issues_btn.configure(fg='#172a3a', bg='#34e5ff')
        self.return_issue_page.grid()

    def display_book(self):
        '''For each book in the list, show book details'''
        self.book_author = Label(self.book_border, bg='#eaf6ff', text=self.details[self.amount].author, wraplength=130)
        spacing = self.book_author.grid(column=0, row=2, sticky=W, pady=(0,15))        
        if self.word_count_title > 20:
            spacing     
        if self.word_count_author > 20:
            spacing 
        if (self.word_count_title +  self.word_count_author) > 42:
            spacing = self.book_author.grid(column=0, row=2, sticky=W, pady=(0,0))   
        else:
            spacing      

        self.book_cover = Button(self.book_border, image=self.details[self.amount].img, command=lambda a=self.amount:self.bookmarks(self.info_list[a]), bg='#34e5ff', height=180, width=120,  borderwidth=0)
        tooltip_1 = Pmw.Balloon(root, label_bg="blue")
        tooltip_1.bind(self.book_cover,'{}\n{}\n{}'.format(self.details[self.amount].title, self.details[self.amount].author, self.details[self.amount].paragraph))
        self.book_cover.grid(column=0, row=0)

        self.book_title = Label(self.book_border, bg='#eaf6ff', text=self.details[self.amount].title, wraplength=130)
        self.book_title.grid(column=0, row=1, sticky=W)
        spacing

    def switch_page_admin(self, page, page_btn):
        '''Switch pages in admin UI'''
        self.clear()
        self.details = []
        if page == self.viewmore_page_outer:
            self.show_books()
            self.book_placement(self.viewmore_page, self.details)

        self.pagetype=page
        page.grid()
        self.returns_issues_btn.configure(fg='#ffffff', bg='#172a3a')
        self.history_btn.configure(fg='#ffffff', bg='#172a3a')
        self.viewmore_btn_admin.configure(fg='#ffffff', bg='#172a3a')
        page_btn.configure(fg='#172a3a',bg='#34e5ff')

    def switch_page_user(self, page, page_btn, book):
        '''Switch pages in user/guest ui'''
        self.clear()
        self.invalid_message()
        self.details = []
        if book == self.bookmark_page:
            label = self.guest_label.cget('text')
            self.details = []
            for books in self.selected_books:
                books.destroy()
            file = open(label, 'r')
            reading = file.readlines()
            for line in reading:
                if line in self.info_list:
                    items = line.split('#')
                    bookmark_books = Data(items[0], items[1], items[2], items[3], items[4])
                    self.details.append(bookmark_books)
                    self.book_placement(self.bookmark_page, self.details)
        else:
            self.show_books()
            self.book_placement(book, self.details)

        self.pagetype=page
        page.grid()
        self.home_btn.configure(fg='#ffffff', bg='#172a3a')
        self.viewmore_btn.configure(fg='#ffffff', bg='#172a3a')
        self.bookmarks_btn.configure(fg='#ffffff', bg='#172a3a')
        page_btn.configure(fg='#172a3a',bg='#34e5ff')

    def clear(self):
        self.home_page.grid_forget()
        self.viewmore_page_outer.grid_forget()
        self.bookmark_page.grid_forget()
        self.return_issue_page.grid_forget()
        self.history_page.grid_forget()
        self.login_frame.grid_forget()
        self.create_acc_frame.grid_forget()
        self.logout_ui_frame.grid_forget()

    def button_change(self):
        self.home_btn.configure(fg='#ffffff', bg='#172a3a')
        self.bookmarks_btn.configure(fg='#ffffff', bg='#172a3a')
        self.viewmore_btn.configure(fg='#ffffff', bg='#172a3a')
        self.viewmore_btn_admin.configure(fg='#ffffff', bg='#172a3a')
        self.returns_issues_btn.configure(fg='#ffffff', bg='#172a3a')
        self.history_btn.configure(fg='#ffffff', bg='#172a3a')

    def invalid_message(self):
        self.password_requirement.config(fg='#172a3a')
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        self.username_entry_login.delete(0, END)
        self.password_entry_login.delete(0, END)
        self.username_invalid.grid_forget()
        self.password_invalid.grid_forget()
        self.username_invalid_login.grid_forget()
        self.password_invalid_login.grid_forget()

#main routine
root = Tk()
Pmw.initialise(root)
root.geometry("1200x750")
root.configure(bg='#ffffff')
root.title('Library')
file = Interface(root)
root.mainloop()