import socket
import sys
def main2():
	def main(host,ports):
		scan_range = []
		scan_results = []

		if '-' in ports:
			start_port, stop_port = ports.split('-')
			for port in range(int(start_port), int(stop_port)+1):
				scan_range.append(port)
		elif ',' in ports:
			for port in ports.split(','):
				port = int(port.strip())
				scan_range.append(port)
		else:
			scan_range.append(int(ports))
			scan_range.append(int(ports)+1)

		scan_range = check_ports(host, scan_range)

	def check_ports(host, ports):
		port_results = []
		for port in ports:
			try:
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				result = sock.connect_ex((host, port))
				if result == 0:
					print(f'{host} -> {port}: up')
					port_results.append((port, True))
				sock.close()
			except Exception as ex:
				print(f'{host} -> {port}: down')
				port_results.append((port, False))
		return port_results
	host = input("Enter Host. For eg [https://www.google.com or 142.250.181.68 ] : ")
	port_range = input("Enter the port range. For eg [1-10] : ")
	main(host, port_range)

