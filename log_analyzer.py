import csv
import re
from collections import Counter

LOG_FILE = "server_access.log"

def analyze_logs():
    #Regex to extract IP address from failed attempt
    failed_pattern = re.compile(r"Failed login attempt.*from (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
    failed_ip_counter = Counter()

    print(f"[*] Reading the log file: {LOG_FILE}...")

    with open(LOG_FILE, "r") as file:
        for line in file:
            match = failed_pattern.search(line)
            if match:
                ip_address = match.group(1)
                failed_ip_counter[ip_address] += 1


