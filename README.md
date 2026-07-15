#To run the project first set up
python3 -m venv venv
source venv/bin/activate

#install the following dependancies
pip install pyzk openpyxl pandas pillow
sudo apt install python3-tk

#before run check physical and lan connection to device
# < enp0s31f6 > is my ethernet profile in usage 
#this is when the biometric is directly connected to the pc via eth
#other workarounds may be used provided a networking connection is made and the device is set to not use dhcp
#< default > status as of model zkt 40 > 192.168.1.201 , port 4370
#the commands below ensure the pc is the same subnet as the biometric device

ip link
sudo ip addr flush dev enp0s31f6
sudo ip addr add 192.168.1.10/24 dev enp0s31f6
sudo ip link set enp0s31f6 up

#the run per script to get att/user
#eg
python3 get_attendance.py
