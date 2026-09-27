clear;
clc;
port     = input("Type port name: ", "s");
baudRate = 9600;
durationSeconds = 30;
arduino         = serialport(port, baudRate);
configureTerminator(arduino, "LF");
flush(arduino);
times  = [];
values = [];
startTime = tic;
while toc(startTime) < durationSeconds
    line  = readline(arduino);
    value = str2double(line);
    if ~isnan(value)
        times(end + 1)  = toc(startTime);
        values(end + 1) = value;
    end
end
clear arduino;
plot(times, values, "LineWidth", 1.5);
xlabel("Time (s)");
ylabel("Analog value");
title("Potentiometer Reading Over Time");
grid on;