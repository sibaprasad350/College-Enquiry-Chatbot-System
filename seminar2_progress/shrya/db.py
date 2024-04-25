import sqlite3
from sqlite3 import Error
from random import randint


def create_conn(db_file):
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    finally:
        conn.close()


conn = sqlite3.connect('db\\sqlite\\db\\pythonsqlite.db')

c = conn.cursor()
c.execute("PRAGMA foreign_keys = ON")


def create_tables(c):
    try:

        c.execute('CREATE TABLE IF NOT EXISTS LOGIN'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'email text, '
                  'pswd text)');

        c.execute('CREATE TABLE IF NOT EXISTS STUD_INFO'
                  '(id integer PRIMARY KEY NOT NULL, '
                  'fname text, '
                  'lname text, '
                  'sem_id integer, '
                  'FOREIGN KEY(id) REFERENCES LOGIN(id) ON DELETE CASCADE)');

        c.execute('CREATE TABLE IF NOT EXISTS GPA_DETAILS'
                  '(id integer, '
                  'sem1 real, '
                  'sem2 real, '
                  'sem3 real, '
                  'sem4 real, '
                  'sem5 real, '
                  'sem6 real, '
                  'sem7 real, '
                  'sem8 real, '
                  'FOREIGN KEY(id) REFERENCES STUD_INFO(id) ON DELETE CASCADE)');

    except Error as e:
        print(e)


create_tables(c)
conn.commit()


def populate(c):
    try:
        # id, email, pswd

        LOGIN_INFO = [(1, '20cse019.sibaprasadmaharana@giet.edu', 'prasad'),
                      (2, '22cs028.ramkrishna@giet.edu', 'ramkrishna'),
                      (3, '23mba023.ranjitamaharana@giet.edu', 'ranjitama'),
                      (4, '20cse361.susantakumarmohapatra@giet.edu', 'susanta'),
                      (5, '22cse034.aniketkumar@giet.edu', 'aniketkumar'),
                      (6, '22EE001.deepakmohanty@giet.edu', 'deepakmohanty'),
                      (7, '20cse028.anweshkumarpradhan@giet.edu', 'anweshkumar'),
                      (8, '24AI111.haripatra@giet.edu', 'haripatra'),
                      (9, '23ML099.anjalimishra@giet.edu', 'anjalimishra'),
                      (10, '21cse013.subhamprakshswain@giet.edu', 'subham'),
                      (11, '20cse267.sibasankarswain@giet.edu', 'sibasankar'),
                      (12, '24DS672.bidyabhusanmajhi@giet.edu', 'bidyabhusan')]

        c.executemany('INSERT INTO LOGIN VALUES (?,?,?)', LOGIN_INFO)

        # id, fname, lname, sem_id

        STUD_DETAILS = [(1, 'Sibaprasad', 'Maharana', 8),
                        (2, 'Ram', 'Krishan', 7),
                        (3, 'Ranjita', 'Maharana', 5),
                        (4, 'Susanta', 'Mohapatra', 8),
                        (5, 'Aniket', 'Kumar', 7),
                        (6, 'Deepak', 'Mohanty', 6),
                        (7, 'Anweshkumar', 'Pradhan', 4),
                        (8, 'Hari', 'Patra', 3),
                        (9, 'Anjli', 'Mishra', 2),
                        (10, 'Subhamprakash', 'Swain', 3),
                        (11, 'Sibasankar', 'Swain', 8),
                        (12, 'Bidyabhushan', 'Majhi', 6)]

        c.executemany('INSERT INTO STUD_INFO VALUES (?,?,?,?)', STUD_DETAILS)

        # id, sem(1 to 8)

        GPA_DETAILS = [(1, 8.9, 8.3, 8.6, 8.5, 8.4, 0.0, 0.0, 0.0),
                       (2, 8.9, 8.3, 8.6, 8.5, 8.4, 8.9, 0.0, 0.0),
                       (3, 8.9, 8.3, 8.6, 8.5, 8.4, 8.5, 9.2, 0.0),
                       (4, 8.9, 8.3, 8.6, 8.5, 8.4, 0.0, 0.0, 0.0),
                       (5, 8.6, 8.3, 9.0, 8.5, 8.4, 8.9, 0.0, 0.0),
                       (6, 8.4, 8.3, 9.4, 8.9, 8.8, 9.5, 9.2, 0.0),
                       (7, 8.4, 8.3, 7.9, 8.5, 8.4, 8.9, 9.0, 0.0),
                       (8, 8.0, 8.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (9, 8.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (10, 8.1, 8.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0),
                       (11, 8.7, 8.7, 8.6, 8.5, 0.0, 0.0, 0.0, 0.0),
                       (12, 8.9, 8.7, 8.6, 8.5, 8.1, 0.0, 0.0, 0.0)
                       ]

        c.executemany('INSERT INTO GPA_DETAILS VALUES (?,?,?,?,?,?,?,?,?)', GPA_DETAILS);

    except Error as e:
        print(e)


populate(c)
conn.commit()


def bulkDataIns():
    #    print("DATA INSERTED")
    #     for num in range(13,150):
    #         if (num%2)==0:
    #             c.execute( "INSERT INTO LOGIN VALUES(?,?,?)",(num,'abc'+str(num)+'@rknec.edu','abc'+str(num)) )
    ##             c.execute( "INSERT INTO STUD_INFO VALUES(?,?,?,?)", () )
    #         else:
    #             c.execute("INSERT INTO LOGIN VALUES(?,?,?)",(num,'xyz'+str(num)+'@rknec.edu','xyz'+str(num)) )

    for num in range(13, 201):
        if (num % 2) == 0:

            c.execute("INSERT INTO LOGIN VALUES(?,?,?)", (num, 'abc' + str(num) + '@rknec.edu', 'abc' + str(num)))
            c.execute("INSERT INTO STUD_INFO VALUES(?,?,?,?)", (num, 'ABC', 'DEF', 8))
            c.execute("INSERT INTO GPA_DETAILS VALUES(?,?,?,?,?,?,?,?,?)",
                      (num, 8.4, 8.3, 9.4, 8.9, 8.8, 9.5, 9.2, 0.0))
        else:
            c.execute("INSERT INTO LOGIN VALUES(?,?,?)", (num, 'xyz' + str(num) + '@rknec.edu', 'xyz' + str(num)))
            c.execute("INSERT INTO STUD_INFO VALUES(?,?,?,?)", (num, 'PQR', 'XYZ', 7))

            c.execute("INSERT INTO GPA_DETAILS VALUES(?,?,?,?,?,?,?,?,?)",
                      (num, 8.6, 8.3, 9.0, 8.5, 8.4, 8.9, 0.0, 0.0))


bulkDataIns()
conn.commit()

for num in range(13, 15):
    print(num, 'abc' + str(num) + '@rknec.edu', 'abc' + str(num))