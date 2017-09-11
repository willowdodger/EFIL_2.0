import subprocess
import os



sudoPassword = 'K01dun43'
subprocess.call(3)

result = os.listdir("/sys/class/power_supply/BAT0/device/power_supply/BAT0/voltage_now.txt")
print(result)


# openFile = open("/home/willowdodger/Downloads/test.html", "r")
openFile = open("/sys/class/power_supply/BAT0/device/power_supply/BAT0/voltage_now.txt")
readFile = openFile.read()
print(readFile)


energyOfEfil = 10
if energyOfEfil <= 10:
    print("get energy, because there is left only", energyOfEfil, "%...")
else:
    print("d")
