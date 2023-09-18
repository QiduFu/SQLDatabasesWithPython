import xml.etree.ElementTree as ET
import sqlite3 as sql


class TracksDatabase:

    def __init__(self):
        self.databaseName = 'tracksDatabase.sqlite'
        self.connection = ''
        self.cursor = ''
        self.dataFile = ''

    def loadData(self, fileName=None):
        if fileName is None:
            fileName = 'Library.xml'
        self.dataFile = ET.parse(fileName)

    def connectDatabase(self):
        self.connection = sql.connect(self.databaseName)
        self.cursor = self.connection.cursor()

    def createTables(self):

        #execute many entries 
        self.cursor.executescript('''
            DROP TABLE IF EXISTS Artist;
            DROP TABLE IF EXISTS Album;
            DROP TABLE IF EXISTS Genre;
            DROP TABLE IF EXISTS Track;

            CREATE TABLE Artist(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
            );

            CREATE TABLE Genre(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                name TEXT UNIQUE
            );

            CREATE TABLE Album(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                artist_id INTEGER,
                title TEXT UNIQUE
            );

            CREATE TABLE Track(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
                title TEXT  UNIQUE,
                album_id  INTEGER,
                genre_id  INTEGER,
                len INTEGER, 
                rating INTEGER, 
                count INTEGER
            );
        ''')

    def storeDataToDatabase(self):
        findings = self.dataFile.findall('dict/dict/dict')
        print('Dict Count:', len(findings))
        #self.cursor.execute(''' ''')

        for entry in findings:
            #print(entry)
            if self.lookup(entry, 'Track ID') is None:
                continue

            name = TracksDatabase.lookup(entry, 'Name')
            artist = TracksDatabase.lookup(entry, 'Artist')
            genre = TracksDatabase.lookup(entry, 'Genre')
            album = TracksDatabase.lookup(entry, 'Album')
            length = TracksDatabase.lookup(entry, 'Total Time')
            rating = TracksDatabase.lookup(entry, 'Rating')
            count = TracksDatabase.lookup(entry, 'Play Count')

            #sanity checking: if one of the listed items is None, we will skip it
            if (name is None) or (artist is None) or \
                (genre is None) or (album is None):
                continue

            #print(name, artist, album, count, rating, length)

            #insert and update the tables from leaves to the root tables
            #insert data into artist table and get its primary key for future table joinning
            self.cursor.execute('''INSERT OR IGNORE INTO Artist(name)
                                VALUES(?)''', (artist,))
            self.cursor.execute('SELECT id FROM Artist WHERE name = ?', (artist,))
            artist_id = self.cursor.fetchone()[0]

            #insert data into genre table and get its primary key for future table joinning
            self.cursor.execute('''INSERT OR IGNORE INTO Genre(name)
                                VALUES(?)''', (genre,))
            self.cursor.execute('SELECT id FROM Genre WHERE name = ?', (genre,))
            genre_id = self.cursor.fetchone()[0]

            #insert data into album table and get its primary key for future table joinning
            self.cursor.execute('''INSERT OR IGNORE INTO Album(title, artist_id)
                                VALUES(?,?)''', (album, artist_id))
            self.cursor.execute('SELECT id FROM Album WHERE title = ?', (album,))
            album_id = self.cursor.fetchone()[0]

            #insert/updat the root table (tracks) and get its primary key for future table joinning
            self.cursor.execute('''INSERT OR REPLACE INTO 
                            Track(title, album_id, genre_id, len, rating, count)
                            VALUES(?, ?, ?, ?, ?, ?)''', 
                            (name, album_id, genre_id, length, rating, count))
            
            self.connection.commit()  #connection is commit

    #show the database data: o(N)
    def showDatabase(self):
        selectedData = self.cursor.execute('''
            SELECT Track.title, Artist.name, Album.title, Genre.name 
                FROM Track JOIN Genre JOIN Album JOIN Artist 
                ON (Track.genre_id = Genre.id) AND 
                    (Track.album_id = Album.id) AND 
                    (Album.artist_id = Artist.id)
                ORDER BY Artist.name LIMIT 3
            ''')

        for dataEntry in selectedData:
            print('Title:', dataEntry[0], 'Atrist:', dataEntry[1], 
                    'Album:', dataEntry[2], 'Genre:', dataEntry[3])

    #close the cursor connection: o(1)
    def disconnectDatabase(self):
        self.cursor.close() 
        self.connection.close()

    #look up the items in the file: o(N)
    @staticmethod
    def lookup(data, key):
        found = False
        for child in data:
            if found:
                return child.text
            if (child.tag == 'key') and (child.text == key):
                found = True

        return None

if __name__=='__main__':
    database = TracksDatabase()
    database.loadData()
    database.connectDatabase()
    database.createTables()
    database.storeDataToDatabase()
    database.showDatabase()
    database.disconnectDatabase()


