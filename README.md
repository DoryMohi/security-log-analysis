
# Security Log Analysis & Attack Detection

This security project analyzing web server logs to detect brute-force, SQL injection, and XSS attacks using defensive monitoring techniques.


## Overview
This project demonstrates a blue-team cybersecurity approach by analyzing web server access logs to detect suspicious and malicious activity. The goal is to simulate a basic Security Operations Center (SOC) workflow by identifying common web attacks through log analysis and generating security alerts.

All analysis was performed in a **local, controlled, and ethical environment** using simulated log data.

---

## Project Objectives
- Analyze web server access logs
- Detect common attack patterns
- Generate alerts for suspicious activity
- Demonstrate defensive (blue-team) security skills

---

## Attack Types Detected

### 1. Brute-Force Authentication Attempts
- Detection of repeated failed login attempts (`POST /login` with HTTP status `401`)
- Alerts triggered when multiple failures occur from the same IP address

---

### 2. SQL Injection Attempts
- Detection of common SQL injection patterns in URL parameters
- Examples include:
  - `' OR 1=1--`
  - `' OR 'a'='a`
  - SQL comment markers (`--`)

---

### 3. Cross-Site Scripting (XSS) Attempts
- Detection of JavaScript and HTML injection attempts
- Examples include:
  - `<script>` tags
  - `onerror` event handlers
  - `<img>` tag injection

---

## Tools & Technologies
- Python 3
- Regular Expressions (regex)
- Simulated Apache/Nginx-style access logs
- macOS
- Git & GitHub

---

## How It Works
1. Simulated web server access logs are stored in `logs/access.log`
2. A Python script parses each log entry
3. Rule-based detection logic identifies suspicious patterns
4. Alerts are generated indicating attack type and source IP

---

## Results
The detection script successfully identified:
- Brute-force login attempts
- SQL injection payloads
- Cross-site scripting attempts

Detected events are printed as security alerts in the terminal.

---

## Ethical Disclaimer
This project uses **simulated log data** only.  
No real systems, users, or production environments were involved.  
The project is intended strictly for **educational and demonstration purposes**.

---

## Skills Demonstrated
- Security log analysis
- Blue-team detection techniques
- Pattern-based attack detection
- Python scripting for security monitoring
- SOC-style alerting and reporting