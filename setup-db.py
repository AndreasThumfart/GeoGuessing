import sqlite3

# Function to execute the SQL script from the setup.sql file
def execute_sql_script():
    # Open the SQL script file
    with open('setup.sql', 'r') as sql_file:
        sql_script = sql_file.read()  # Read the entire file contents
    
    # Connect to the SQLite database (it will create the file if it doesn't exist)
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Execute the SQL script
    try:
        cursor.executescript(sql_script)
        conn.commit()
        print("SQL script executed successfully!")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Call the function to execute the SQL script
if __name__ == '__main__':
    execute_sql_script()
