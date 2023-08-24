import mysql.connector

def create_and_query_states(username, password, db_name):
    try:
        # Connect to the MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            database=db_name
        )
        
        cursor = connection.cursor()

        # Create the states table
        create_table_query = """
        CREATE TABLE IF NOT EXISTS states (
            id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(256) NOT NULL,
            PRIMARY KEY (id)
        );
        """
        cursor.execute(create_table_query)
        connection.commit()
        
        # Insert sample data
        insert_data_query = """
        INSERT INTO states (name) VALUES
            ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");
        """
        cursor.execute(insert_data_query)
        connection.commit()

        # Query and display the states
        query_states = "SELECT * FROM states ORDER BY id"
        cursor.execute(query_states)
        results = cursor.fetchall()

        print("id\tstate")
        print("--\t-----")
        for row in results:
            print(f"{row[0]}\t{row[1]}")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <db_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        create_and_query_states(username, password, db_name)
