# GET COLUM NAMES FROM A TABLE

# LIBRARIES AND MODULES
import psycopg2  # For PostgreSQL

# Properties of the connection string
database = "metsastys"
user = "postgres"
password = "Q2werty"
host = "localhost"
port = "5432"

# Try to establish a connection to DB server
try:
    # Create a connection object
    dbaseconnection = psycopg2.connect(database=database, user=user, password=password,
                                      host=host, port=port)
    
    # Create a cursor to execute commands and retrieve result set
    cursor = dbaseconnection.cursor()
    
    # Execute a SQL command to get hunters (jasen)
    command = "SELECT * FROM public.jasen;"
    cursor.execute(command)
    # get number of rows in the result set
    rows = cursor.rowcount
    print("Tulos joukossa on", rows, "riviä.")
    print("")

    # Get colum names from cursor
    colum_names = [colum_name[0] for colum_name in cursor.description]
    print("Sarakkeiden nimet ovat:")
    for colum in colum_names:
        print(colum)        
    print("Sarakeluettelo päättyi.")
    print("")    
    
# Throw an error if connection or cursor creation fails                                     
except(Exception, psycopg2.Error) as error:
    print("Tietokantayhteydessä tapahtui virhe.", error)

# If or if not successfull close the cursor and the connection   
finally:
    if (dbaseconnection):
        cursor.close()
        dbaseconnection.close()
        print("Yhteys tietokantaan katkaistiin.")
