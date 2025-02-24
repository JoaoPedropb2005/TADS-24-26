import sqlite3

def connect_db(db_name:str):
    """connect to an existent databse.
        if not exist, it will create one.
    Args:
        db_name (str): datase name

    """
    conn = sqlite3.connect(db_name)

    return conn