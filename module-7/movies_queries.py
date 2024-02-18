import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    db.close()

db.reconnect()

cursor = db.cursor()

cursor.execute("SELECT studio_ID, studio_name FROM studio")

stu = cursor.fetchall()

print("--DISPLAYING Studio RECORDS--")

for s in stu:
    
    print("Studio ID: {}\n Studio Name: {}\n".format(s[0],s[1]))
  

cursor = db.cursor()

cursor.execute("Select genre_ID, genre_name FROM genre")

gen = cursor.fetchall()

print("--DISPLAYING Genre RECORDS--")

for g in gen:
    print("Genre ID: {} \n Genre Name: {}\n".format(g[0],g[1]))


cursor = db.cursor()

cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")

fil = cursor.fetchall()

print("--DISPLAYING Short Film RECORDS--")

for f in fil:
    print("Film Name: {}\nRuntime: {}\n".format(f[0],f[1]))

cursor = db.cursor()

cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

fi = cursor.fetchall()

print("--DISPLAYING Director RECORDS in Order--")

for row in fi:
    print("Film Name:", row[0])
    print("Director:", row[1])
    print("  ")



