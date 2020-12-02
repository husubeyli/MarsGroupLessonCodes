import pymysql.cursors
#1#
# Connect to the database
connection = pymysql.connect(host='localhost',
        user='root',
        port=3306,
        password='example',
        db='MacBookPro',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)

def create_table1():
    with connection.cursor() as cursor:
        sql = """create table if not exists hospital(
            id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
            hospital_name varchar(49) NOT NULL,
            bed_count int(11) NOT NULL
        );
        """
        cursor.execute(sql)
    connection.commit()

def create_table2():
    with connection.cursor() as cursor:
        sql = """ create table if not exists doctor(
        doctor_id int(11) unsigned AUTO_INCREMENT PRIMARY KEY,
        doctor_name varchar(49) NOT NULL,
        hospital_id int(11) unsigned  NOT NULL, 
        joining_date date NOT NULL,
        speciality varchar(49) NOT NULL,
        salary int(11) NOT NULL,
        experience varchar(49),
        FOREIGN KEY (hospital_id) REFERENCES hospital(id)
        ); 
        """
        cursor.execute(sql)
    connection.commit() 

create_table1()
create_table2()


def insert_table1(hospital_name, bed_count):
    with connection.cursor() as cursor:
        sql = """ insert into MacBookPro.hospital (hospital_name, bed_count)
        values (%s, %s)
        """
        cursor.execute(sql,(hospital_name,bed_count))
    connection.commit()    

def insert_table2(doctor_name, hospital_id, joining_date, speciality, salary, experience='null'):
    with connection.cursor() as cursor:
        sql = """insert into MacBookPro.doctor (doctor_name, hospital_id, joining_date, speciality, salary, experience)
        values(%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql,(doctor_name, hospital_id, joining_date, speciality, salary, experience))
    connection.commit()   

# insert_table1('Mayo Clinic', 200)
# insert_table1('Clevand Clinic', 400)
# insert_table1('Johns Hopkings', 1000)
# insert_table1('Ucla Medical Center', 1500)


# insert_table2('David', 1, '2005-02-10', 'Pediatric', 40000)
# insert_table2('Michael', 1, '2018-07-23', 'Oncologist', 20000)
# insert_table2('Susan', 2, '2016-05-19', 'Garnacologist', 25000)
# insert_table2('Robert', 2, '2017-12-28', 'Pediatric', 28000)
# insert_table2('Linda', 3, '2004-06-04', 'Garnacologist', 42000)
# insert_table2('William', 3, '2012-09-11', 'Dermatologist', 30000)
# insert_table2('Richard', 4, '2014-08-21', 'Garnacologist', 32000)
# insert_table2('Karen', 4, '2011-10-17', 'Radiologist', 30000)

#2#

def all_print1():
    with connection.cursor() as cursor:
        sql = """ select * from MacBookPro.hospital;
        """
        cursor.execute(sql,)
    return cursor.fetchall()


def id_print1(id):
    with connection.cursor() as cursor:
        sql = """select * from MacBookPro.hospital where id = %s;
        """
        cursor.execute(sql, id )
    return cursor.fetchone()


def all_print2():
    with connection.cursor() as cursor:
        sql = """ select * from MacBookPro.doctor;
        """
        cursor.execute(sql,)
    return cursor.fetchall()


def id_print2(doctor_id):
    with connection.cursor() as cursor:
        sql = """select * from MacBookPro.doctor where doctor_id = %s;
        """
        cursor.execute(sql, doctor_id )
    return cursor.fetchone() 


# all_print1()
# all_print2()
# id_print1(2)
# id_print2(2)


#3#

def salary_speciality(speciality, salary):
    with connection.cursor() as cursor:
        sql = """ select * from doctor where speciality =%s and salary> %s;
        """
        cursor.execute(sql,(speciality, salary))
    return cursor.fetchall()

# print()
# print()
#print(salary_speciality("Pediatric",28000))#

#4#
def equal (hospital_id):
     with connection.cursor() as cursor:
        sql = """ select * from MacBookPro.doctor where hospital_id = %s;
        """
        cursor.execute(sql,(hospital_id))
     return cursor.fetchall()

#print(equal(2))#

#5#


def update(experience):
    with connection.cursor() as cursor:
        sql = """ Update MacBookPro.doctor Set experience = %s  where experience is null
        """
        cursor.execute(sql, (experience))
    connection.commit()
    

print(update("Ebejdad"))



    
    



    







    

