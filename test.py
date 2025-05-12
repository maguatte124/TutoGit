import psycopg2

conn_params = {
    "host": "db.vbbjmbmwijtdkoepnhsz.supabase.co",
    "port": 5235,
    "database": "postgres",
    "user": "postgres",
    "password": 'Km5="Jx_jn8N3wb'
}

try:
    conn = psycopg2.connect(**conn_params)

    cur = conn.cursor()

    cur.execute("SELECT * FROM examen.candidats c")

    rows = cur.fetchall()

    for row in rows:
        print(row)


    cur.close()
    conn.close()

except Exception as e:
    print("ERROR", e)
