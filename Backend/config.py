class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///scraper.db" #Tells Flask to connect to a database file named scraper.db.
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This tells the app not to keep track of things that doesn’t have to.
