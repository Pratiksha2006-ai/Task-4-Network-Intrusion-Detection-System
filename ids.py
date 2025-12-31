import socket
import time

print("Network Intrusion Detection System Started...")
print("Monitoring network traffic...\n")

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("127.0.0.1", 9999))

suspicious_count = 0

while True:
    data, addr = s.recvfrom(1024)
    message = data.decode()

    print(f"Packet received from {addr}: {message}")

    if "attack" in message.lower() or "malware" in message.lower():
        suspicious_count += 1
        print("⚠️ ALERT: Suspicious activity detected!")

    if suspicious_count >= 3:
        print("\n🚨 INTRUSION DETECTED!")
        print("Response: Blocking source temporarily.\n")
        suspicious_count = 0

    time.sleep(1)
