from zk import ZK
from openpyxl import Workbook

# Device configuration
DEVICE_IP = "192.168.1.201"   # Change to your K40 IP
DEVICE_PORT = 4370

zk = ZK(DEVICE_IP, port=DEVICE_PORT, timeout=10)

conn = None

try:
    print("Connecting to device...")
    conn = zk.connect()

    print("Disabling device...")
    conn.disable_device()

    print("Reading users...")
    users = conn.get_users()

    wb = Workbook()
    ws = wb.active
    ws.title = "Users"

    ws.append([
        "UID",
        "User ID",
        "Name",
        "Privilege",
        "Password",
        "Card Number",
        "Group ID"
    ])

    for user in users:
        ws.append([
            user.uid,
            user.user_id,
            user.name,
            user.privilege,
            user.password,
            getattr(user, "card", ""),
            getattr(user, "group_id", "")
        ])

    wb.save("users.xlsx")

    print(f"Successfully exported {len(users)} users to users.xlsx")

except Exception as e:
    print("Error:", e)

finally:
    if conn:
        try:
            conn.enable_device()
            conn.disconnect()
        except:
            pass
