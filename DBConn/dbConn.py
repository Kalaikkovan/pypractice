# python code to connect to PGADMIN DB

import psycopg2
import openpyxl
from openpyxl.styles import Font

def dbConn():
    try:
        connection = psycopg2.connect(user = "postgres",
                                  password = "postgres",
                                  host = "127.0.0.1",
                                  port = "5432",
                                  database = "postgres")

        cursor = connection.cursor()
    # Print PostgreSQL Connection properties
        print ( connection.get_dsn_parameters(),"\n")

    # Print PostgreSQL version
        cursor.execute("COPY (select * from public.employee where salary=10000 order by id asc) TO '/home/kalai/Projects/python/Practice1/test.csv' DELIMITER ',' CSV HEADER;")
        #record = cursor.fetchall()
        #print("You are connected to - ", record,"\n")
       
 
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    finally:
        #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
                
dbConn()

