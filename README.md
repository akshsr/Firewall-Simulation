# custom-firewall-simulation
Python script which simulate aka work as firewall 

Network Firewall Simulation with Packet Filtering
This Python script simulates a simple network firewall that filters incoming network packets based on user-defined rules. It blocks specific IP addresses, ports, or protocols, logs blocked packets to a file, and allows traffic that doesn't match any rule. The firewall also includes a simulated server that listens for incoming connections and a simulation of random network traffic for testing purposes.

Features
Packet Filtering: The firewall can block packets based on source IP, destination IP, port, and protocol (TCP/UDP).
Logging: All blocked packets are logged to a file (blocked_packets.log) with the reason for the block.
Real-time Traffic Simulation: Simulates random network traffic to test the firewall's functionality.
Dynamic Rule Management: You can add and remove block rules dynamically for testing purposes.
Requirements
Python 3.x
The script uses the socket, time, random, logging, and threading modules, which are part of the Python standard library.
