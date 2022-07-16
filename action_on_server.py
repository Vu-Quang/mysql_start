import mysql.connector
from datetime import date, timedelta

connection = mysql.connector.connect(host = 'localhost', user = 'Quang', password = 'Vumanhquang1', database = 'python_db')
cursor = connection.cursor()

print('database version is', connection.get_server_version())

print('Printing doctors whose specialty is Garnacologist and salary greater than 30000')

cursor.execute('select * from doctor where speciality = %s and salary > %s', ('Garnacologist', 30000))
docts = cursor.fetchall()
for doct in docts:
    print('doctor_Id', doct[0])
    print('doct_name ', doct[1])
    print('hospital_Id ', doct[2])
    print('joining date ', doct[3])
    print('speciality ', doct[4])
    print('salary ', doct[5])
    print('exp ', doct[6])

def get_doctor(hospital):
    cursor.execute('select doctor_name from doctor where hospital_id = %s', (hospital,))
    doct = cursor.fetchall()
    return doct
result = [x[0] for x in get_doctor(1)]
# result = tuple([x[0] for x in get_doctor('1')])
print('doctor in Mayo Clinic hospital are: ',end='')
print(*result, sep=', ')


# function for calculate exp of a doctor
def update_exp(doctor):
    cursor.execute("select joining_date from doctor where doctor_id = %s", (doctor,))
    year = str(cursor.fetchone()[0]).split('-') #convert to list of string
    year = [int(a.lstrip('0')) for a in year] #remove prefix 0s in each part of year, month, day if appearance
    year = date(*year) #result is date object
    exp = (date.today() - year)//timedelta(days=365)
    cursor.execute('update doctor set experience=%s where doctor_id = %s', (exp, doctor))
    connection.commit()

cursor.execute('select doctor_id from doctor where experience is null')
doc_list = cursor.fetchall()
for a in doc_list:
    update_exp(a[0])

cursor.close()
connection.close()