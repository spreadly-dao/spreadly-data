import pyrqlite.dbapi2 as dbapi2

# Connect to the database
connection = dbapi2.connect(
    host="localhost",
    port=4001,
)

try:
    with connection.cursor() as cursor:
        cursor.execute(
            """
            CREATE TABLE users (
                id SERIAL PRIMARY KEY,
                alias TEXT UNIQUE NOT NULL,
                primary_wallet_address_id INT UNIQUE,
                hashed_password TEXT NOT NULL,
                is_active BOOLEAN DEFAULT true,
                is_superuser BOOLEAN DEFAULT false
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE ergo_addresses (
                id SERIAL PRIMARY KEY,
                user_id INT NOT NULL,
                address TEXT UNIQUE,
                is_smart_contract BOOLEAN DEFAULT false
            );
        """
        )
        # cursor.executemany('INSERT INTO users(alias, primary_wallet_address_id,) VALUES(?)', ))
finally:
    connection.close()
