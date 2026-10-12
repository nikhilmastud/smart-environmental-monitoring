# Smart Environmental Monitoring & Data Logging System

A beginner-friendly Arduino project that reads temperature and humidity, prints CSV-formatted records, and validates saved readings with Python.

## Features
- Read temperature and humidity from an Arduino Uno + DHT22 sensor.
- Print readings as `elapsed_ms,temperature_c,humidity_pct`.
- Save readings as CSV and validate the file structure with Python.
- Provide sample data for testing the workflow. Sample records below are illustrative, not physical measurements.

## Hardware
- Arduino Uno, DHT22 sensor/module, jumper wires, USB cable.
- To simulate first, use https://wokwi.com/ and add an Arduino Uno and DHT22.
- Connect VCC to 5V, DATA/SDA to D2, GND to GND; leave NC unconnected. Confirm labels for the component you add.

## Arduino setup
Install the Adafruit DHT sensor library and its required dependency using Arduino Library Manager (or Wokwi Library Manager). Open `arduino/smart_environment_monitor.ino`, upload it, then open Serial Monitor at 9600 baud.

## Save and validate readings
Copy Serial Monitor output into `data/sensor_data.csv`, retaining the header. From this repository root, run:

```bash
python python/validate_sensor_data.py data/sensor_data.csv
```

The script checks required columns, numeric values, non-negative elapsed time, temperature range (-40 to 80 C), and humidity range (0 to 100%).

## Limitations
This is a learning project, not a calibrated or safety-critical measurement instrument. Sensor accuracy depends on the hardware and environment.
