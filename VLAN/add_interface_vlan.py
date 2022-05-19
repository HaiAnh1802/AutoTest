import os
import subprocess
import re


while 1:
    print('enter 1 to Add vlan for interface')
    print('enter 0 to exit')
    choose = input('choose: ')
    
    if int(choose) == 1:
        print('Add vlan for interface:')
        inf = input('Enter the interface you want to add vlan: ')

        #check vlan
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
        for i in arr_data:
            if re.findall('vlan',i):
                print(i)
        num_vlan = []
        for i in arr_data:
            if re.findall('vlan',i):
                temp = re.sub(r'\D', "",i)
                num_vlan.append(int(temp))
        print("vlan was config:" + str(num_vlan))

        vlan =  input('Enter the vlan you want to add interface: ')
        while 1:
            check = 0;
            for vlan_tmp in num_vlan:
                if int(vlan_tmp) == int(vlan):
                    check = 1;
            if int(check) == 1:
                break;
            else:
                vlan =  input('please enter value vlan was config: ')
        cmd1 = '/usr/bin/clish -x /Klish-XML/ -c "enable network" -c "configure terminal" -c "interface ethernet %s" -c "switchport mode access" -c "switchport access vlan %s" '%(inf,vlan)
        print(cmd1)
        os.system(str(cmd1))
        # check interface vlan

        cmd_bf = ['bridge', 'vlan', 'ciscoshow']
        proc = subprocess.Popen(cmd_bf, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        line_num = 0;
        interface = []
        count = int(0)
        while True:
            line = proc.stdout.readline()
            if not line:
                break
            line_temp = str(line)
            line_temp = line_temp.replace('\\t',' ')
            line_temp = line_temp.replace('\\n','')
            line_temp = line_temp.replace("'"," ")
            line_temp = line_temp.replace(","," ")
            vlan_temp = 'vlan%s'%(vlan)
            if re.findall(vlan_temp,line_temp):
                temp = line_temp
        check_vlan = str(temp).split(' ')
        print(check_vlan)
        for i in check_vlan:
            if(str(i) == str(inf)):
                count = count + 1
        if count == 0:
            print('FALSE')
        else:
            print('PASSED')

    elif int(choose) == 0:
        break
    else:
        print('please choose 1 or 0')
