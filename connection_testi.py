# FOR TESTING PSYCOPG2 CONNECTIONS TO LOCAL POSTGRESQL DATABASE

# LIBRARIES AND MODULES
from msilib.schema import Condition
import psycopg2

# properties of the connec"tion string
database = "metsastys"
user = "postgres"
password = "Q2werty"
host = "localhost"
port = "5432"

# Try to establish a connection to DB server

try:
    databaseconnection = psycopg2.connect(
        database=database, user=user, password=password, host=host, port=port)

    # Create a cursor to execute commands on the connection
    cursor =databaseconnection.cursor()    
    cursor.execute("SELECT version();")    
    version_number = cursor.fetchone()
    print("PostgreSQL:n versionumero on ", version_number)

except (Exception, psycopg2.Error) as e:
    print("Tietokantayhteydessä tapahtui virhe", e)

finally:    
    if (databaseconnection):
     cursor.close() 
     databaseconnection.close() 
    print("Login ok, yhteys katkaistiin ")
   


 