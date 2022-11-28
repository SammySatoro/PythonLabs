def lab15():
    class PyServerDB:
        import sqlite3
        from sqlite3 import Error

        __db: sqlite3.Connection
        __cursor: sqlite3.Cursor

        def __init__(self, db_name):
            import sqlite3
            from sqlite3 import Error
            try:
                self.__db = sqlite3.connect(db_name)
                self.__cursor = self.__db.cursor()
            except Error:
                print(Error)

        def sent_query(self, query):
            from sqlite3 import Error
            try:
                self.__cursor.execute(query)
            except Error:
                print(Error)

        def get_select(self, query):
            from sqlite3 import Error
            try:
                return list(self.__cursor.execute(query))
            except Error:
                print(Error)

        def create_table(self, query):
            self.__cursor.execute(query)
            self.__db.commit()


        def get_table_names(self):
            return self.__cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

        def get_table_data(self, table):
            return list(self.__cursor.execute(f'SELECT * FROM {table}'))

        def drop_table(self, table):
            from sqlite3 import Error
            try:
                self.__cursor.execute(f'DROP TABLE {table}')
                self.__db.commit()
                print(f'\'{table}\' table has been deleted.')
            except Error:
                print('Table with such name don\'t exist.')

        def insert(self, table, fields, values):
            from sqlite3 import Error
            placeholders = ', '.join('?' for _ in fields)
            query = f"INSERT INTO {table}({', '.join(i for i in fields)}) VALUES ({placeholders})"
            try:
                self.__cursor.execute(f"SELECT * FROM {table}")
                if values not in self.__cursor.fetchall():
                    self.__cursor.execute(query, values)
                    self.__db.commit()
                else:
                    print('This entry already exists')
                    for value in self.__cursor.execute(f"SELECT * FROM {table}"):
                        print(value)
            except Error:
                print('Entry with such entry ID already exists.\nTable:', table)

        def insert_many(self, table, fields, values):
            from sqlite3 import Error
            placeholders = ', '.join(str(i) for i in values)
            query = f"INSERT INTO {table}({fields}) VALUES ({placeholders})"
            print(query)
            try:
                self.__cursor.execute(f"SELECT * FROM {table}")
                if values not in self.__cursor.fetchall():
                    self.__cursor.execute(query)
                    self.__db.commit()
                else:
                    print('This entry already exists')
                    for value in self.__cursor.execute(f"SELECT * FROM {table}"):
                        print(value)
            except Error:
                print('Entry with such entry ID already exists.\nTable:', table)

        def update(self, query):
            from sqlite3 import Error
            if query.split()[0].lower() == 'update':
                self.__cursor.execute(query)
                self.__db.commit()
            else:
                raise Error('Query format is not correct...')

        def get_rowcount(self, table):
            self.__cursor.execute(f'SELECT * FROM {table}')
            return len(self.__cursor.fetchall())

        def close_connection(self):
            self.__db.close()

        def set_foreign(self, tabel1, table2):
            pass


    db = PyServerDB('pyserver.db')


    table = 'Show'

    for i in db.get_select(f'SELECT * FROM {table}'):
        print(i)
    print('---------------------')

    q1 = 'select Cost from Ticket where TicketID>5'
    q2 = 'select FirstName, MiddleName, LastName from Visitor'
    q3 = 'select FirstName, MiddleName, LastName from Visitor join Ticket on Visitor.TicketID = Ticket.TicketID join Show on Ticket.ShowID = Show.ShowID where AmountOfSoldTickets>40'
    # db.update('update Visitor as v set FirstName=\'C\', MiddleName=\'Ch\', LastName=\'Ben \' from Ticket as t where t.TicketID = v.TicketID and Place=2')
    # db.update('update Ticket set Place = Place + 10 where Place>30')
    # db.update('update Show set AmountOfSoldTickets = a.amount from (select Show.ShowID, count(AmountOfSoldTickets) as amount '
    #           'from Show, Ticket where Show.ShowID = Ticket.ShowID group by Show.ShowID) as a where Show.ShowID = a.ShowID')
    
    for i in db.get_select(f'SELECT * FROM {table}'):
        print(i)


# demo
if __name__ == "__main__":
    lab15()
