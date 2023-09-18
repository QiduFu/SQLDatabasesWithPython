import json
import sqlite3


class RosterDatabase:

    def __init__(self):
        self.databaseName = 'rosterdb.sqlite'
        self.connection = None
        self.cursor = None
        self.jsonData = None
    
    #part1: connect the database
    def connectDatabase(self):
        self.connection = sqlite3.connect(self.databaseName)
        self.cursor = self.connection.cursor()

    #part2: crate tables and data
    #Do some setup
    #Set up the tables
    #Drop existing tables if any
    #Create new tables accordingly
    def createTables(self):
        self.cursor.executescript('''
        DROP TABLE IF EXISTS User;
        DROP TABLE IF EXISTS Member;
        DROP TABLE IF EXISTS Course;

        CREATE TABLE User (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            name   TEXT UNIQUE
        );

        CREATE TABLE Course (
            id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
            title  TEXT UNIQUE
        );

        CREATE TABLE Member (
            user_id     INTEGER,
            course_id   INTEGER,
            role        INTEGER,
            PRIMARY KEY (user_id, course_id)
        )
        ''')

    #part3: read and store the data into the database
    def loadData(self, fileName=None):
        if fileName is None:
            fileName = 'roster_data.json'

        # [
        #   [ "Charley", "si110", 1 ],
        #   [ "Mea", "si110", 0 ],

        strData = open(fileName).read() #open and read the file
        print(type(strData))
        self.jsonData = json.loads(strData) #convert the data into json objects

    def storeDataToDatabase(self):
        #Extracting name, title, and role from json objects
        for entry in self.jsonData:

            name = entry[0]
            title = entry[1]
            role = entry[2]

            print((name, title, role))

            #if there is a None in these 3, we skip it
            if (name is None) or (title is None) or (role is None):
                continue

            self.cursor.execute('''INSERT OR IGNORE INTO User (name)
                                    VALUES (?)''', ( name, ) )
            self.cursor.execute('SELECT id FROM User WHERE name = ? ', (name,))
            user_id = self.cursor.fetchone()[0]

            self.cursor.execute('''INSERT OR IGNORE INTO Course (title)
                                    VALUES (?)''', (title,))
            self.cursor.execute('SELECT id FROM Course WHERE title = ? ', 
                                    (title,))
            course_id = self.cursor.fetchone()[0]

            self.cursor.execute('''INSERT OR REPLACE INTO Member
                                (user_id, course_id, role) VALUES (?, ?, ?)''',
                                (user_id, course_id, role,))

            self.connection.commit()

    #part4: test and obtain the results
    def testAndObtainResults(self):
        self.cursor.execute("""
            SELECT User.name, Course.title, Member.role 
                FROM User JOIN Member JOIN Course 
                ON (User.id = Member.user_id) AND (Member.course_id = Course.id)
                ORDER BY User.name DESC, Course.title DESC, Member.role DESC 
                LIMIT 2;""")
        testResult = self.cursor.fetchone()
        print('The first row in the resulting record set: ', str(testResult))

        self.cursor.execute('''
            SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X 
                FROM User JOIN Member JOIN Course 
                ON (User.id = Member.user_id) AND (Member.course_id = Course.id)
                ORDER BY X LIMIT 1;''')
        finalResult = self.cursor.fetchone()[0]
        print('The final result: ', finalResult)

    #part5: close the cursor and connection
    def disconnectDatabase(self):
        self.cursor.close()
        self.connection.close()

if __name__=='__main__':
    database = RosterDatabase()
    database.connectDatabase()
    database.createTables()
    database.loadData()
    database.storeDataToDatabase()
    database.testAndObtainResults()
    database.disconnectDatabase()
