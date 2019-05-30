import os
import datetime
import pymysql

# Get username from cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user= username,
                            password= '',
                            db='Chinook')
                            
try:
    #Run a query
    with connection.cursor() as cursor:

        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    # Close the connection, regardless of whether the above was succcessful
    connection.close()