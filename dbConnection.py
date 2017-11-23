import psycopg2


def query_db(statement):
    database = "del2jus8rch1te"
    host = "ec2-54-83-40-208.compute-1.amazonaws.com"
    port ="5432"
    user="trxfpaplidosmm"
    password="243a030d40cd7b88ae86d65f1c0640cbfac08ae46eab9d6c29769409e1d4ffd2"
    conn = psycopg2.connect(database=database, host=host, port=port, user=user, password=password)
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(statement)
    return cur.fetchall()
