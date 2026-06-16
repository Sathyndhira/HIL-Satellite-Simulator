# HIL-Satellite-Simulator
A Satellite Simulator which simulates battery levels of a satellite and a physical LED shows whether it's in low power mode or not.

I built a Hardware-in-the-Lop (HIL) testing setup that bridges a physical Arduino UNO (which is similar to that of a flight computer) with a Python script/simulation running in VS Code (which is similar to that of an orbital environment).

Instead of running standard software math, my script simulates a 24-hour day cycle, if it's day, battery levels will recharge a bit, and if it's night, batter is continuosly drained. This information is sent down a 9600 baud serial connection to the Arudino UNO, which parses the info in real time. If the simulation records battery levels below 50%, the Arduino engages Safe Mode, and turns on a physical LED on my desk, and tells the simulation to change power consumtion from 5.0A to 1.5A.

During development, I had to debug a serial timeout issue where the Arduino misread data gaps as 0% battery. I fixed this by adding a boundary check in the Arduino IDE to ensure it only used positive integers.

This projects allowd me to practice systems engineering, serial communication via pySerial, and embeded C++ logic (the Arduino language is similar to C++) using the exact testing methodologies used by SpaceX and NASA.
