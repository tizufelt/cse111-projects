import os
import sys
import subprocess
import platform
from datetime import datetime
from matplotlib import pyplot as plt

condition = True

def icmp(host):
    pinglist = []
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "3", host]
    return subprocess.call(command)


def if_linux(ipin, interin, db):
    file = open(db, 'a')
    interin = int(interin)
    y = []
    x = []
    parameter = '-c'
    while condition:
        ping = os.popen(f'ping {ipin} {parameter} 1')
        result = ping.readlines()
        if result == []:
            ms_result = float(0)
            c = str(ms_result)
            now = datetime.now()
            file.write(now.strftime('%H:%M:%S') + ' ' + c + '\n')
            y.insert(0, ms_result)
            x.insert(0, now.strftime('%H:%M:%S'))
            plt.title(f'Ping Monitor to {ipin}')
            plt.xlabel('Time')
            plt.ylabel('ms')
            plt.xticks(rotation=90)
            plt.yticks(rotation=45)
            plt.scatter(x, y, c='green')
            plt.pause(interin)
        else:
            msLine = result[-1].strip()
            split = msLine.split(' = ')[-1]
            ms_result = split.split('ms')[0]
            ms_result = ms_result.split('/')[0]
            if ms_result == '':
                ms_result = float(0)
                print('error')
            else:
                ms_result = float(ms_result)
            c = str(ms_result)
            now = datetime.now()
            file.write(now.strftime('%H:%M:%S') + ' ' + c + '\n')
            y.insert(0, ms_result)
            x.insert(0, now.strftime('%H:%M:%S'))
            plt.title(f'Ping Monitor to {ipin}')
            plt.xlabel('Time')
            plt.ylabel('ms')
            plt.xticks(rotation=90)
            plt.yticks(rotation=45)
            plt.scatter(x, y, c='green')
            plt.pause(interin)
    file.close()

def if_windows(ipin, interin, db):
    file = open(db, 'a')
    interin = int(interin)
    y = []
    x = []
    parameter = '-n'
    while condition:
        ping = os.popen(f'ping {ipin} {parameter} 1')
        result = ping.readlines()
        msLine = result[-1].strip()
        split = msLine.split(' = ')[-1]
        ms_result = split.split('ms')[0]
        if ms_result == '1 (100% loss),':
            ms_result = 0
        if ms_result == '0 (0% loss),':
            ms_result = 0
        ms_result = float(ms_result)
        c = str(ms_result)
        now = datetime.now()
        file.write(now.strftime('%H:%M:%S') + ' ' + c + '\n')
        y.insert(1, ms_result)
        x.insert(1, now.strftime('%H:%M:%S'))
        plt.xlabel('Time')
        plt.ylabel('ms')
        plt.title(f'Ping Monitor to {ipin}')
        plt.xticks(rotation=90)
        plt.yticks(rotation=45)
        plt.scatter(x, y, c='green')
        plt.pause(interin)
    file.close()

def main():
    icmp(host = "google.com") 
    print()
    db = input("Enter Database name:")
    print()
    db = db + ".txt"
    file_path = str(db)
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print('Build a DataBase: ' + db)
        print()
        print('The computer`s operating system is:', sys.platform)
        print('#### For stop pinging press CTRL+C ####')
        print()
        ip = input('Enter ip address to ping:')
        inter = input('time to interval:')
        if sys.platform == 'darwin' or 'linux':
            if_linux(ip, inter, db)
        if sys.platform == 'windows' or 'win32':
            if_windows(ip, inter, db)
    
        plt.show()
    
if __name__ == "__main__":
    main()