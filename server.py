from flask import Flask
from flask import request, jsonify
import psycopg2
from crawler import database
app = Flask(__name__)

try: 
    connection = psycopg2.connect(
        user="postgres",
        password="1234",
        host="192.168.31.171",
        port="5432",
        database="postgres",
    )
    cursor = connection.cursor()
    postgreSQL_select_Query = "select * from voucher"
    cursor.execute(postgreSQL_select_Query)
    voucher_records = cursor.fetchall()

    vouchers = []
    for i in voucher_records:
        vouchers.append(
            {
                "division_id": i[0],
                "voucher_code": str(i[1]),
                "voucher_des": i[2],
                "voucher_name": i[3]
            }
        )
    print(vouchers)
       
except (Exception, psycopg2.Error) as error:
    print(error)
finally:
    if(connection):
        cursor.close()
        connection.close()


@app.route('/',methods=['GET'])
def hello_world():
    return 'Voucher by Tien Anh'

@app.route('/api/v1/resources/vouchers/all', methods=['GET'])
def api_voucher_all():
    return jsonify(vouchers)
    

@app.route('/api/v1/resources/vouchers/',methods=['GET'])
def api_voucher():
    if 'division_id' in request.args:
        divison_id = int(request.args['division_id'])
    else:
        return "Error: No id field provided. Please specify an id."
    results = []
    for i in vouchers:
        if i['division_id'] == divison_id:
            results.append(i)
    return jsonify(results)