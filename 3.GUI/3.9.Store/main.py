import sqlite3

class Store:
    def show_menu(self):
        print(" 1️⃣  Show List")
        print(" 2️⃣  Add")
        print(" 3️⃣  Remove")
        print(" 4️⃣  Edit")
        print(" 5️⃣  Search")
        print(" 6️⃣  Exit")

    def load_database(self):
        global connection, my_cur
        connection = sqlite3.connect("media.db")
        my_cur = connection.cursor()        
        
    def user_input(self):
        self.type = input("what genre of movie do you want to add: ")
        self.name = input("Enter the name of movie: ")
        self.director = input("Enter the name of director:  ")
        self.imdb_score = input("Enter imdb SCORE:  ")
        self.url = input("Enter url for download:  ")
        self.duration = input("Enter duration in minutes:  ")
        self.casts = input("Enter casts:  ")

    def show_list(self):
        for media in my_cur.execute("SELECT * FROM medias"):
            print(media) 
       
    def add(self):
        self.user_input()
        my_cur.execute(f"INSERT INTO medias(type, name, director, imdb_score, url, duration, casts)"
                    f"VALUES('{self.type}','{self.name}','{self.director}','{self.imdb_score}','{self.url}','{self.duration}','{self.casts}')")
        connection.commit()
        print("successfully added.")

    def edit(self):
        id = input("Enter movie id  ")
        self.user_input()
        my_cur.execute(f"UPDATE medias SET type='{self.type}', name='{self.name}', director='{self.director}', imdb_score='{self.imdb_score}',"
                    f"url='{self.url}', duration='{self.duration}', casts='{self.casts}' WHERE id={id}")
        connection.commit()
        print("successfully edited.")
        self.show_list()

    def remove(self):
        id = input("Enter movie id  ")
        my_cur.execute(f"DELETE FROM medias WHERE id='{id}'")
        connection.commit()
        print("successfully deleted.")
        self.show_list()

    def search(self):
        t1 = input("Enter minimum duration of movie ")
        t2 = input("Enter maximum duration of movie ")
        result = my_cur.execute(f"SELECT * FROM medias WHERE duration>'{t1}' and duration<'{t2}'")
        medias = result.fetchall()
        for media in medias:
            print(media)

store = Store()
store.load_database()

while True:
    print('WELCOME TO MOVIE STORE')
    store.show_menu()
    user_select = int(input('Enter your choice:\n'))

    match user_select:
        case 1:
            store.show_list()
        case 2:
            store.add()
        case 3:
            store.remove()
        case 4:
            store.edit()
        case 5:
            store.search()
        case 6:
            exit(0)