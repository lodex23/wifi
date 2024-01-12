import socket
import struct
import time
import os

def capture_handshake(interface, target_bssid):
    print(f"Capturing handshake on {interface} for {target_bssid}...")

    try:
        # Create a raw socket to sniff Wi-Fi frames
        raw_socket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.htons(0x0003))

        # Set the interface in promiscuous mode
        raw_socket.bind((interface, 0))

        # Start capturing frames
        start_time = time.time()
        handshake_captured = False

        while time.time() - start_time < 15:  # Capture frames for 15 seconds (adjust as needed)
            packet = raw_socket.recvfrom(2048)[0]

            # Extract BSSID from the 802.11 frame
            bssid = struct.unpack("!6s6s6s", packet[36:54])[2]

            if bssid == target_bssid.encode():
                print("Handshake captured!")
                handshake_captured = True
                break

        if not handshake_captured:
            print("Handshake not captured within the time limit.")

        # Close the socket
        raw_socket.close()

    except Exception as e:
        print(f"An error occurred: {e}")

def get_ssids():
    print("Scanning for available SSIDs...")

    try:
        result = os.popen("netsh wlan show networks mode=Bssid").read()
        ssids = [line.strip() for line in result.split('\n') if "SSID" in line]

        for ssid in ssids:
            print(f"SSID found: {ssid}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":

        get_ssids()

        ssid = input("Choose ssid: ")

        capture_handshake(interface="Wireless LAN adapter Wi-Fi", target_bssid=ssid)