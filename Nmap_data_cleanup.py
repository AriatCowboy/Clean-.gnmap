file_name = "archetypes_nmapdata.gnmap"
f = open(file_name)
f = f.readlines()
fsplit = f[0].split(' ')[5:][:5]
date = "Date: "
for item in fsplit:
	date = date + item + " "
host_status= []
port_data_list = []
host = ""
status = ""
port_data_list = []
all_data = []
f.pop(0)
f.pop()
for item in f:
	host = item.split(" ")[1]
	data = item.split(":")[1]
	data = data.split(" ")[2][3:]
	if data.startswith('Status'):
		status = [item.split(" ")[3].rstrip(), item.split(" ")[1].rstrip()]
		status = "Host: {}\nStatus: {}\n\n".format(status[1], status[0])
		continue
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
			port_data_list.append("	Port: {}\n	Status: {}\n 	Type: {}\n 	Application: {}\n\n".format(port_num,port_status,port_type,port_application))
	all_data.append((status, port_data_list))
print(date)
for i in range(len(all_data)):
	print(all_data[i][i])
	for item in all_data[i][1]:
		print(item)
