Project Title: Port Scanner Using Python

 Objective
To develop a tool that scans a host or IP range to detect open, closed, or filtered ports, and optionally identify the services running on them. It helps in:

Network troubleshooting

Vulnerability assessment

Learning TCP/IP networking and security

Key Components
1. Target Input
Accept a single IP address or domain name

Optionally allow a range of IPs or ports

2. Port Scanning Logic
Try to connect to each specified port on the target using TCP (or UDP for advanced scanners)

Based on the response, categorize ports as:

Open

Closed

Filtered (e.g., blocked by a firewall)

3. Service Detection (Optional)
Attempt to grab banners from open ports to identify running services

Example: detect if port 80 is running an HTTP server

4. Reporting
Display or save the scan results

Learning Outcomes
Socket programming

TCP/IP protocol basics

Network enumeration

Ethical hacking foundations
