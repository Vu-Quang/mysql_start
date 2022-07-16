import mysql.connector

cnt = mysql.connector.connect(host = 'localhost', user = 'root', password = 'Vumanhquang1')
cur = cnt.cursor()

cur.execute('CREATE database if not exists python_db')
cur.execute('use python_db')
cur.execute('''CREATE TABLE if not exists Hospital (
            Hospital_Id INT UNSIGNED NOT NULL, 
            Hospital_Name TEXT NOT NULL, 
            Bed_Count INT, 
            PRIMARY KEY (Hospital_Id))
            ''')
data = [(1, 'Mayo Clinic', 200),(2, 'Cleveland Clinic', 400), (3, 'Johns Hopkins', 1000), (4, 'UCLA Medical Center', 1500)]
cur.executemany('INSERT INTO Hospital (Hospital_Id, Hospital_Name, Bed_count) VALUES (%s,%s,%s)', data)


cur.execute('''CREATE TABLE if not exists Doctor (
                Doctor_Id INT UNSIGNED NOT NULL, 
                Doctor_Name TEXT NOT NULL, 
                Hospital_Id INT NOT NULL, 
                Joining_Date DATE NOT NULL, 
                Speciality TEXT NULL, 
                Salary INT NULL,
                Experience INT NULL,
                PRIMARY KEY (Doctor_Id))
            ''')
cur.executemany("INSERT INTO Doctor (Doctor_Id, Doctor_Name, Hospital_Id, Joining_Date, Speciality, Salary) VALUES (%s,%s,%s,%s,%s,%s)",
            [(101, 'David', 1, '2005-2-10', 'Pediatric', '40000'),
            (102, 'Michael', 1, '2018-07-23', 'Oncologist', '20000'),
            (103, 'Susan', 2, '2016-05-19', 'Garnacologist', '25000'),
            (104, 'Robert', 2, '2017-12-28', 'Pediatric ', '28000'),
            (105, 'Linda', 3, '2004-06-04', 'Garnacologist', '42000'),
            (106, 'William', 3, '2012-09-11', 'Dermatologist', '30000'),
            (107, 'Richard', 4, '2014-08-21', 'Garnacologist', '32000'),
            (108, 'Karen', 4, '2011-10-17', 'Radiologist', '30000')]
            )
cnt.commit()
cur.execute('show databases')

cur.close()
cnt.close()