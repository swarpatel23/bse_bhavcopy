import requests
import zipfile
import csv
import redis
from datetime import date


def download_and_extract(url, zip_save_path, csv_save_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        with open(zip_save_path, 'wb') as f:
            f.write(response.content)
        with zipfile.ZipFile(zip_save_path, 'r') as zip:
            zip.extractall(csv_save_path)

    return response.status_code


def parse_and_save(csv_file, redis_conn):
    with open(csv_file) as f:
        csv_reader = csv.DictReader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                redis_conn.hmset(row["SC_NAME"].strip(), {
                                 "code": row["SC_CODE"], "open": row["OPEN"], "high": row["HIGH"], "low": row["LOW"], "close": row["CLOSE"]})
                print(redis_conn.hgetall(row["SC_NAME"].strip()))
            line_count += 1


def get_bhavcopy():
    today = date.today()
    present_day = today.strftime("%d%m%y")

    url = "https://www.bseindia.com/download/BhavCopy/Equity/"
    url = url + "EQ" + present_day + "_CSV.ZIP"

    zip_save_path = "./bsebhav/" + present_day + ".zip"   # path to save zip file
    csv_save_path = "./bsebhav"     # directory where extracted csv get stored

    state = download_and_extract(url, zip_save_path, csv_save_path)
    redis_conn = redis.Redis('localhost')

    if state == 200:
        csv_file = csv_save_path + "/EQ" + present_day + ".CSV"    # ???
        parse_and_save(csv_file, redis_conn)


get_bhavcopy()
