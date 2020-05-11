# Raspberry Pi TCP Infrared Motion Detection
## Description
This is the repository of a Python application built for Raspberry Pi which detects motion using the *HC-SR501 Passive Infrared (PIR) Motion Sensor* and sends the signal to a client application using TCP protocol.

## Hardware Setup
Please refer to [the sensor datasheet](./docs/hc_sr501_pir_motion_sensor_datasheet.pdf) and [the Raspberry Pi GPIO pinout diagram](./docs/raspberry_pi_gpio_pinout_diagram.png) before proceeding.
* Connect `+Power` pin of the sensor to a `5V power` pin of Raspberry Pi.
* Connect `GND` pin of the sensor to a `Ground` pin of Raspberry Pi.
* Connect `High / Low Output` pin of the sensor to the `GPIO 23` pin of Raspberry Pi.

## Demo Video
* [[YouTube] Raspberry Pi TCP Infrared Motion Detection with Unity](https://youtu.be/_uFyIu8G5lA)

## Contributor
* [phogbinh](https://github.com/phogbinh)

## Reference
The author refers to the following article to implement the program:
* [HC-SR501 PIR motion sensor on Raspberry Pi
](https://www.freva.com/2019/05/21/hc-sr501-pir-motion-sensor-on-raspberry-pi/)