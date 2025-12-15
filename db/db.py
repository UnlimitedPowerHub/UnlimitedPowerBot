import json
import secrets
import string

utf_8 = "utf-8"


class DB:

    def __init__(self, db_name=str):
        self.db_file = f"data/{db_name}.json"

    def load(self):
        with open(self.db_file, 'r', encoding=utf_8) as file:
            return json.load(file)

    def save(self, data):
        with open(self.db_file, 'w', encoding=utf_8) as file:
            json.dump(data, file, indent=4)

    def get_all(self):
        """
        input: Nothing

        output: all data of database
        """
        return DB.load(self)

    def exist(self, a):
        """
        input: key

        output: True if key is exist in database else False
        """
        return bool(str(a) in DB.get_all(self))

    def set_key(self, a, b):
        """
        input: key & value

        output: void
        """
        db_data = DB.load(self)
        db_data[str(a)] = b
        DB.save(self, db_data)

    def get_key(self, a):
        """
        input: key

        output: goal key value
        """
        return DB.load(self)[str(a)]

    def remove_key(self, a):
        """
        input: Key

        output: void
        """
        db_data = DB.load(self)
        del db_data[str(a)]
        DB.save(self, db_data)

    def get_nested(self, a):
        """
        input: key or key address

        output: your goal key or key address
        """
        db_data = DB.load(self)
        goal = []
        m = 0
        for key in a:
            if m == 0:
                goal = db_data[str(key)]
            else:
                goal = goal[key]
            m += 1
        return goal

    def set_nested(self, a, b):
        """
        input: key or key address & value

        key address must be like: ['key1',key2]

        for example data we have and we want set it

        we_db = { "key1": { "key2":"value" } }

        we_db = DB('json')
        we_db.setNested(we_db class,['key1','key2'],"Reza")

        result: { "key1": { "key2":"Reza" } }

        output: void
        """

        db_data = DB.load(self)
        goal = db_data
        m = 0
        for key in a:
            if m == len(a) - 1:
                goal[key] = b
            else:
                if key not in goal:
                    goal[key] = {}
                goal = goal[key]
            m += 1
        DB.save(self, db_data)

    def remove_nested(self, a):
        """
        input: Key or Key address

        key address must be like: ['key1','key2']

        example data we have & we want to remove a key in it:

        we_db = { "key1": { "key2":"value" } }

        we_db = DB('json')
        we_db.removeNested(we_db class,['key1','key2'])

        result: { "key1": {} }

        output: void
        """
        db_data = DB.load(self)
        goal = db_data
        m = 0
        for key in a:
            if m == len(a) - 1:
                del goal[key]
            else:
                if key not in goal:
                    goal[key] = {}
                goal = goal[key]
            m += 1
        DB.save(self, db_data)

    @staticmethod
    def generate_id():
        """
        input: DB class

        output: randon id
        """
        a = string.ascii_lowercase + string.digits
        b = "".join(secrets.choice(a) for _ in range(35))
        return f"0c_{b}"

# Add SQLite In Another Updates

# import sqlite lib
# import sqlite3

# open connection
# conn = sqlite3.connect('db.db')
# c = conn.cursor()

# create database if not exists
# c.execute("CREATE TABLE IF NOT EXISTS carts(id INTEGER PRIMARY KEY,name TEXT,url TEXT)")

# add data to database
# c.execute("INSERT INTO carts(id,name,url) VALUES (?,?,?)",(1,'Amirreza','https://i.com/'))
# conn.commit()

# remove data in database
# c.execute("DELETE FROM user WHERE age = ?",(17,))
# conn.commit()

# update data in database
# c.execute("UPDATE user SET age = ? WHERE name = ?",(17,'Mamad',))
# conn.commit()

# get all
# c.execute('SELECT * FROM carts')
# rows = c.fetchall()
# for row in rows:
#     print(row)

# get carts where cart name = Amirreza
# c.execute("SELECT * FROM carts WHERE name = ?",("Amirreza",))
# print(c.fetchall())

# close connection
# conn.close()
