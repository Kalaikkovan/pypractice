import psycopg2

def dbConn():
    
    dbname = 'postgres'
    username = 'postgres'
    password = 'postgres'
    hostname = 'localhost'
    hostport = 5432
    
    try:
        connection = psycopg2.connect(database=dbname,user=username,password = password,host = hostname,port=hostport)
        connection.cursor()
        
        print(connection.get_dsn_parameters())
    except:
        print('Unable to connect to database')
    else:
        print('Connection is successfull')
    
    finally:
        print('This must get executed')
        
dbConn()