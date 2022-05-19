#!/usr/bin/env python
import os
import subprocess
import re


#show vlan truoc khi config
def add_vlans():
	cmd_bf = ['bridge', 'vlan', 'ciscoshow']
	proc = subprocess.Popen(cmd_bf, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	o_bf, e_bf = proc.communicate()
	data_bf = str(o_bf)
	vlan_c = []
	data_bf = data_bf.replace('\\n','')
	data_bf = data_bf.replace('\\t',' ')
	data_bf = data_bf.replace('-','')
	arr_data = data_bf.split(' ')
	print('Vlan has been config:')
	# x = re.findall('vlan/[0-9][0-9]',data_bf)
	for i in arr_data:
		if re.findall('vlan',i):
				print(i)		
	num_vlan = []
	for i in arr_data:
		if re.findall('vlan',i):
			temp = re.sub(r'\D', "",i)
			num_vlan.append(int(temp))
	print(num_vlan)
	for i in num_vlan:
		command_del = '/usr/bin/clish -x /Klish-XML/ -c "enable network" -c "configure terminal" -c "no vlan %s"'%i
		os.system(str(command_del))
	print('Please enter the Vlan range you need to add( ex: 2-40): ')
	vlan1 = input('Enter value start: ')
	while  int(vlan1) <= 1:
		vlan1 = input("please reload enter value with value start > 1:")

	vlan2 = input('Enter value stop: ')
	while  int(vlan2) >= 4096:
		vlan2 = input("please reload enter value with value start < 4096:")
	for i in range(int(vlan1),int(vlan2)):	
		command = '/usr/bin/clish -x /Klish-XML/ -c "enable network" -c "configure terminal" -c "vlan %s"'%i
		os.system(str(command))

	#show vlan sau config
	cmd = ['bridge', 'vlan', 'ciscoshow']
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	o, e = proc.communicate()
	data = str(o)
	vlan_c = []
	data = data.replace('\\n','')
	data = data.replace('\\t',' ')
	data = data.replace('-','')
	arr_data = data.split(' ')
	print('Vlan current config:')
	# x = re.findall('vlan/[0-9][0-9]',data)
	for i in arr_data:
		if re.findall('vlan',i):
				print(i)

def add_vlan():
	cmd_bf = ['bridge', 'vlan', 'ciscoshow']
	proc = subprocess.Popen(cmd_bf, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	o_bf, e_bf = proc.communicate()
	data_bf = str(o_bf)
	vlan_c = []
	data_bf = data_bf.replace('\\n','')
	data_bf = data_bf.replace('\\t',' ')
	data_bf = data_bf.replace('-','')
	arr_data = data_bf.split(' ')
	print('Vlan has been config:')
	# x = re.findall('vlan/[0-9][0-9]',data_bf)
	for i in arr_data:
		if re.findall('vlan',i):
				print(i)		
	num_vlan = []
	for i in arr_data:
		if re.findall('vlan',i):
			temp = re.sub(r'\D', "",i)
			num_vlan.append(int(temp))
	print(num_vlan)

	print('Please enter the Vlan you need to add( ex: 2-40): ')
	vlan1 = input('Enter value vlan: ')
	while 1:
		check = 0;
		for vlan_tmp in num_vlan:
			if int(vlan_tmp) == int(vlan1):
				check = 1;
		if int(check) == 1:
			vlan1 =  input('the vlan value has been configured, please re-enter: ')
			
		else:
			break;

	command = '/usr/bin/clish -x /Klish-XML/ -c "enable network" -c "configure terminal" -c "vlan %s"'%vlan1
	os.system(str(command))
	#show vlan sau config
	cmd = ['bridge', 'vlan', 'ciscoshow']
	proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	o, e = proc.communicate()
	data = str(o)
	vlan_c = []
	data = data.replace('\\n','')
	data = data.replace('\\t',' ')
	data = data.replace('-','')
	arr_data = data.split(' ')
	print('Vlan current config:')
	# x = re.findall('vlan/[0-9][0-9]',data)
	for i in arr_data:
		if re.findall('vlan',i):
				print(i)
while 1:
	print("select 1 to add vlan")
	print("select 2 to add vlans ")
	print("select 0 break ")
	select = input("please selection: ")
	if int(select) == 1:
		print("add vlan")
		add_vlan()
	elif int(select) == 2:	
		print("add vlans")
		add_vlans()
	elif int(select) == 0:
		break;
	else:
		print("select 1 to add vlan")
		print("select 2 to add vlans ")
		print("select 0 break ")
		select = input("please select case above: ")	

	




