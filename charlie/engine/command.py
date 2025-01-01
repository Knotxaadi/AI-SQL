

tablec = ['make','create','draft','generate','build','construct','form','produce','develop','design','forge','invent',
          'establish','set up','assemble']
tabled = ['delete','remove','erase','clear','discard','eliminate','cancel','cut','omit','exclude','expunge','purge',
          'rub out']
tableinsert=['insert','insert into','add values','add into','add value','append','incorporate','introduce','inject','interpose','interject','insinuate','instil','infuse']


def columnss(parts):
    L = parts.strip().split()
    print(L)    
    colum = []
    i=0
    while i < len(L):
            try:
                if L[i] == 'name' ==L[0]:
                    colum.append(f'{L[i]}')
                elif (L[i] != 'number' and L[i] != 'name' and L[i] !='no') and (L[i+1] == 'name' or L[i+1]== 'number' or L[i+1] == 'no'):
                    colum.append(f'{L[i]}_{L[i+1]}')
                    i+=1
                else:
                    colum.append(f'{L[i]}')
            except:
                colum.append(f'{L[i]}')
            i+=1
    return colum


def generate_sql(query):
    try:
        #Create table
        for word in tablec:
            if word in query.lower():
                parts = query.split('where')
                table_name = parts[0].replace("create table","").replace("make a table",'').strip()
                columns = columnss(parts[1]) if len(parts)>1 else[]
                column_definitions = []
                for column in columns:
                    #column = column.strip()
                    #assiging data type
                    if "name" in column:
                        column_definitions.append(f"{column} VARCHAR(255)")
                    elif "number" in column or "no" in column or "age" in column:
                        column_definitions.append(f"{column} INT")
                    else:
                        column_definitions.append(f"{column} VARCHAR(255)")
                return f"CREATE TABLE {table_name} ({', '.join(column_definitions)})"

        #Insert into table
        for word in tableinsert:
            if word in query.lower():
                parts = query.split("values")
                t_name = parts[0].replace(word,"").strip()
                
                values_part = parts[1].strip()  
                value = values_part.split()
                values = []
                print(value)
                for val in value:
                    if val.isnumeric():
                        values.append(int(val))
                    else:
                        values.append(f"{val}")  

                sql_query = f"INSERT INTO {t_name} VALUES {tuple(values)}"
                print(sql_query)
                return f"INSERT INTO {t_name} VALUES ({', '.join(value)})"
                
        #Delete table     
        for word in tabled: 
            if word in query:
                return 'Deleting the file'
    except:
        return 'Sorry, I am not able to understand what you are saying.'



#query= 'create table info where name last name age mobile number employee number address'
#query = 'add into students values shashank somvanshi 20'
#print(generate_sql(query))
