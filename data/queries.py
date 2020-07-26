from data import data_manager
import bcrypt
import os


def random_api_key():
    """
    :return: salt in secret key
    """
    return os.urandom(100)


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_show_by_id(id):
    return data_manager.execute_dml_statement('SELECT * '
                                              'FROM shows '
                                              'WHERE id = %(id)s;', {'id': id})


def username_exists(username):
    return data_manager.execute_dml_statement('SELECT * FROM users WHERE username = %(username)s;',
                                              {'username': username})


def register_user(username, text_password, submission_time):
    if username_exists(username):
        return False
    return data_manager.execute_dml_statement('INSERT INTO users (username,password,submission_time) '
                                              'VALUES (%(username)s,%(password)s,%(submission_time)s)',
                                              {"username": username,
                                               "password": encrypt_password(text_password),
                                               "submission_time": submission_time})


def check_user(username):
    return data_manager.execute_dml_statement('SELECT id, password '
                                              'FROM users '
                                              'WHERE username '
                                              'ILIKE %(username)s;', {"username": username})


def encrypt_password(password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_pass.decode("utf-8")


def verify_password(text_password, hashed_pass):
    return bcrypt.checkpw(text_password.encode("utf-8"), hashed_pass.encode("utf-8"))


def show_genre(id):
    return data_manager.execute_select('SELECT g.name '
                                       'FROM show_genres as sg '
                                       'LEFT JOIN genres as g '
                                       'ON sg.genre_id=g.id '
                                       'WHERE sg.show_id = %(id)s '
                                       'GROUP BY sg.show_id, g.name; ',
                                       {'id': id})

def get_actors():
    return data_manager.execute_select("""
        SELECT actors.name, shows.rating, actors.id as id
        FROM shows 
        Join show_characters 
        ON shows.id = show_characters.show_id 
        Join actors 
        ON show_characters.actor_id=actors.id 
        GROUP BY actors.name , shows.rating, actors.id
        Order BY shows.rating DESC
        LIMIT 10;
        """
    )

def getComment(movie_id):
    return data_manager.execute_select("""
        SELECT comment,user_id,id
        FROM comments
        WHERE movie_id=(%(movie_id)s)
    """, {'movie_id':movie_id })

def updateComment(commID,comment):
    return data_manager.execute_dml_statement('UPDATE comments '
                                              'SET comment=(%(comment)s) '
                                              'WHERE id =(%(commID)s); '
                                              ,
                                              {"comment": comment,"commID":commID})

def deleteComment(commID):
    return data_manager.execute_dml_statement('DELETE FROM comments '
                                              'WHERE id =(%(commID)s); '
                                              ,
                                              {"commID": commID})
def getCOmmentByID(id):
    return data_manager.execute_select("""
            SELECT comment
            FROM comments
            WHERE id=(%(id)s)
        """, {'id':id})

def addComment(user_id,movie_id,comment):
    return data_manager.execute_dml_statement("""
        INSERT INTO comments (user_id,movie_id,comment) 
        values (%(user_id)s,%(movie_id)s,%(comment)s)
        """,
                                              {'user_id': user_id,'movie_id':movie_id,'comment':comment})

def addFav(movie,user_id):
    return data_manager.execute_dml_statement("""
    INSERT INTO favorites (title,user_id) 
    values (%(movie)s,%(user_id)s)
    RETURNING id
    """,
{'movie':movie,"user_id":user_id})

def checkFav(movie,user_id):
    return data_manager.execute_select("""
SELECT 1
FROM favorites
WHERE title = (%(movie)s) AND user_id=(%(user_id)s);
""",
       {"movie":movie,"user_id":user_id})

def getActorsInfo():
    return data_manager.execute_select("""
    SELECT name, id
    FROM actors
    order by name
    """)

def getActorInfoById(id):
    return data_manager.execute_select("""
        SELECT actors.name, shows.title,show_characters.character_name
        FROM actors
        JOIN show_characters on actors.id = show_characters.actor_id
        JOIN shows on show_characters.show_id = shows.id
        WHERE actors.id =%(id)s
        """,{'id':id})

def getFavorites(user_id):
    return data_manager.execute_select("""
    SELECT title
    FROM favorites
    WHERE user_id=(%(user_id)s);
    """,
                                       {"user_id": user_id})

def get_movies_by_id(id):
    return data_manager.execute_select("""
        Select show_characters.actor_id , shows.title ,show_characters.character_name
        FROM shows 
        Join show_characters 
        ON shows.id = show_characters.show_id 
        WHERE show_characters.actor_id = %(id)s
        GROUP BY show_characters.actor_id , shows.title,show_characters.character_name
    """,
       {"id":id})


def get_last_15_rated_shows(offsetNr):
    return data_manager.execute_select(
        "SELECT shows.id, shows.title,shows.year,shows.runtime,shows.trailer, shows.homepage, shows.rating,"
        "string_agg(genres.name, ', ' ORDER BY name) as genres"
        " FROM shows"
        " JOIN show_genres ON shows.id=show_genres.show_id"
        " JOIN genres ON show_genres.genre_id=genres.id"
        ' GROUP BY shows.id,shows.rating'
        ' ORDER BY shows.rating DESC LIMIT 15'
        ' OFFSET %(offsetNr)s ',
        {'offsetNr':offsetNr})

def getTopActors(id):
    return data_manager.execute_select("""
        SELECT actors.name,actors.biography
        FROM show_characters
        JOIN actors ON show_characters.actor_id=actors.id
        WHERE show_characters.show_id=%(id)s
        LIMIT 3
    """,{'id':id})

def sort_by(offsetNr,what):
    return data_manager.execute_select(
        "SELECT shows.id, shows.title,shows.year,shows.runtime,shows.trailer, shows.homepage, shows.rating,"
        "string_agg(genres.name, ', ' ORDER BY name) as genres"
        " FROM shows"
        " JOIN show_genres ON shows.id=show_genres.show_id"
        " JOIN genres ON show_genres.genre_id=genres.id"
        f' GROUP BY shows.id,shows.{what}'
        f' ORDER BY shows.{what} DESC LIMIT 15'
        f' OFFSET {offsetNr}')

