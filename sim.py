import matplotlib.pyplot as plt

batt_percent = 100
pwrg_solar = 3
pwrd_computer = 5
batt_level = []
time = []

for hour in range(24):
    current_drain = 0
    if batt_percent < 50:
        current_drain = 1.5
    else:
        current_drain = pwrd_computer
    if hour < 12:
        batt_percent = batt_percent + pwrg_solar - current_drain
        if batt_percent >= 100:
            batt_percent = 100
    elif hour >= 12:
        batt_percent = batt_percent - current_drain
    time.append(hour)
    batt_level.append(batt_percent)


plt.plot(time, batt_level)
plt.title("Satellite Battery Management System")
plt.xlabel("Time (Hours)")
plt.ylabel("Battery Level (%)")
plt.grid(True)
plt.show()
