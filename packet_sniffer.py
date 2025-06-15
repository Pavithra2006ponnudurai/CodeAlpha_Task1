from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime
from colorama import Fore, Style, init
import os

# Initialize colorama
init(autoreset=True)

# Clear the screen
os.system('clear')

# Banner
banner = r"""
               
   ------------------Basic Network Packet Sniffer - Kali Linux-------------------------
  ____             _        _   _                   _             
 |  _ \ __ _ _ __ | | _____| \ | | ___  _   _ _ __ (_) ___  _ __  
 | |_) / _` | '_ \| |/ / _ \  \| |/ _ \| | | | '_ \| |/ _ \| '_ \ 
 |  __/ (_| | | | |   <  __/ |\  | (_) | |_| | | | | | (_) | | | |
 |_|   \__,_|_| |_|_|\_\___|_| \_|\___/ \__, |_| |_|_|\___/|_| |_|
                                       |___/                      
              Basic Network Packet Sniffer - Kali Linux                 
   
            AUTHOUR      :   PAVITHRA PONNUDURAI
            CREATED ON   :   15 JUNE 2025
"""
print(Fore.CYAN + banner + Style.RESET_ALL)

# Packet processing function
def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src_ip = ip_layer.src
        dst_ip = ip_layer.dst
        proto = ip_layer.proto
        timestamp = datetime.now().strftime('%H:%M:%S')

        log_line = f"[{timestamp}] Packet: {src_ip} --> {dst_ip} | Protocol: {proto}"

        if TCP in packet:
            log_line += f" | TCP Port: {packet[TCP].sport} -> {packet[TCP].dport}"
        elif UDP in packet:
            log_line += f" | UDP Port: {packet[UDP].sport} -> {packet[UDP].dport}"
        elif ICMP in packet:
            log_line += " | ICMP Packet"
        else:
            log_line += " | Other IP Packet"

        # Print with color
        print(Fore.GREEN + log_line)

        # Save to log file
        with open("packet_log.txt", "a") as log_file:
            log_file.write(log_line + "\n")

# Start sniffing
print(Fore.YELLOW + "\n[!] Starting packet capture... Press Ctrl+C to stop.\n")
sniff(prn=packet_callback, store=0)
