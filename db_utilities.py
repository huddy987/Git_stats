import sqlite3

# Initial setup for DB

# WARNING: Only use this to create a new DB. It may replace a db of
# the same name if it already exists.
def setup_db():
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE repos(id INTEGER PRIMARY KEY, name TEXT,
                       user TEXT, language TEXT, stars INTEGER,
                       contributors INTEGER, forks INTEGER)''')
    db.commit()

# Add data to DB
def add_data(name, user, language, stars, contributors, forks):
    try:
        db = sqlite3.connect('data.db')
        cursor = db.cursor()
        cursor.execute('''INSERT INTO repos(name, user, language, stars, contributors, forks)
                      VALUES(?,?,?,?,?,?)''', (name, user, language, stars, contributors, forks))
        db.commit()
    except Exception as Error:
        print(Error)
        db.rollback()
        raise Error

    finally:
        db.close()

# Read data from the db at a specific user ID
def read_data(user_id):
    try:
        db = sqlite3.connect('data.db')
        cursor = db.cursor()
        cursor.execute('''SELECT name, user, language, stars, contributors, forks FROM repos WHERE id=?''', (user_id,))
        repo = cursor.fetchone() #retrieve the user at user ID

        # Print out all the data at that user_id
        print("Name: " + repo[0])
        print("User: " + repo[1])
        print("language: " + repo[2])
        print("Stars: " + str(repo[3]))
        print("Contrib: " + str(repo[4]))
        print("Forks: " + str(repo[5]))
        print("ID: " + str(user_id))
        print("")
    except Exception as Error:
        print(Error)
        db.rollback()
        raise Error

    finally:
        db.close()

# Read data from the db at the last index
def read_last_insert():
    try:
        db = sqlite3.connect('data.db')
        cursor = db.cursor()
        cursor.execute('''SELECT * FROM repos WHERE ID = (SELECT MAX(ID)  FROM repos);''');
        repo = cursor.fetchone() #retrieve the user at user ID

        # Print out all the data at that user_id
        print("ID: " + str(repo[0]))
        print("Name: " + repo[1])
        print("User: " + repo[2])
        try:
            print("language: " + repo[3])
        except:
            pass
        print("Stars: " + str(repo[4]))
        print("Contrib: " + str(repo[5]))
        print("Forks: " + str(repo[6]))
        print("")
    except Exception as Error:
        print(Error)
        db.rollback()
        raise Error

    finally:
        db.close()

# Checks if the entry already exists
def check_db(name, user):
    db = sqlite3.connect('data.db')
    cursor = db.cursor()
    cursor.execute('''SELECT name, user FROM repos''')
    all_rows = cursor.fetchall()

    for row in all_rows:
        if (row[0] == name) and (row[1] == user):
            db.close()
            return 1
    db.close()
    return 0

# If run from main you can create a new database and table if
# you want to start fresh...
if __name__ == "__main__":
    userin = input("Do you really want to create a new database?")
    if userin:
        setup_db()
