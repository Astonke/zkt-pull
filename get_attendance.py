from zk import ZK
from openpyxl import Workbook

zk = ZK('192.168.1.201', port=4370, timeout=10)

conn = zk.connect()
conn.disable_device()

attendance = conn.get_attendance()

wb = Workbook()
ws = wb.active
ws.title = "Attendance"

ws.append([
    "User ID",
    "Timestamp",
    "Status",
    "Punch",
    "UID"
])

for record in attendance:
    ws.append([
        record.user_id,
        str(record.timestamp),
        record.status,
        record.punch,
        record.uid
    ])

wb.save("attendance.xlsx")

conn.enable_device()
conn.disconnect()

print(f"Saved {len(attendance)} records to attendance.xlsx")
