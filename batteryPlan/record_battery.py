import psutil
import enum

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

# Get battery time remaining
time = battery.secsleft
seconds = str(time % 60)
minutes = (int)(time / 60)
hours = str((int)(minutes / 60))
minutes = str(minutes % 60)
if (int(hours) < 100):
    time_remaining = hours + " hours, " + minutes + " minutes, " + seconds + " seconds"
else:
    time_remaining = "Unavailable"

# If plugged in, time is -2
if (not plugged):
    print(percent+'% | ' + time_remaining)
else:
    print(percent+'% | ' + plugged)

#print(battery.index())
#print(battery.count())

