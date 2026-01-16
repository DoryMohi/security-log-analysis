import re
from collections import defaultdict

LOG_FILE = "logs/access.log"

# Detection patterns
SQLI_PATTERNS = [
    r"(?i)or\s+1=1",
    r"(?i)'--",
    r"(?i)or\s+'a'='a"
]

XSS_PATTERNS = [
    r"<script>",
    r"onerror=",
    r"<img"
]

failed_logins = defaultdict(int)
alerts = []

with open(LOG_FILE, "r") as file:
    for line in file:
        if not line.strip():
            continue  # skip empty lines

        parts = line.split()
        if len(parts) < 1:
            continue

        ip = parts[0]

        # Detect brute-force login attempts
        if "POST /login" in line and "401" in line:
            failed_logins[ip] += 1
            if failed_logins[ip] == 5:
                alerts.append(f"[BRUTE FORCE] Possible brute-force attack from IP {ip}")

        # Detect SQL Injection
        for pattern in SQLI_PATTERNS:
            if re.search(pattern, line):
                alerts.append(f"[SQL INJECTION] Suspicious request from IP {ip}")

        # Detect XSS
        for pattern in XSS_PATTERNS:
            if re.search(pattern, line):
                alerts.append(f"[XSS] Suspicious request from IP {ip}")

# Print results
print("=== Security Alerts ===")
if alerts:
    for alert in alerts:
        print(alert)
else:
    print("No suspicious activity detected.")