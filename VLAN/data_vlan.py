import os
import subprocess
import re
import json
def interface_vlan():
    cmd_bf = ['bridge', 'vlan', 'ciscoshow']
    proc = subprocess.Popen(cmd_bf, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    line_num = 0;

    while True:
        
        line = proc.stdout.readline()
        if not line:
            break
    #the real code does filtering here
        # print ("test:", line)
        line_temp = str(line)
        line_temp = line_temp.replace('\\t',' ')
        line_temp = line_temp.replace('\\n','')
        line_temp = line_temp.replace("'"," ")
        x = 'line%s'%(line_num)
        a_dictionary = {x: line_temp}
        with open("data_file.json", "r+") as file:
            data = json.load(file)
            data.update(a_dictionary)
            file.seek(0)
            json.dump(data, file)
        line_num = line_num + 1;
