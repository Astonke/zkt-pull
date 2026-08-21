from zk import ZK
from openpyxl import Workbook
import random

def gen5():
    return f"{random.randint(0, 99999):05d}"

unique_file_name=gen5()

def append_to_file(text, filename):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)

zk = ZK('192.168.1.201', port=4370, timeout=10)

conn = zk.connect()
conn.disable_device()
attendance = conn.get_attendance()

for record in attendance:
    append_to_file(
    f"{record.user_id}\t{record.timestamp.strftime('%Y-%m-%d\t %H:%M:%S')}\t{record.status}\t{record.punch}\t1\t0\n",
    f"attendance_{unique_file_name}.dat")

conn.enable_device()
conn.disconnect()

print(f"Saved attendance_{unique_file_name}.odt ")
