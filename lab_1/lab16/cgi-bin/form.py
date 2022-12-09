import cgi
import sqlite3
from main import PyServerDB

from sqlite3 import Error

def id_find(req_id):
    cursor.execute(f'SELECT * FROM {tbl_name}')
    cc = cursor.fetchall()
    for d in range(len(cc)):
        if cc[d][0] == req_id:
            return True

    return False


form = cgi.FieldStorage()
if form.getvalue('table_list') is not None:  # запись в файл
    tbl_name = form.getvalue('table_list')
    file = open("cgi-bin/table.txt", "w")
    file.write(form.getvalue('table_list'))
else:
    inp = open("cgi-bin/table.txt", "r")
    tbl_name = inp.read()
    inp.close()

print("Content-type: text/html\n")
print(f"""<!DOCTYPE HTML>
        <html>
            <head>
                <meta charset="utf-8">
                <title>Table interaction {tbl_name}</title>
            </head>
            <body>
                <form action="/index.html">
                    <p><input type="submit" value="Back to table selection"></p>
                </form>
                <form action="/cgi-bin/form.py">
                    <h3>Select interaction option: {tbl_name}</h3>
                    <p><select name="act_list">
                        <option></option>
                        <option>Insert a new entry</option>
                        <option>Update entry</option>
                        <option>Delete entry</option>
                        <option>Print out all entries</option>
                    </select></p>
                    <p><input type="submit" value="Enter"></p>
                """)

# if form.getvalue('act_list') is not None:
connection = PyServerDB('pyserver.db')
cursor = connection.getCursor()
table_str = '<table><tr>\n'

act = form.getvalue('act_list')
if form.getvalue('act_list') is not None:  # запись в файл
    act = form.getvalue('act_list')
    file = open("cgi-bin/option.txt", "w")
    file.write(form.getvalue('act_list'))
    file.close()
else:
    inp = open("cgi-bin/option.txt", "r")
    act = inp.readline()
    inp.close()

if act is not None:
    if act == 'Insert a new entry':
        print("""
                Enter the data of a new space-separated record: <input type="text" name="new_tran">
                <p><input type="submit" value="Sent"></p>
                    <style>
                    input[type="text"] 
                    {
                        width: 300px;
                    }
                    </style>
               </form>
        """)

        row = form.getfirst("new_tran").split()
        cursor.execute(f'SELECT * FROM {tbl_name}')  # имя таблицы можно хранить в файле
        headers = [description[0] for description in cursor.description]

        if len(row) != len(headers):
            print(f"""Invalid number of fields -> The entry wasn't recorded to the {tbl_name}""")
        elif len(row) == len(headers):
            fields = ', '.join('?' for _ in row)
            # fields = fields[:-2]
            cursor.execute(f'INSERT INTO {tbl_name} VALUES({fields})', row)
            connection.getConnection().commit()
            print("""The record was successfully added""")

        file = open("cgi-bin/option.txt", "w")
        file.write('None')
        file.close()

    if act == 'Update entry':
        print("""
                        Enter an entry ID you want to update: <input type="text" name="update_id"><br /><br />
                        Enter new space-separated data: <input type="text" name="update_tran">
                        <p><input type="submit" value="Sent"></p>
                            <style>
                            input[name="update_tran"] 
                            {
                                width: 300px;
                            }
                            input[name="update_id"]
                            {
                                width:50px;
                            }
                            </style>
                       </form>
                """)


        update_id = int(form.getfirst("update_id"))
        row = form.getfirst("update_tran").split()
        cursor.execute(f'SELECT * FROM {tbl_name}')
        headers = [description[0] for description in cursor.description]

        find = id_find(update_id)
        sql_str = 'UPDATE ' + tbl_name + ' SET '

        if len(row) < len(headers) - 1 or len(row) >= len(headers):
            print(f"""Invalid number of fields -> The entry wasn't recorded to the {tbl_name}""")
        elif not find:
            print('Entry with such ID doesn\'t exist')
        elif len(row) == len(headers) - 1 and find:
            for i in range(len(row)):
                sql_str += headers[i + 1] + ' = "' + row[i] + '", '
            sql_str = sql_str[:-2]
            sql_str += f' where {headers[0]} = ' + str(update_id)
            cursor.execute(sql_str)
            connection.getConnection().commit()
            print("""Record updated successfully""")

        file = open("cgi-bin/option.txt", "w")
        file.write('None')
        file.close()

    if act == 'Delete entry':
        print("""
                        Enter an entry ID you want to delete: <input type="text" name="delete_id">
                        <p><input type="submit" value="Sent"></p>
                            <style>
                            input[name="delete_id"]
                            {
                                width:50px;
                            }
                            </style>
                       </form>
                """)
        cursor.execute(f'SELECT * FROM {tbl_name}')  # имя таблицы можно хранить в файле
        headers = [description[0] for description in cursor.description]
        delete_id = int(form.getfirst("delete_id"))
        find = id_find(delete_id)
        if find:
            cursor.execute(f'DELETE from {tbl_name} where {headers[0]}= {delete_id}')
            connection.getConnection().commit()
            print("""Record deleted successfully""")
        else:
            print('Entry with such ID doesn\'t exist')

    file = open("cgi-bin/option.txt", "w")
    file.write('None')
    file.close()

if act == 'Print out all entries':

    cursor.execute(f'SELECT * FROM {tbl_name}')  # имя таблицы можно хранить в файле
    headers = [description[0] for description in cursor.description]
    for i in range(len(headers)):
        table_str += '<th>' + headers[i] + '</th>'
    table_str += '</tr>\n\n'

    for row in cursor.fetchall():
        table_str += '<tr>\n'
        tmp = list(row)
        for i in range(len(tmp)):
            table_str += '<td>' + str(tmp[i]) + '</td>'
        table_str += '</tr>\n'

    table_str += """<style>table {
           border: 1px solid grey;
           border-collapse: collapse;
            }
           td {
           border: 1px solid grey;
           text-align: center;
            }
            th {
           border: 1px solid grey;
           min-width:160px;
            }
        </table>
        </style>"""
    print(table_str)
    print('</table>')
    file = open("cgi-bin/option.txt", "w")
    file.write('None')
    file.close()

print("""</body>
    </html>""")