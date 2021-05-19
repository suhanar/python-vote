
import psycopg2
try:
    connection = psycopg2.connect(user = "postgres",
                                  password = "postgre123",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "usersdb")

    cursor = connection.cursor()
    #sql = "CREATE TABLE USERS(NAME VARCHAR,PASSWORD VARCHAR);"
    sql_insert = "INSERT INTO USERS (NAME,PASSWORD) VALUES ('manu','1abc'),('suhan','2abc'),('dev','3abc')";


    #cursor.execute(sql)
    cursor.execute(sql_insert)
    connection.commit()
    print("Table created")
except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
        if(connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
