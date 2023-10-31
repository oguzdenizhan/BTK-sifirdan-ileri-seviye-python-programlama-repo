import mysql.connector
from datetime import datetime
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "My.123456.o",
    database = "schooldb"
)