import mysql.connector as mysql
from tabulate import tabulate

mydb = mysql.connect(host='localhost',user='root',password='1955',database='CSpro')

if mydb.is_connected():
    print('done!!!')

cur = mydb.cursor()

def tablure(Col,Row):
    print(tabulate(Row,Col,tablefmt="simple_outline"))

def creattable():
    try:
        T = input("Enter the table name:")
        cur.execute(f"SHOW TABLES LIKE %s",(T,))
        re= cur.fetchone()
        if re:
            print(f"Table {T} exist already")
            print(" Enter New name")
            creattable()
        n = int(input("Enter the number of columns will be there:"))
        L = ''
        for col in range(n):
            sw=''
            ColName = input(f"Enter the {col+1} column name:")
            ColType = input(f"Enter the type of {ColName}:")
            s = input("Do you want any key in this ?(y/n):")
            if s=='y':
                Key = input("primary or foreign?")
                if Key=='primary':
                    ColKey = 'primary key'
                    sw += f'{ColName} {ColType} {ColKey}'
                    L += f"{sw},"
            else:
                sw += f'{ColName} {ColType}'
                L += f"{sw},"
                continue
        print(L[:-1])
        cur.execute(f"CREATE TABLE {T}({L[:-1]})")
        print(f"Table {T} Created!!")
    
    except ValueError as e:
        print(f"Error Occured:{e}")
        print("Please write in correct value!")
        creattable()
    
    except mysql.Error as err:
        print(f'Something is wrong {err}')
        print("Please write in correct order!")
        creattable()

    except:
        print('error occured')
        print("something went wrong!")
        creattable()
        
def insertable():
    try:
        T = input("Enter the table name:")
        cur.execute(f"SHOW TABLES LIKE %s",(T,))
        re= cur.fetchone()
        if re:
            cur.execute(f"DESCRIBE {T}")
            ro = cur.fetchall()
            L=[]
            for row in ro:
                L.append(row[0])
            n = int(input("enter the number of Rows wants to enter:"))
            print('''make sure that:
            for name:enter in ('name_here')
            for integer:enter
            for date: enter in('date')''')
            for i in range(n):
                A =input(f"Enter in {L} format:")
                A.partition(',')
                print(A)
                cur.execute(f"INSERT INTO {T} VALUES({A})")
                mydb.commit()
            print("Values are inserted")
        else:
            print('Table not exist!!')
            cur.execute("SHOW TABLES")
            re = cur.fetchall()
            for i in re:
                print(f':-{i[0]}')
            print('This are the tables!, enter again')
            insertable() 
    
    except ValueError as e:
        print(f"Error Occured:{e}")
        print("Please write in correct order!")
        insertable()
    
    except mysql.Error as err:
        print(f'Something is wrong {err}')
        print("Please write in correct order!")
        insertable()

    except:
        print('error occured')
        print("Please write in correct order!")
        insertable()

def delettable():
    try:
        T = input("Enter the table name:")
        cur.execute(f"SHOW TABLES LIKE %s",(T,))
        re= cur.fetchone()
        if re:
            y =int(input('''1: DELETE entire table
                2:condition:'''))
            if y==1:
                cur.execute(f"DELETE FROM {T}")
                mydb.commit()
                print("Table Deleted!")
            elif y==2:
                cur.execute(f"DESCRIBE {T}")
                ro = cur.fetchall()
                ColNames=[]
                for row in ro:
                    ColNames.append(row[0])
                print(f"This are the columns {ColNames}")
                W= input('Enter the condition:')
                cur.execute(f"DELETE FROM {T} WHERE {W}")
                mydb.commit()
                print(f"DELETED from Table where {W}")
            else:
                print("DO it AGain!")
                delettable()
        else:
            print('Table not exist!!')
            cur.execute("SHOW TABLES")
            re = cur.fetchall()
            for i in re:
                print(f':-{i[0]}')
            print('This are the tables!, enter again')

    except ValueError as e:
        print(f"Error Occured:{e}")
        print("Please write in correct value!")
        delettable()
    
    except mysql.Error as err:
        print(f'Something is wrong {err}')
        print("Please write in correct order!")
        delettable()

    except:
        print('error occured')
        print("something went wrong!")
        delettable()

