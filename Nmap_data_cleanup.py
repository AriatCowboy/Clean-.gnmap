file_name = "archetypes_nmapdata.gnmap"
file_name1 = "archetypes_nmapdata.nmap"

f = open(file_name)
f = f.readlines()
fsplit = f[0].split(' ')[5:][:5]

g = open(file_name1)
g = g.readlines()
gsplit = ""

date = "Date: "
for item in fsplit:
	date = date + item + " "
host_status= []
port_data_list = []
f.pop(0)
f.pop()
for item in f:
	if item.startswith('Host:'):
		addresses = item.split(" ")[1]
		data = item.split(":")[1]
		data = data.split(" ")[2][3:]
		if data.startswith('Status'):
			status = item.split(" ")[3]
		if not status.startswith("Host:"):
			status = "Host: {}\nStatus: {}\n".format(addresses, status)

		if data.startswith('Ports'):
			ports = item.split(":")
			ip = ports[1].split(" ")[1]
			num = len(ports)
			ports = ports[2:(num-3)]
			port_data = ports[0].split(",")
			for data in port_data:
				try:
					delete = data.split(';')
					if len(delete) > 1:
						delete.pop()
						port_data.pop()
						port_data.append(delete[0])
				except:
					pass
			for port in port_data:
				info = port.split('/')
				for i in range(10):
					try:
						info.remove('')
					except:
						pass
				port_num = info[0]
				port_status = info[1]
				port_type = info[2]
				if port_type == 'tcp':
					port_type = "TCP"
				if port_type == 'udp':
					port_type = "UDP"
				port_application = info[4]
				port_data_list.append("Port: {}\nStatus: {}\nType: {}\nApplication: {}\n\n".format(port_num,port_status,port_type,port_application))
		if not status in host_status:
			host_status.append(status)
print(date + "\n")
for item in host_status:
	print(item)
for item in port_data_list:
	print(item)