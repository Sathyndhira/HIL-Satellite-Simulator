import serial
import time
import matplotlib.pyplot as plt

arduino = serial.Serial('COM6', 9600)
time.sleep(2)

batt_percent = 100.0
pwrg_solar = 3.0
batt_level = []
timeline = []

for hour in range(24):
    # send current battery percent to Arduino
    arduino.write(f"{int(batt_percent)}\n".encode())

    response = arduino.readline()
    current_drain = float(response.decode().strip())

    print(
        f"Hour {hour:02d} | Batter: {int(batt_percent)}% | Arduino Drain Command: {current_drain}A")

    if hour < 12:
        batt_percent = batt_percent + pwrg_solar - current_drain
    else:
        batt_percent = batt_percent - current_drain

    if batt_percent >= 100:
        batt_percent = 100
    if batt_percent <= 0:
        batt_percent = 0

    timeline.append(hour)
    batt_level.append(batt_percent)

    time.sleep(0.5)

plt.plot(timeline, batt_level)
plt.title("Satellite Battery Management System")
plt.xlabel("Time (Hours)")
plt.ylabel("Battery Level (%)")
plt.grid(True)
plt.show()
