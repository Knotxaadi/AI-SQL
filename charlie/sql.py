import mysql.connector as mysql

mydb = mysql.connect(host='localhost',user='root',password='Aadi2007',database='aadi')

if mydb.is_connected():
    print('done!!!')

cur = mydb.cursor()

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
        cur.execute(f"CREATE TABLE {T}({L[:-1]}")
    
    except ValueError as e:
        print(f"Error Occured:{e}")
        print("Please write in correct order!")
        creattable()
    
    except mysql.Error as err:
        print(f'Something is wrong {err}')
        print("Please write in correct order!")
        creattable()
    except:
        print('error occured')
        print("Please write in correct order!")
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

#def delettable():


def querytaker():
    print('''which feature do you want to use?
          1: creating table
          2: inserting values
          3: deleting values
          4: updating values
          5: altering table
          6: read table''')
    try:
        q = int(input('Enter the no:'))
        if 0<q<7:
            if q==1:
                creattable()
            elif q==2:
                insertable()
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

