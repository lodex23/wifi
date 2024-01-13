import subprocess
import os

def get_ssids(interface):
    try:
        # Kill any processes that might interfere
        subprocess.run(['airmon-ng', 'check', 'kill'])

        # Start the monitor mode
        subprocess.run(['airmon-ng', 'start', interface])

        # Stop NetworkManager (if running)
        subprocess.run(['sudo', 'systemctl', 'stop', 'NetworkManager'])

        # Run airodump-ng to scan for SSIDs in the background
        airodump_process = subprocess.Popen(['airodump-ng', interface])

        # Wait for user input to stop the process
        input("Press Enter to stop scanning...")

        # Terminate the airodump-ng process
        airodump_process.terminate()

    except Exception as e:
        print(f"An error occurred: {e}")

def capture_handshake(interface, output_file, target_bssid=None, channel=None):
    if not target_bssid:
        target_bssid = input("Enter the target BSSID (MAC address): ")

    if not channel:
        channel = input("Enter the channel of the target network: ")

    print(f"Capturing handshake on {interface} for {target_bssid} on channel {channel}...")

    try:
        # Start airodump-ng to capture the handshake
        subprocess.run(['airodump-ng', '--bssid', target_bssid, '-c', channel, '--write', output_file, interface])

        print("Handshake captured!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    interface = "wlx1cbfceba6bcb"

    # Run get_ssids to scan for available SSIDs
    get_ssids(interface)

    # Capture handshake with specified BSSID, channel, and output file
    target_bssid = input("Enter the target BSSID (MAC address): ")
    channel = input("Enter the channel of the target network: ")
    output_file = input("Enter the output file path for the handshake capture: ")

    # Run the capture_handshake function
    capture_handshake(interface=interface, target_bssid=target_bssid, output_file=output_file, channel=channel)
