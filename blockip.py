import os
with open("/mlt3/blocked.txt","r") as file1:
	for i in file1:
		os.system('iptables -A INPUT -s {} -j DROP'.format(i.rstrip('\n')))
	os.system('service iptables save')
