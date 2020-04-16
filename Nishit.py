###Code###
def Regexr(log_file_name):
	Port = []
	Name = []
	Status = []
	Vlan = []
	Duplex = []
	Speed = []
	Type = []
	hostname = ""
	import re
	Open_File = open('log_file_name', 'r')
	Read_File = Open_File.readlines()
	for x in Read_File:
		Temp = re.search("^([\w\/]+)\s+(.{19})(\w+)\s+(.{1,5})\s+(.{6})\s+(.{4,6}\s)(.{5,14})", x)
		Port.append(Temp.group(1))
		Name.append(Temp.group(2).strip())
		Status.append(Temp.group(3))
		Vlan.append(Temp.group(4).strip())
		Duplex.append(Temp.group(5).strip())
		Speed.append(Temp.group(6).strip())
		Type.append(Temp.group(7))
	#print(Port)
	#print(Name)
	#print(Status)
	#print(Vlan)
	#print(Duplex)
	#print(Speed)
	#print(Type)
	Open_File.close()
	return(Port, Name, Status, Vlan, Duplex, Speed, Type, hostname)
