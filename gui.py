import tkinter as tk
from tkinter import ttk

# Function to toggle GPS
def toggle_gps():
    global gps_active
    gps_active = not gps_active
    print("GPS Active:", gps_active)
    button_text.set("Stop GPS" if gps_active else "Start GPS")

def update_data():
    # Simulate update wind direction and speed
    wind_direction.set("West")
    vehicle_speed.set("5 MPH")

    root.after(1000, update_data)

# Initialize GPS active state
gps_active = False

# GUI setup
def create_gui():
    global button_text, wind_direction, vehicle_speed, root
    root = tk.Tk()
    root.title("Smart Crop Spraying System")
    # Use ttk for modern look
    style = ttk.Style()
    style.configure('TButton', font=('Helvetica', 16), padding=10)

    button_text = tk.StringVar()
    button_text.set("Start GPS")

    button_text = tk.StringVar()
   