# 🕵️‍♀️ Basic Network Packet Sniffer - Kali Linux

This is a simple Python-based network packet sniffer developed using the `scapy` library on Kali Linux. It captures and displays packet-level details like source and destination IPs, ports, and protocol types.

---

## 📌 Features
- Captures real-time packets
- Supports TCP, UDP, and ICMP
- Displays IP addresses, ports, and protocols
- ASCII banner for branding
- Author and timestamp display

---

## 💻 Technologies Used
- Python 3
- Scapy
- Linux Terminal (Tested on Kali Linux)


## 🛠️ Installation & Usage

### 1. Clone the repo

```bash
git clone https://github.com/Pavithra2006Ponnudurai/CodeAlpha_Task1.git
cd packet-sniffer
```

---

### 2. Install requirements

> This tool uses `scapy`. You can install it via pip:

```bash
sudo apt update
sudo apt install python3-pip -y
pip3 install scapy
```

---

### 3. Run the Packet Sniffer

```bash
sudo python3 packet_sniffer.py
```

> 🔒 Use `sudo` to allow access to network interfaces.

---

### 📄 Sample Output

```
[+] Packet: 192.168.243.128 --> 192.168.243.2 | Protocol: 17 | UDP Port: 45926 -> 53
[+] Packet: 34.36.137.203 --> 192.168.243.128 | Protocol: 6 | TCP Port: 443 -> 50112
```
## 🧑‍💻 Author
**Pavithra Ponnudurai**  
*Created on: 15 June 2025*

---

## 📜 License
This project is licensed under the MIT License.
