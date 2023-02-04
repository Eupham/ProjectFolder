import pymongo

def create_mongodb_user(username, password, database_name, collection_name):
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")

    # Create the database if it does not already exist
    db = client[database_name]

    try:
        # Create the user with only the necessary permissions
        db.command("createUser",
                   username,
                   pwd=password,
                   roles=[{"role": "readWrite", "db": database_name, "collection": collection_name}])
    except pymongo.errors.OperationFailure as e:
        # User already exists, just ignore
        pass

    # Authenticate as the newly created user
    client.close()
    client = pymongo.MongoClient(f"mongodb://{username}:{password}@localhost:27017/{database_name}")

    # Verify that the user has been created and has the correct permissions
    return client[database_name].command("serverStatus")["ok"]

# Example usage
result = create_mongodb_user("myuser", "mypassword", "mydatabase", "dicts")
print(result) # should return 1
