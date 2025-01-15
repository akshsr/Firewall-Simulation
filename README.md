# Firewall Simulation and Packet Blocking

This project simulates a simple firewall system that can block packets based on rules for IP addresses, ports, or protocols. The firewall logs all blocked packets and can dynamically modify the blocking rules at runtime.

## Features

- **Dynamic Packet Blocking**: Block packets based on IP address, port, or protocol.
- **Packet Logging**: All blocked packets are logged in a `blocked_packets.log` file.
- **Simulated Network Traffic**: Generates random traffic to simulate network conditions and test the firewall.
- **Simulated Server**: A basic server that listens on port 8080, simulating a real-world server environment.

## Requirements

- Python 3.x
- No external libraries required (standard Python libraries: `socket`, `random`, `time`, `logging`, `threading`)

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/akshsr/firewall-simulation.git
   cd firewall-simulation
