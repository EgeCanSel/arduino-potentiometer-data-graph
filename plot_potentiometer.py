import serial
import time
import matplotlib.pyplot as plt
PORT      = input("Type Port Name").strip()     
BAUD_RATE = 9600
DURATION  = 30      
arduino   = serial.Serial(PORT, BAUD_RATE, timeout=1)
time.sleep(2)
times  = []
values = []
start_time = time.time()
while time.time() - start_time < DURATION:
    line = arduino.readline().decode("utf-8", errors="ignore").strip()
    if line.isdigit():
        times.append(time.time() - start_time)
        values.append(int(line))
arduino.close()
plt.plot(times, values)
plt.xlabel("Time (s)")
plt.ylabel("Analog value")
plt.title("Potentiometer Reading Over Time")
plt.grid(True)
plt.show()