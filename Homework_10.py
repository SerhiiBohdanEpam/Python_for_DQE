import datetime
import sqlite3

# Function to read info/records from a file
def add_info_from_file(filename):
    with open(filename, 'r') as f:
        return f.read().splitlines()  # Returns the lines read from the file as a list

# Class to manage SQLite database operations
class Database:
    def __init__(self, db_name):
        # Connect to the SQLite database using provided db_name
        self.conn = sqlite3.connect(db_name)
        self.c = self.conn.cursor()

    def create_table(self, table_name, fields):
        # Drop the table if it exists and create a fresh table
        # Please be aware that this will delete any existing data in these tables
        self.c.execute(f"DROP TABLE IF EXISTS {table_name}")
        # Create a new table with the provided table name and field names
        self.c.execute(f"CREATE TABLE {table_name} ({', '.join([f'{k} {v}' for k, v in fields.items()])})")
        self.conn.commit()  # Commit the changes

    def insert_data(self, table_name, data):
        # Insert a row of data into the table
        sql_query = f"INSERT INTO {table_name} ({', '.join(data.keys())}) VALUES ({', '.join(['?' for _ in data])})"
        try:  # Try to execute the query
            self.c.execute(sql_query, tuple(data.values()))
            self.conn.commit()  # Commit the changes
        except sqlite3.OperationalError as e:  # In case of any operational errors
            # Print the error and the attempted data for debugging
            print(f"Failed to insert data into {table_name}: {e}")
            print(f"Attempted to insert the following data: {data}")

    def select_all(self, table_name):
        # Select all records from the table
        self.c.execute(f"SELECT * FROM {table_name}")
        # Fetch all rows from the last executed SELECT statement
        return self.c.fetchall()

    def close_connection(self):
        # Close the connection to the SQLite database
        self.conn.close()

# Initialize the database
db = Database('content.db')

# Class to manage News records
class News:
    def __init__(self, db):
        self.db = db
        # Create the News table in the database
        db.create_table('News', {'id': 'INTEGER PRIMARY KEY', 'text': 'TEXT', 'city': 'TEXT', 'publish_date': 'TEXT'})

    def add(self):
        method = input("Enter NEWS data from a file or manually? Enter 'file' or 'manual': ")
        if method.lower() == 'file':
            filename = input("File path or press enter for default path: ")
            filename = filename if filename else 'default_content.txt'
            file_contents = add_info_from_file(filename)
            self.text = file_contents[0]
            self.city = file_contents[1]
        else:
            self.text = input("News text: ")
            self.city = input("City: ")
        self.publish_date = datetime.datetime.now()
        # Insert the entered news data into the News table in the database
        self.db.insert_data('News', {'text': self.text, 'city': self.city, 'publish_date': self.publish_date.strftime('%Y-%m-%d')})
        return self

# Class to manage PrivateAd records
class PrivateAd:
    def __init__(self, db):
        self.db = db
        # Create the Ad table in the database
        db.create_table('Ad', {'id': 'INTEGER PRIMARY KEY', 'text': 'TEXT', 'expiration_date': 'TEXT', 'days_left': 'INTEGER'})

    def add(self):
        method = input("Enter AD data from a file or manually? Enter 'file' or 'manual': ")
        if method.lower() == 'file':
            filename = input("File path or press enter for default path: ")
            filename = filename if filename else 'default_content.txt'
            file_contents = add_info_from_file(filename)
            self.text = file_contents[0]
            self.expiration_date = datetime.datetime.strptime(file_contents[1], '%Y-%m-%d')
        else:
            self.text = input("Ad text: ")
            self.expiration_date = datetime.datetime.strptime(input("Expiration date (YYYY-MM-DD): "), '%Y-%m-%d')
        self.days_left = (self.expiration_date - datetime.datetime.now()).days
        # Insert the entered ad data into the Ad table in the database
        self.db.insert_data('Ad', {'text': self.text, 'expiration_date': self.expiration_date.strftime('%Y-%m-%d'), 'days_left': self.days_left})
        return self

# Class to manage NewProduct records
class NewProduct:
    def __init__(self, db):
        self.db = db
        # Create the Product table in the database
        db.create_table('Product', {'id': 'INTEGER PRIMARY KEY', 'name': 'TEXT', 'price': 'TEXT', 'receipt_date': 'TEXT'})

    def add(self):
        method = input("Enter PRODUCT data from a file or manually? Enter 'file' or 'manual': ")
        if method.lower() == 'file':
            filename = input("File path or press enter for default path: ")
            filename = filename if filename else 'default_content.txt'
            file_contents = add_info_from_file(filename)
            self.name = file_contents[0]
            self.price = file_contents[1]
            self.receipt_date = datetime.datetime.strptime(file_contents[2], '%Y-%m-%d')
        else:
            self.name = input("Product name: ")
            self.price = input("Price: ")
            self.receipt_date = datetime.datetime.strptime(input("Received date (YYYY-MM-DD): "), '%Y-%m-%d')
        # Insert the entered product data to the Product table in the database
        self.db.insert_data('Product', {'name': self.name, 'price': self.price, 'receipt_date': self.receipt_date.strftime('%Y-%m-%d')})
        return self

# Class to manage feed of records (news, ads, products)
class Feed:
    def __init__(self):
        self.news_feed = []

    def add_record(self, record):
        self.news_feed.append(record.add())  # Invoke the add method on the provided record and append the result to the feed.

    def publish(self, filename):
        with open(filename, 'a') as file:
            for record in self.news_feed:
                file.write(str(record))

# Create instances of News, PrivateAd, and NewProduct
news = News(db)
private_ad = PrivateAd(db)
new_product = NewProduct(db)

# Create an instance of Feed and add records
content = Feed()
content.add_record(news)
content.add_record(private_ad)
content.add_record(new_product)


# Publish the added records to my_content_feed.txt
content.publish("my_content_feed_db.txt")

news_records = db.select_all('News')
for news in news_records:
    print(news)

ad_records = db.select_all('Ad')
for ad in ad_records:
    print(ad)

product_records = db.select_all('Product')
for product in product_records:
    print(product)

# Close the connection to the database
db.close_connection()