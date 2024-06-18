# Smart Crop Spraying System

## Overview

This project implements a smart crop spraying system using a Raspberry Pi, GPS module, wind sensor, and vehicle speed sensor. The system displays real-time data on a touchscreen GUI, showing wind direction, vehicle speed, and the field being sprayed with lines indicating the areas already covered.

## Features

- Real-time display of wind direction and vehicle speed
- Visualization of sprayed areas on a video feed
- Calculation and display of total distance traveled and number of runs
- Easy-to-use touchscreen interface

## Hardware Requirements

- Raspberry Pi 4 Model B (4GB)
- Official Raspberry Pi Power Supply (USB-C, 5.1V 3A)
- Raspberry Pi Camera Module V2
- Raspberry Pi 7-inch Touchscreen Display
- GPS Module (e.g., Adafruit Ultimate GPS HAT)
- Micro SD Card (32GB) with Raspberry Pi OS
- Case for Raspberry Pi 4
- Wind Sensor (e.g., Adafruit Anemometer/Wind Speed Sensor)
- Hall Effect Speed Sensor Module

## Software Requirements

- Python 3
- OpenCV
- gpsd and gps3
- RPi.GPIO
- Tkinter
- geopy

## Installation

### Step 1: Setting Up Raspberry Pi

1. **Install Raspbian OS**:
   - Download the latest version of Raspbian from the [official website](https://www.raspberrypi.org/downloads/raspberry-pi-os/).
   - Use a tool like Balena Etcher to write the image to your micro SD card.
   - Insert the SD card into your Raspberry Pi and power it on.

2. **Initial Configuration**:
   - Follow the on-screen instructions to configure your Raspberry Pi.
   - Enable SSH, VNC, and configure Wi-Fi settings as needed.

### Step 2: Update and Upgrade

Open a terminal and run the following commands to update your system:

```bash
sudo apt-get update
sudo apt-get upgrade
