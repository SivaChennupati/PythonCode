import cx_Oracle

try:
    # Type 1 Connection
    # pass the direct connection string for connection
    con = cx_Oracle.connect("system/tiger@localhost:1521/pdb1")
    c = con.cursor()
    c.execute('select username,account_status from user_users')
    for row in c:
        print(row[0], '-', row[1])
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
finally:
    if c:
        c.close()
    if con:
        con.close()
