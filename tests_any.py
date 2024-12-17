import psycopg2

connection = psycopg2.connect(
    dbname="example_db",
    user="username",
    password="password",
    host="localhost",
    port="5432"
)