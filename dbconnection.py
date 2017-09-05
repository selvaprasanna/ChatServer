# dbconnection.py: Connection and utilities related to mySQL

from config import HOST, MYSQL_PORT, USER, PASSWORD, DB_NAME, TABLE_NAME
from mysql.connector import errorcode
import mysql.connector

def create_database(cnx=None):
    if cnx is None:
        cnx = connect_to_mysql()

    cursor = cnx.cursor()
    # Create the Database --- ChatServerDB
    cursor.execute("CREATE DATABASE %s DEFAULT CHARACTER SET 'utf8';" % DB_NAME)
    cnx.database = DB_NAME
    # Create the Table --- chat_table
    cursor.execute("CREATE TABLE %s (timestamp VARCHAR(25), user VARCHAR(100), message TEXT);" % TABLE_NAME)

def add_chat_message_to_db(timestamp, user, message):
    cnx = connect_to_mysql()
    try:
        cnx.database = "ChatServerDB"
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            # If MySQL DB is not found, create one!
            create_database(cnx)
        else:
            print(err)
            exit(1)

    cursor = cnx.cursor()
    print timestamp
    cursor.execute("INSERT INTO chat_table (timestamp, user, message) VALUES (%s, %s, %s);", (timestamp, user, message))
    close_connection(cnx, cursor)

def get_latest_records(count_of_records=100):
    cnx = connect_to_mysql()
    try:
        cnx.database = DB_NAME
    except:
        print "No database found in MySQL"
        return {"error": True}

    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM chat_table ORDER BY timestamp DESC LIMIT %s;" % str(count_of_records))
    records = {}
    messages = []
    for record in cursor:
        current_record = {}
        current_record["timestamp"] = record[0]
        current_record["user"] = record[1]
        current_record["text"] = record[2]
        messages.append(current_record)

    records["messages"] = messages
    close_connection(cnx, cursor)
    return records

def get_unique_users():
    cnx = connect_to_mysql()
    try:
        cnx.database = DB_NAME
    except:
        print "No database found in MySQL"
        return {"error": True}

    cursor = cnx.cursor()
    cursor.execute("SELECT DISTINCT user FROM chat_table;")

    records = {}
    users = []
    for record in cursor:
        users.append(record[0])

    records["users"] = users
    close_connection(cnx, cursor)
    return records

def close_connection(cnx, cursor):
    cnx.commit()
    cursor.close()
    cnx.close()

def connect_to_mysql():
    return mysql.connector.connect(host=HOST, port=str(MYSQL_PORT), user=USER, password=PASSWORD)
