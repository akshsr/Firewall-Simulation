#!/bin/python3 

import socket
import time
import logging
import random
import threading

logging.basicConfig(filename="blocked_packets.log", level=logging.INFO, format="%(asctime)s - %(message)s")

firewall_rules = {
    "ip": set(),  
    "ports": set(),  
    "protocols": set()  
}

class Packet:
    def __init__(self, source_ip, dest_ip, port, protocol):
        self.source_ip = source_ip
        self.dest_ip = dest_ip
        self.port = port
        self.protocol = protocol  

def add_block_rule(rule_type, rule_value):
    if rule_type == "ip":
        firewall_rules["ip"].add(rule_value)
        print(f"Blocked IP address: {rule_value}")
    elif rule_type == "port":
        firewall_rules["ports"].add(int(rule_value))
        print(f"Blocked port: {rule_value}")
    elif rule_type == "protocol":
        firewall_rules["protocols"].add(rule_value)
        print(f"Blocked protocol: {rule_value}")
    else:
        print(f"Invalid rule type: {rule_type}")

def remove_block_rule(rule_type, rule_value):
    if rule_type == "ip" and rule_value in firewall_rules["ip"]:
        firewall_rules["ip"].remove(rule_value)
        print(f"Unblocked IP address: {rule_value}")
    elif rule_type == "port" and int(rule_value) in firewall_rules["ports"]:
        firewall_rules["ports"].remove(int(rule_value))
        print(f"Unblocked port: {rule_value}")
    elif rule_type == "protocol" and rule_value in firewall_rules["protocols"]:
        firewall_rules["protocols"].remove(rule_value)
        print(f"Unblocked protocol: {rule_value}")
    else:
        print(f"Rule not found: {rule_type} - {rule_value}")

def log_blocked_packet(packet, reason):
    logging.info(f"Blocked Packet - Source: {packet.source_ip}, Destination: {packet.dest_ip}, Port: {packet.port}, Protocol: {packet.protocol}, Reason: {reason}")

def packet_handler(packet):
    if packet.source_ip in firewall_rules["ip"]:
        log_blocked_packet(packet, "Blocked source IP")
        return  # Block the packet
    
    if packet.dest_ip in firewall_rules["ip"]:
        log_blocked_packet(packet, "Blocked destination IP")
        return  # Block the packet
    
    if packet.port in firewall_rules["ports"]:
        log_blocked_packet(packet, f"Blocked port {packet.port}")
        return  # Block the packet
    
    if packet.protocol in firewall_rules["protocols"]:
        log_blocked_packet(packet, f"Blocked protocol {packet.protocol}")
        return  # Block the packet
    
    print(f"Allowing packet - Source: {packet.source_ip}, Destination: {packet.dest_ip}, Port: {packet.port}, Protocol: {packet.protocol}")

def simulate_network_traffic():
    while True:
        source_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        dest_ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
        port = random.randint(1, 65535)
        protocol = random.choice(["TCP", "UDP"])


        packet = Packet(source_ip, dest_ip, port, protocol)
        

        packet_handler(packet)


        time.sleep(1)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", 8080)) 
    server_socket.listen(5)

    print("Server started on port 8080. Waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        client_socket.close()

def start_simulation():
    traffic_thread = threading.Thread(target=simulate_network_traffic)
    traffic_thread.daemon = True
    traffic_thread.start()

    server_thread = threading.Thread(target=start_server)
    server_thread.daemon = True
    server_thread.start()

    while True:
        time.sleep(1)

if __name__ == "__main__":
    add_block_rule("ip", "192.168.1.100")
    add_block_rule("port", 8080)
    add_block_rule("protocol", "TCP")
    
    start_simulation()

    time.sleep(10)  
    remove_block_rule("ip", "192.168.1.100")
    remove_block_rule("port", 8080)
    remove_block_rule("protocol", "TCP")
