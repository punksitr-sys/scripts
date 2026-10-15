#!/usr/bin/env python3
import re
import sys
# 1. Check if the user provided the file path argument
if len(sys.argv) < 2:
    print("Error: Please provide the path to the Nmap result file!")
    print("Usage: python3 get_ports.py <file_path> [delimiter]")
    sys.exit(1)
# 2. Get the file path from command line arguments
file_path = sys.argv[1]
# 3. Handle the delimiter, convert '\n' or '\t' strings into real control characters
delimiter = ","
if len(sys.argv) > 2:
    try:
        delimiter = sys.argv[2].encode('utf-8').decode('unicode_escape')
    except Exception:
        delimiter = sys.argv[2]
ports = []
try:
    # 4. Read the file and filter open ports
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            tcp_match = re.search(r"(\d+)/tcp\s+open", line)
            udp_match = re.search(r"(\d+)/udp\s+open", line)
            if tcp_match:
                ports.append(tcp_match.group(1))
            elif udp_match:
                ports.append(udp_match.group(1))
    
    # 5. Print the result using the processed delimiter
    if ports:
        print(delimiter.join(ports))
    else:
        print("No open TCP/UDP ports found in the file.")
except FileNotFoundError:
    print(f"Error: File '{file_path}' not found. Please check the path.")
