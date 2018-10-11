from tkinter import *
import pymysql

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        """
        This function create the GUI
        for entering DB, Password and
        Query and also makes a panel
        for showing output
        """

        #Database entry panel
        Label(self, text = "DB Name:").grid(row = 0, column = 0, sticky = W)
        self.db_entry = Entry(self, width = 40)
        self.db_entry.grid(row = 0, column = 1, sticky = W)

        #Password entry panel
        Label(self, text = "Password:").grid(row = 1, column = 0, sticky = W)
        self.pass_entry = Entry(self, show = '*', width = 40)
        self.pass_entry.grid(row = 1, column = 1, sticky = W)

        #Query entry
        Label(self, text = "Your Query:").grid(row = 2, column = 0, sticky = W)
        self.query_entry = Entry(self, width = 40)
        self.query_entry.grid(row = 2, column = 1, sticky = W)

        #Creating a Submit Button
        self.sub_button = Button(self, text = "Submit", command = self.run_app,
                                                        width = 40, height = 1)
        self.sub_button.grid(row = 3, column = 1, sticky = W, columnspan = 9)

        #Output panel
        self.text = Text(self, width = 60, height = 25, wrap = WORD)
        self.text.grid(row = 4, column = 0, columnspan = 4)

    def run_app(self):

        """
        This function takes the data from previous function
        and check the password is valid or not.
        If pass is valid then fetch the data from database
        and show it.
        """

        self.host = 'localhost'
        self.user = 'root'
        self.db = str(self.db_entry.get())
        self.password = str(self.pass_entry.get())
        query = str(self.query_entry.get())

        if self.password == "852963":
            self.connection = pymysql.connect(self.host,
                                              self.user,
                                              self.password,
                                              self.db)
            self.cursor = self.connection.cursor()

            try:
                cursor = self.connection.cursor(pymysql.cursors.DictCursor)
                cursor.execute(query)

                ans = cursor.fetchall()
                print_ans = "{0}".format(ans)
                self.text.delete(0.0, END)
                self.text.insert(0.0, print_ans)
            except:
                self.connection.rollback()
                print_ans = "Query not match"
                self.text.delete(0.0, END)
                self.text.insert(0.0, print_ans)

        else:
            print_ans = "Wrong Password"
            self.text.delete(0.0, END)
            self.text.insert(0.0, print_ans)
            

def main():
    Application.create_widgets()
    Application.run_app()

if __name__ == '__main__':
    main()