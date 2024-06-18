# Wind Direction sensor data
from gps3 import gps3

def get_wind_data(wind_direction):
    wind_direction.set("N")
   
# Vehicle speed sensor data
def get_vehicle_speed(vehicle_speed):
    gps_socket = gps3.GPSSocket()
    data_stream = gps3.DataStream()
    gps_socket.watch()

    for new_data in gps_socket:
        if new_data:
            data_stream.unpack(new_data)
            if hasattr(data_stream.TPV, 'speed'):
                speed = data_stream.TPV['speed'] * 2.23694
                vehicle_speed.set(f"{speed:.2f}mph")
                break
            else:
                vehicle_speed.set("N/A")