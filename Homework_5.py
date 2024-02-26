import datetime


# Defines the News type
class News:
    # Initializes News object with its attributes
    def __init__(self, text=None, city=None):
        self.text = text
        self.city = city
        self.publish_date = datetime.datetime.now()

    # Converts object to string format
    def __str__(self):
        return f'News: \n {self.text}. \n City:{self.city}. \n Published on: {self.publish_date.strftime("%Y-%m-%d")}.\n\n'

    # Method to create and add news object
    def add(self):
        self.text = input("Enter news text: ")
        self.city = input("Enter news city: ")
        self.publish_date = datetime.datetime.now()  # get current date
        return self


# Defines the PrivateAdd type:
class PrivateAd:
    # Initializes PrivateAd object with its attributes
    def __init__(self, text=None, expiration_date=None):
        self.days_left = None
        self.text = text
        self.expiration_date = expiration_date

    # Converts object to string format
    def __str__(self):
        return f'Ad: \n {self.text}. \n Expires on: {self.expiration_date.strftime("%Y-%m-%d")}. \n Days left: {(self.expiration_date - datetime.datetime.now()).days}.\n\n'

    # Method to create and add PrivateAd object
    def add(self):
        self.text = input("Enter ad text: ")
        self.expiration_date = datetime.datetime.strptime(input("Enter expiration date (YYYY-MM-DD): "), '%Y-%m-%d')
        self.days_left = (self.expiration_date - datetime.datetime.now()).days
        return self


# Defines the NewProduct type
class NewProduct:
    # Initializes NewProduct object with its attributes
    def __init__(self, name=None, price=None, receipt_date=None):
        self.name = name
        self.price = price
        self.receipt_date = receipt_date

    # Converts object to string format
    def __str__(self):
        return f'New product: {self.name}. \n Price: {self.price}. \n Received on: {self.receipt_date.strftime("%Y-%m-%d")}.\n\n'

    # Method to create and add NewProduct object
    def add(self):
        self.name = input("Enter product name: ")
        self.price = input("Enter product price: ")
        self.receipt_date = datetime.datetime.strptime(input("Received date in format (YYYY-MM-DD): "), '%Y-%m-%d')
        return self


# Defines the Feed application
class Feed:
    # Initializes an empty news_feed
    def __init__(self):
        self.news_feed = []

    # Adds a record to the news_feed
    def add_record(self, record):
        self.news_feed.append(record.add())

    # Saves the news_feed as a string to a text file
    def publish(self, filename):
        with open(filename, 'a') as file:
            for record in self.news_feed:
                file.write(str(record))


content = Feed()
content.add_record(News())
content.add_record(PrivateAd())
content.add_record(NewProduct())
content.publish("my_news_feed.txt")
