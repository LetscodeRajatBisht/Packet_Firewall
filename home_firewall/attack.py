import sys, time
from scapy.all import Ether, IP, TCP, sendp

TARGET_IP = "192.168.x.x"  # Replace with the target IP address
INTERFACE = "eth0"  # Replace with your network interface
NUM_PACKETS_PER_IP = 45
INTERVAL_BETWEEN_IPS = 3  # in seconds
SOURCE_IPS = [f"10.0.0.{i}" for i in range(1, 17)]  # Generates a list of source IPs

def send_packets(target_ip, interface, num_packets, source_ip):
    packet = Ether() / IP(dst=target_ip, src=source_ip) / TCP()
    packet_count = 0

    while packet_count < num_packets:
        sendp(packet, iface=interface)
        packet_count += 1

if __name__ == "__main__":
    if sys.version_info[0] < 3:
        print("This script requires Python 3.")
        sys.exit(1)

    for source_ip in SOURCE_IPS:
        send_packets(TARGET_IP, INTERFACE, NUM_PACKETS_PER_IP, source_ip)
        time.sleep(INTERVAL_BETWEEN_IPS)