def Updatetable():
    try:
        T=input("Enter name of table:")
        cur.execute(f"SHOW TABLES LIKE %s",(T,))
        re= cur.fetchone()
        if re:
            cur.execute(f"DESCRIBE {T}")
            ro = cur.fetchall()
            ColNames=[]
            for row in ro:
                ColNames.append(row[0])
            print(f"This are the columns {ColNames}")
            S = input("Enter the changes in <columnname=value>:")
            W= input('Enter the condition:')
            cur.execute(f"UPDATE {T} SET {S} WHERE {W}")
            mydb.commit()
            print(f"Table {T} is Updated!")
        else:
            print('Table not exist!!')
            cur.execute("SHOW TABLES")
            re = cur.fetchall()
            for i in re:
                print(f':-{i[0]}')
            print('This are the tables!, enter again')
        
    except ValueError as e:
        print(f"Error Occured:{e}")
        print("Please write in correct value!")
        Updatetable()
    
    except mysql.Error as err:
        print(f'Something is wrong {err}')
        print("Please write in correct order!")
        Updatetable()

    except:
        print('error occured')
        print("something went wrong!")
        Updatetable()

def altertable():
    try:
        T=input("Enter name of table:")
        cur.execute(f"SHOW TABLES LIKE %s",(T,))
        re= cur.fetchone()
        if re:
            cur.execute(f"DESCRIBE {T}")
            ro = cur.fetchall()
            ColNames=[]
            for row in ro:
                ColNames.append(row[0])
            print(f"This are the columns {ColNames}")
            print('''Here are options:
                1:Add column
                2:Modify column datatype
                3:change name of column
                4:Drop column
                5:Add key constraint
                6:Drop key constraint''')
            y=int(input("Enter the above options[1 to 6]:"))
            if 0<y<7:
                if y==1:
                    CDS = input("Enter<columnname datatype constraint> in format as possible:")
                    cur.execute(f"ALTER TABLE {T} ADD {CDS}")
                    mydb.commit()
                    print(f"Column {CDS} added in table {T}")

                elif y==2:
                    CDS = input("Enter<columnname new-datatype> in format as possible:")
                    cur.execute(f"ALTER TABLE {T} MODIFY {CDS}")
                    mydb.commit()
                    print(f"Column {CDS} MODIFIED in table {T}")

                elif y==3:
                    CDS = input("Enter<old-columnname new-columnname new-datatype> in format as possible:")
                    cur.execute(f"ALTER TABLE {T} CHANGE {CDS}")
                    mydb.commit()
                    print(f"Column {CDS} Changed in table {T}")

                elif y==4:
                    CDS = input("Enter<columnname> in format as possible:")
                    cur.execute(f"ALTER TABLE {T} DROP {CDS}")
                    mydb.commit()
                    print(f"Column {CDS} DROPPED in table {T}")

                elif y==5:
                    CDS = input("Enter<keytype(Columnname)> in format as possible:")
                    cur.execute(f"ALTER TABLE {T} ADD {CDS}")
                    mydb.commit()
                    print(f"Constraint {CDS} added in table {T}")

                elif y==6:
                    CDS = input("Enter<keytype> in format as possible:")
                    cur.execute(f"ALTER TABLE {T} DROP {CDS}")
                    mydb.commit()
                    print(f"Constraint {CDS} dropped in table {T}")

                else:
                    print("Enter the correct value between 1 to 6")
                    altertable() 
        else:
            print('Table not exist!!')
            cur.execute("SHOW TABLES")
            re = cur.fetchall()
            for i in re:
                print(f':-{i[0]}')
            print('This are the tables!, enter again')
            altertable()

    except ValueError as e:
        print(f"Error Occured:{e}")
        print("Please write in correct value!")
        altertable()
    
    except mysql.Error as err:
        print(f'Something is wrong {err}')
        print("Please write in correct order!")
        altertable()

    except:
        print('error occured')
        print("something went wrong!")
        altertable()

