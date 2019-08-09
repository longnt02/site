import cx_Oracle

dsn_tns = cx_Oracle.makedsn('ORAACB_90', '1521', service_name='orademo')
conn = cx_Oracle.connect(user='osibank', password='osibank', dsn=dsn_tns)

print(conn.version)

conn.close()
