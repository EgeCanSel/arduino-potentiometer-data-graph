# Arduino Potentiometer Data Graph

This project reads the analog value of a B10K potentiometer using an Arduino UNO and sends the data to a computer through serial communication.

## Hardware

- Arduino UNO
- B10K potentiometer
- Breadboard
- Jumper wires

## Wiring

- Potentiometer outer pin → 5V
- Potentiometer middle pin → A0
- Potentiometer other outer pin → GND

## Arduino

The Arduino reads the potentiometer value using `analogRead(A0)` and sends it through serial communication at 9600 baud.

## Data Processing

The serial data can be read and plotted using:

- Python
- MATLAB

Both scripts collect the potentiometer values for 30 seconds and plot them against time.

## Result

The project demonstrates analog data acquisition, serial communication, and time-based data visualization.
