#sql test
#pip install pyodbc
#pip list
"""
Connects to a SQL database using pyodbc, i.e., to  db
"""
import pyodbc

server = 'dxxxxxx'
database = 'x'
username = 'xxxxxxx'
password = 'xxxxxxxxxx!'

# Construct the connection string
conn_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'


try:
  # Connect to the database
  conn = pyodbc.connect(conn_string)

  # Print a success message
  print("Connected to SQL Server database successfully!")

  # You can now execute SQL statements using a cursor
  cursor = conn.cursor()

except pyodbc.Error as ex:
  # Print error message in case of connection failure
  print("Error connecting to database:", ex)
'''
finally:
  # Close the connection (always recommended)
  if conn:
    conn.close()
    print("Connection closed.")''''''
'''
'''
import pyodbc
import sqlite3

def connect_to_sql_server():
  server = 'acceptance.b-fine.be,1433'
  database = 'master'
  username = 'sa'
  password = 'bfineSolutions2019!'

# Construct the connection string using the correct driver name
  conn_string = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}'
#cursor = conn_string.cursor()

  try:
      conn = pyodbc.connect(conn_string)
      print("Connected to SQL Server database successfully!")
      return conn
      #cursor = conn.cursor()

  except pyodbc.Error as ex:
    print("Error connecting to database:", ex)
    return None
  
''' 
'''finally:
    # Close the connection if it was opened
    if conn:
        conn.close()
        print("Connection closed.")'''

'''SQL_1 = """SELECT COUNT(DISTINCT LotID) AS UniqueLotCount FROM [BRX_IL].[dbo].[Instrument]"""
cursor.execute(SQL_QUERY_1)'''
'''
SQL_QUERY_1 = """
SELECT TOP 1000 * FROM [BRX_IL].[dbo].[Instrument]
--SELECT TOP 2000 [LotId],[AccruedInterest] FROM [BRX_IL].[dbo].[Instrument]
WHERE 1 = 1
AND AccruedInterest <> 0
"""'''


'''
def calculation():
    """
    Connects to the database and executes the query to get the count of unique LotID.
    """
    conn = connect_to_sql_server()
    if conn is not None:
        try:
            # Create a cursor object using the connection
            cursor = conn.cursor()
            # Define the query
            #query1 = "SELECT COUNT(DISTINCT LotID) AS UniqueLotCount FROM [BRX_IL].[dbo].[Instrument]"
            query2 = "SELECT TOP 1000 * FROM [BRX_IL].[dbo].[Instrument] --SELECT TOP 2000 [LotId],[AccruedInterest] FROM [BRX_IL].[dbo].[Instrument] WHERE 1 = 1 AND AccruedInterest <> 0"
            # Execute the query
            cursor.execute(query2)
            # Fetch the result
            result = cursor.fetchone()
            if result:
                print("Unique Lot Count:", result.UniqueLotCount)
            else:
                print("No data found.")
            
            # Close the cursor and the connection
            cursor.close()
            conn.close()
        except Exception as e:
            print("Error during query execution:", e)
    else:
        print("Failed to connect to the database.")

# Call the function to get the unique lot count
calculation()



#cursor.execute("SELECT COUNT(DISTINCT LotID) AS UniqueLotCount FROM [BRX_IL].[dbo].[Instrument]")
'''