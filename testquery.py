import pymysql.cursors

# database connection parameters

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='docker',
                             database='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


with connection:
    with connection.cursor() as cursor:
      
        #sql variable contains the query to execute
        
        sql = 'SELECT * FROM animali WHERE identificativo = 2'
        cursor.execute(sql)
        
        #cursor.fetchone() -> prints only the frist record
        #cursor.fetchall() -> prints all the records
        
        result = cursor.fetchall()
        print(result)
    
    # there is no autocommit, so we have to commit.
    connection.commit()
