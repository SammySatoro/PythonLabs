def task15():
    import sqlite3
    from sqlite3 import Error

    def sql_connection():
        try:
            db = sqlite3.connect('pyserver.db')
            return db
        except Error:
            print(Error)

    def sql_print_table(table):
        with con:
            cursorObj.execute(f"SELECT * FROM {table}")
            print(cursorObj.fetchall())

    def sql_print_tables():
        with con:
            cursorObj.execute('SELECT name from sqlite_master where type= "table"')
            print(cursorObj.fetchall())

    def sql_table(query):
        cursorObj.execute(query)
        con.commit()


    def sql_drop_table(table):
        try:
            cursorObj.execute(f'DROP TABLE {table}')
            con.commit()
            print(f'\'{table}\' table has been deleted.')
        except Error:
            print('Table with such name don\'t exist.')

    def sql_insert(table, fields, values):
        placeholders = ', '.join('?' for i in fields)
        query = f"INSERT INTO {table}({', '.join(i for i in fields)}) VALUES ({placeholders})"
        try:
            cursorObj.execute(f"SELECT * FROM {table}")
            if values not in cursorObj.fetchall():
                cursorObj.execute(query, values)
                con.commit()
            else:
                print('This entry already exists')
                for value in cursorObj.execute(f"SELECT * FROM {table}"):
                    print(value)
        except Error:
            print('Entry with such entry ID already exists.\nTable:', table)

    def sql_update(query):
        if query.split()[0].lower() == 'update':
            print('Yep')
            cursorObj.execute(query)
            con.commit()
        else:
            raise Error('Query format is not correct...')

    def sql_rowcount(table):
        cursorObj.execute(f'SELECT * FROM {table}')
        return len(cursorObj.fetchall())

    con = sql_connection()
    cursorObj = con.cursor()
    sql_table("CREATE TABLE IF NOT EXISTS test(id integer PRIMARY KEY, name text)")
    # sql_insert('test', ('id', 'name'), (0, 'Alice'))
    # sql_update('UPDATE test SET name = \'Jinx\' where name = \'Alice\'')

    sql_drop_table('test')
    # print(sql_print_tables())
    # print(sql_rowcount('test'))
    # sql_print_table('test')


# demo
if __name__ == "__main__":
    task15()
