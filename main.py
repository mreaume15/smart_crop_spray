import cv2
import time 
from threading import Thread
import tkinter as tk 
from tkinter import ttk
from sensors import get_wind_data, get_vehicle_speed
from geopy.distance import geodesic 
import gps

### Function to toggle GPS ###
def toggle_gps():
    global gps_active, run_start_coords, total_distance, total_runs_label
    gps_active = not gps_active
    if gps_active:
        run_start_coords = get_gps_coordinates()
        print("GPS Active:", gps_active)
    else:
        # Calculate the distance for this run
        run_end_coords = get_gps_coordinates()
        print(f"GPS stopped at: {run_end_coords}")
        if run_start_coords and run_end_coords:
            run_distance = geodesic(run_start_coords, run_end_coords).meters
            total_distance += run_distance
            total_runs += 1
            run_distance_var.set(f"Last Run: {run_distance:.2f} meters")
            total_distance_var.set(f"Total Distance: {total_distance:.2f} meters")
            total_runs_var.set(f"Total Runs: {total_runs}")
            print(f"Run distance: {run_distance:.2f} meters")
            print(f"Total distance: {total_distance:.2f} meters")
            print(f"Total runs: {total_runs}")
    button_text.set("Stop Spray" if gps_active else "Start Spray")
    print("GPS Active:", gps_active)


### Function to update data ###
def update_data():
    get_wind_data(wind_direction)
    get_vehicle_speed(vehicle_speed)
    root.after(1000, update_data)

### Initiazlize GPS active state ###
gps_active = False
run_start_coords = None
total_distance = 0.0
total_runs = 0

### GUI Setup ###
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
    button_text.set("Start GPS")

    butoon = ttk.Button(root, textvariable=button_text, command=toggle_gps, width=20)
    butoon.pack(pady=20)

    # Wind Direction Label
    wind_direction_label = ttk.Label(root, text="Wind Direction:", font=('Helvetica, 16'))
    wind_direction_label.place(x=20, y=60)

    wind_direction = tk.StringVar()
    wind_direction_value = ttk.Label(root, textvariable=wind_direction, font=('Helvetica', 16))
    wind_direction_value.place(x=20, y=60)

    # Vehicle Speed Label
    vehicle_speed_label = ttk.Label(root, text="Vehicle Speed (mph):", font=('Helvetica', 16))
    vehicle_speed_label.place(x=600, y=20)

    vehicle_speed = tk.StringVar()
    vehicle_speed_value = ttk.Label(root, textvariable=vehicle_speed, font=('Helvetica', 16))
    vehicle_speed_value.place(x=600, y=60)

    # Add a new section for run and distance information 
    run_distance_var = tk.StringVar()
    run_distance_label = ttk.Label(root, textvariable=run_distance_var, font=('Helvetica', 16))
    run_distance_label.place(x=20, y=120)
    print("Run distance label created")

    total_distance_var = tk.StringVar()
    total_distance_label = ttk.Label(root, textvariable=total_distance_var, font=('Helvetica', 16))
    total_distance_label.place(x=20, y=160) 
    print("total distance label created")

    total_runs_var = tk.StringVar()
    total_runs_label = ttk.Label(root, textvariable=total_runs_var, font=('Helvetica', 16))
    total_runs_label.place(x=20, y=200)
    print("Total Runs label created")

    root.geometry("800x480")  # Adjust based on your screen resolution
    root.mainloop()

# Function to draw lines on video feed
    def dra