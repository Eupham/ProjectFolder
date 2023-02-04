import psycopg2

def create_postgres_user(username, password, database_name, table_name):
    # Connect to PostgreSQL
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )
    cur = conn.cursor()

    # Create the user if it does not already exist
    cur.execute(f"CREATE USER IF NOT EXISTS {username} WITH PASSWORD '{password}'")

    # Grant the necessary permissions to the user
    cur.execute(f"GRANT readWrite, create ON DATABASE {database_name} TO {username}")
    cur.execute(f"GRANT readWrite, create ON TABLE {database_name}.{table_name} TO {username}")

    # Commit the changes and close the connection
    conn.commit()
    cur.close()
    conn.close()

# Example usage
create_postgres_user("myuser", "mypassword", "mydatabase", "dicts")