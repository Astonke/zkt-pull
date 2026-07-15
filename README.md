# ZKTeco Biometric Device Utility

This project connects to a ZKTeco biometric device to retrieve attendance records and user information.

## Prerequisites

- Python 3.x
- Linux (Ubuntu/Debian recommended)
- Physical or LAN connection to the biometric device

---

## 1. Create a Python Virtual Environment

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

---

## 2. Install Python Dependencies

```bash
pip install pyzk openpyxl pandas pillow
```

Install Tkinter (required for GUI components):

```bash
sudo apt update
sudo apt install python3-tk
```

---

## 3. Connect the Biometric Device

Before running any scripts:

- Ensure the biometric device is powered on.
- Ensure there is a physical Ethernet/LAN connection between the PC and the biometric device.
- Configure the biometric device with a **static IP address** (DHCP should be disabled).

### Default Device Settings

| Setting | Value |
|---------|-------|
| Device Model | ZKT 40 |
| IP Address | `192.168.1.201` |
| Port | `4370` |

---

## 4. Configure the Network Interface

If the biometric device is connected directly to your computer via Ethernet, configure your network interface to be on the same subnet.

Replace `enp0s31f6` with your Ethernet interface if different.

### List Available Interfaces

```bash
ip link
```

### Configure the Interface

```bash
sudo ip addr flush dev enp0s31f6
sudo ip addr add 192.168.1.10/24 dev enp0s31f6
sudo ip link set enp0s31f6 up
```

Verify the configuration:

```bash
ip addr show enp0s31f6
```

---

## 5. Run the Scripts

Retrieve attendance records:

```bash
python3 get_attendance.py
```

Retrieve users:

```bash
python3 get_users.py
```

Update users (if applicable):

```bash
python3 update_users.py
```

Replace the script name with whichever utility you intend to execute.

---

## Troubleshooting

### Unable to Connect

- Verify the Ethernet cable is connected.
- Confirm the biometric device IP address.
- Ensure the PC is on the same subnet as the device.
- Confirm the device is listening on port `4370`.
- Disable DHCP on the biometric device if using a direct Ethernet connection.

### Check Connectivity

```bash
ping 192.168.1.201
```

If the device responds, the network connection has been established successfully.

---

## Project Structure

```
.
├── get_attendance.py
├── get_users.py
├── update_users.py
├── requirements.txt
└── README.md
```

---

## Notes

- These scripts use the **pyzk** library to communicate with ZKTeco biometric devices.
- Ensure no other software is connected to the biometric device while running the scripts.
- Administrative privileges (`sudo`) may be required when configuring network interfaces.
