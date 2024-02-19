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

def show_films(cursor, title):

    cursor.execute("Select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' FROM film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

def main():

    cursor = db.cursor()

    show_films(cursor, "--DISPLAYING FILMS--")

    insertQuery = "INSERT INTO film(film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id) VALUES ('The Lorax', '2012', '95', 'Chris Renaud', (SELECT studio_id FROM studio WHERE studio_name = 'Universal Pictures'), (SELECT genre_id FROM genre WHERE genre_name = 'Drama'));" 
    cursor.execute(insertQuery)
    show_films(cursor, "--DISPLAYING FILMS AFTER INSERT--")

    updateQuery = "UPDATE film SET genre_id = (SELECT genre_id FROM genre WHERE genre_name = 'Horror') WHERE film_name = 'Alien';"
    cursor.execute(updateQuery)
    show_films(cursor, "-- DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror --")

    deleteQuery = "DELETE FROM film WHERE film_name = 'Gladiator';"
    cursor.execute(deleteQuery)
    show_films(cursor, "--DISPLAYING FILMS AFTER DELETE--")
    
main()

    
        
