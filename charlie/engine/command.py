from tabulate import tabulate

tablec = ['make','create','draft','generate','build','construct','form','produce','develop','design','forge','invent',
          'establish','set up','assemble']
tabled = ['delete','remove','erase','clear','discard','eliminate','cancel','cut','omit','exclude','expunge','purge',
          'rub out']
tableinsert=['insert','insert into','add values','add into','add value','append','incorporate','introduce','inject','interpose','interject','insinuate','instil','infuse']
tableup = ['update','modify','amend','revise','correct','adapt','adjust','change','edit','emend','reshuffle','rearrange','reorganize','reorder','restructure','reform','revamp','renovate','renew','remodel','rebuild','reconstruct','refashion','recondition','redevelop','rework','recast','redraft','rephrase','reword','rewrite','rescript','rehash','reissue','reprint','reproduce','recreate']
tablese = ['select','show','print','display','present','exhibit','demonstrate','reveal','broadcast','telecast','screen','stream','webcast','videocast','podcast','transmit','relay','beam','send','forward','post','upload','put up','put on','put out','issue','release','circulate','disseminate','disperse','spread']
tableal = ['alter','change','convert']

def columnss(parts):
    L = parts.strip().split()   
    colum = []
    i=0
    while i < len(L):
            try:
                if L[i] == 'name' ==L[0]:
                    colum.append(f'{L[i]}')
                elif L[i] == 'equal' and L[i+1] == 'to':
                    colum.append(f'=')
                    i+=1
                elif L[i] == 'greater' and L[i+1] == 'than':
                    colum.append(f'>')
                    i+=1
                elif (L[i] == 'less' and L[i+1] == 'than') or (L[i] == 'smaller' and L[i+1] == 'than'):
                    colum.append(f'<')
                    i+=1
                elif L[i] == 'all' or L[i] == 'every' or L[i] == 'each':
                    colum.append(f'*')
                elif (L[i] != 'number' and L[i] != 'name' and L[i] !='no') and (L[i+1] == 'name' or L[i+1]== 'number' or L[i+1] == 'no'):
                    colum.append(f'{L[i]}_{L[i+1]}')
                    i+=1
                else:
                    colum.append(f'{L[i]}')
            except:
                colum.append(f'{L[i]}')
            i+=1
    return colum

def tablepri(Col,Row):
    return(tabulate(Row,Col,tablefmt="simple_outline"))

def assign_data_type(column):
    u = ''
    i=0
    while i < len(column):
        if column[i] != 'will be' and column[i] != 'will' and column[i] != 'be' and column[i] != 'to' and column[i] != 'character' and column[i] != 'number' and column[i] != 'no' and column[i] != 'integer':
            u += f' {column[i]}'
        elif column[i] == 'character':
            u += f' VARCHAR(255)'
        elif column[i] == 'number' or column[i] == 'no' or column[i] == 'integer':
            u += f' INT'
        i+=1
    return u
            
def generate_sql(query,cursor):
    a = query.split()
    try:
        #Create table
        for word in tablec:
            if word in a[:2]:
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
                cursor.execute(f"CREATE TABLE {table_name} ({', '.join(column_definitions)})")
                return f'table {table_name} created successfully'

        #Insert into table
        for word in tableinsert:
            if word in a[:2]:
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
                cursor.execute(sql_query)
                return f"Values inserted into {t_name} successfully"

        #Update table  
        for word in tableup:
            if word in a[:2]:
                parts = query.split("set")
                table_name = parts[0].split()[1]
                set_part = parts[1].split("where", 1)[0].strip()
                set_part = columnss(set_part)
                set_part = ''.join(set_part)
                where_part = parts[1].split("where", 1)[1].strip()
                where_part = columnss(where_part)
                where_part = ''.join(where_part)
                sql_query = f"UPDATE {table_name} SET {set_part} WHERE {where_part};"
                cursor.execute(sql_query)
                return f'Table {table_name} value {set_part} where {where_part} updated successfully'
                              
        #Delete table
        for word in tabled: 
            if word in a[:2]:
                parts = query.split("from")
                print(parts)
                table_name = parts[1].split("where")[0].strip()
                print(table_name)
                condition = parts[1].split("where")[1].strip()
                condition = columnss(condition)
                condition = ''.join(condition)
                print(condition)
                sql_query = f"DELETE FROM {table_name} WHERE {condition};"
                cursor.execute(sql_query)
                return f"From Table {table_name} where {condition} deleted successfully"
        
        #Select table
        for word in tablese:
            if word in a[:2]:
                parts = query.split("from")
                column = parts[0].replace(word,"").strip()
                column = columnss(column)
                column = ','.join(column)
                L= column
                if "where" in parts[1]: 
                    table_name = parts[1].split("where")[0].strip()
                    condition = parts[1].split("where")[1].strip()
                    condition = columnss(condition)
                    condition = ''.join(condition)
                    sql_query = f"SELECT {column} FROM {table_name} WHERE {condition};"
                    if column == '*':
                        cursor.execute(f"DESCRIBE {table_name}")
                        a = cursor.fetchall()
                        L=[]
                        for row in a:
                            L.append(row[0])
                    print('where clause')
                else:
                    table_name = parts[1].strip()
                    sql_query = f"SELECT {column} FROM {table_name};"
                    if column == '*':
                        cursor.execute(f"DESCRIBE {table_name}")
                        a = cursor.fetchall()
                        L=[]
                        for row in a:
                            L.append(row[0])
                    print('no where clause')
                cursor.execute(sql_query)
                a = cursor.fetchall()
                print(L)
                print(a)
                re = tablepri(L,a)
                print(re)
                return re
            
        #alter table
        for word in tableal:
            if word in a[:2]:
                al = ['add','drop','modify','change']
                parts = query.split("table")                
                for i in al:
                    if i in parts[1]:
                        table_name = parts[1].split(i)[0].strip()
                column_part = parts[1].split()
                if column_part[1] == 'add':
                    column_part = column_part[3::]
                    column_part = assign_data_type(column_part)
                    #column_part = columnss(column_part)
                    sql_query = f"ALTER TABLE {table_name} ADD {column_part};"
                    cursor.execute(sql_query)
                    return f'Column {column_part} added to {table_name} successfully'
                
                elif column_part[1] == 'drop':
                    column_part = column_part[3::]
                    sql_query = f"ALTER TABLE {table_name} DROP {column_part};"
                    cursor.execute(sql_query)
                    return f'Column {column_part} dropped from {table_name} successfully'
                
                elif column_part[1] == 'modify':
                    column_part = column_part[3::]
                    column_part = assign_data_type(column_part)
                    sql_query = f"ALTER TABLE {table_name} MODIFY {column_part};"
                    cursor.execute(sql_query)
                    return f'Column {column_part} modified in {table_name} successfully'
                
                elif column_part[1] == 'change':
                    column_part = column_part[3::]
                    column_part = assign_data_type(column_part)
                    sql_query = f"ALTER TABLE {table_name} CHANGE {column_part};"
                    cursor.execute(sql_query)
                    return f'Column {column_part} changed in {table_name} successfully'
    except:
        return 'Sorry, I am not able to understand what you are saying.'




#query = 'alter table info add column address will be character'
#query= 'alter table info drop column address'
#query = 'alter table info modify column address to integer'
#query = 'alter table info change column address to home will character'
#query = "select all from info where age equal to 17"
#print(generate_sql(query))