def readtable():
    try:
        T = input("Enter the table name:")
        cur.execute(f"SHOW TABLES LIKE %s",(T,))
        re= cur.fetchone()
        if re:
            y =int(input('''1: Read entire table
                2:condition:'''))
            if y==1:
                cur.execute(f"SELECT * FROM {T}")
                r=cur.fetchall()
                cur.execute(f"DESCRIBE {T}")
                ro = cur.fetchall()
                L=[]
                for row in ro:
                    L.append(row[0])
                tablure(L,r)
                print("Table Printed!")
            elif y==2:
                print('''Options:
                      1:In/not in
                      2:between/ not between
                      3:Like/ not like
                      4:ORDER BY''')
                cur.execute(f"DESCRIBE {T}")
                ro = cur.fetchall()
                ColNames=[]
                for row in ro:
                    ColNames.append(row[0])
                print(f"This are the columns {ColNames}")
                W= int(input('Enter the option:'))
                S = input("Enter the column names that should be print('ALL',<any column-name>):")
                L=[]
                if S.upper()=='ALL':
                    cur.execute(f"DESCRIBE {T}")
                    ro = cur.fetchall()
                    for row in ro:
                        L.append(row[0])
                else:
                    R=[]
                    for i in S:
                        if i in L:
                            R.append(i)
                    L=R        


                if W==1:
                    col = input("enter <column name In (values)> format:")
                    cur.execute(f"SELECT {S} FROM {T} WHERE {col}")
                    re = cur.fetchall()
                    tablure(L,re)


            else:
                print("DO it AGain!")
                delettable()
        else:
            print('Table not exist!!')
            cur.execute("SHOW TABLES")
            re = cur.fetchall()
            for i in re:
                print(f':-{i[0]}')
            print('This are the tables!, enter again')

    except ValueError as e:
        print(f"Error Occured:{e}")
        print("Please write in correct value!")
        readtable()
    
    except mysql.Error as err:
        print(f'Something is wrong {err}')
        print("Please write in correct order!")
        readtable()

    except:
        print('error occured')
        print("something went wrong!")
        readtable()

def Droptable():
    try:
        T = input("Enter the table name:")
        cur.execute(f"SHOW TABLES LIKE %s",(T,))
        re= cur.fetchone()
        if re:
            cur.execute(f"DROP TABLE {T}")
            mydb.commit()
            print(f"Table {T} Dropped!")
        else:
            print('Table not exist!!')
            cur.execute("SHOW TABLES")
            re = cur.fetchall()
            for i in re: 
                print(f':-{i[0]}')
            print('This are the tables!, enter again')
            Droptable()

    except ValueError as e:
        print(f"Error Occured:{e}")
        print("Please write in correct value!")
        Droptable()
    
    except mysql.Error as err:
        print(f'Something is wrong {err}')
        print("Please write in correct order!")
        Droptable()

    except:
        print('error occured')
        print("something went wrong!")
        Droptable()

def querytaker():
    print('''which feature do you want to use?
          1: creating table
          2: inserting values
          3: deleting values
          4: updating values
          5: altering table
          6: read table
          7: Drop Table''')
    try:
        q = int(input('Enter the no:'))
        if 0<q<8:
            if q==1:
                creattable()
            elif q==2:
                insertable()
            elif q==3:
                delettable()
            elif q==4:
                Updatetable()
            elif q==5:
                altertable()
            elif q==6:
                readtable()
            elif q==7:
                Droptable()
        else:
            print("wrong value")
            querytaker()

    except ValueError:
        print("enter the correct type('integer')")
        querytaker()

if __name__ == '__main__':
    print('Hello sir!!')
    querytaker()
    Y = input("Do you want to continue?(y/n):")
    if Y=='y':
        querytaker()
    else:
        print("Thank you sir!!")

