import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="1234",
        host="127.0.0.1",
        port="5432",
        database="postgres",
    )
    cursor = connection.cursor()
    cursor.execute("SELECT version();")
    record = cursor.fetchone()
except (Exception, psycopg2.Error) as error:
    print(error)
finally:
    if(connection):
        cursor.close()
        connection.close()


def insert_voucher(data: dict):
    sql = """INSERT INTO voucher(id_division, price_voucher, des_voucher, name_voucher) VALUES(%s, %s, %s, %s) 
    ON CONFLICT (name_voucher, id_division) 
    DO UPDATE SET price_voucher = EXCLUDED.price_voucher, des_voucher = EXCLUDED.des_voucher"""
    conn = None
    cursor = None
    try:
        conn = psycopg2.connect(
            user="postgres",
            password="1234",
            host="127.0.0.1",
            port="5432",
            database="postgres",
        )
        cursor = conn.cursor()
        cursor.execute(sql, (data["id_division"], data["price_voucher"], data["des_voucher"], data["name_voucher"]))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        raise

    finally:
        if(conn):
            cursor.close()
            conn.close()




if __name__ == "__main__":
    insert_voucher({
        "id_division": 1,
        "price_voucher": 1001,
        "des_voucher": 1000,
        "name_voucher": 199,
    })
