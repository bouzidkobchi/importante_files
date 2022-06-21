# in this file i choose my most importants codes that i found and use it ( part1 ):
# --------------------------------------------------------------------------------------------------------------------------------------
# 1 - open or choose file or files or even directory with  OS GUI
from tkinter import  filedialog as fd
file = fd.askopenfilename()     #  \
files = fd.askopenfilenames()   #   | => string path (adress in system)
directory = fd.askdirectory()   #  /
# --------------------------------------------------------------------------------------------------------------------------------------
# 2 - run python code (string) in python
exec(compile('print(5)','sumstring','exec'))        # you can add text file just read parameteres BRO
# --------------------------------------------------------------------------------------------------------------------------------------
# 3 - copy and paste 
import pyperclip
pyperclip.copy('done')                              #string you want to make it copied to clipboard
text = pyperclip.paste()
# --------------------------------------------------------------------------------------------------------------------------------------
# 4 - ALLO terminal (command line)
    # your request
import os
os.system('command')                                # if you want to shutdown your pc write 'shutdown /s'
    # its answer 
import subprocess
print(subprocess.check_output('command'))
# --------------------------------------------------------------------------------------------------------------------------------------
# 5 - auto keyboard & free mouse
    # keyboard and mouse control 
import pyautogui
pyautogui.press('keyboard key')                      # like 'a' , 'enter' , 'alt'     # you can see also :  pyautogui.click()
pyautogui.hotkey('alt' ,'f4')                        # for multiple keys in one time (alt + f4 = out the current app)
pyautogui.moveTo(x = 100  , y = 200, duration=3)     # to change mouse cursor position (in pixel)
pyautogui.dragTo (x = 100  , y = 200 , duration=2)   # to change mouse cursor position + press in time 
pyautogui.write('your string BRO (^_^) ')
pyautogui.rightClick()    # \
pyautogui.leftClick()     #  | => their names represent their functions
pyautogui.doubleClick()   # /

import keyboard
keyboard.record(until='choosen key')                 # recording pressed keys until choosen key be pressed
keyboard.wait('choosen key')                         # waiting user to press choosen key
    # mouse position in easy way (changing automatically)
from mouseinfo import mouseInfo
mouseInfo()
# --------------------------------------------------------------------------------------------------------------------------------------
# 6 - working with files & directories in system
# --------------------------------------------------------------------------------------------------------------------------------------
os.remove('file path')                               # to remove single file
os.rmdir('folder path')                              # to remove directory
os.getcwd()                                          # to get the currrent working directory
os.chdir('the new path')                             # to change working directory 
os.listdir('the folder path')                        # return the folder element in list
os.mkdir('folder name | path + name in')             # to make a single folder where you choose 
# --------------------------------------------------------------------------------------------------------------------------------------
# 7 - types of hashing that i now until now :
# --------------------------------------------------------------------------------------------------------------------------------------
text = 'something'
from hashlib import sha1 , sha224 , sha256 ,sha384, sha3_224, sha3_256, sha3_384, sha3_512 ,sha512 , md5 
encrypted_text = md5(text.encode())              # 32 baytes
encrypted_text = sha1(text.encode())             # 40 baytes
encrypted_text = sha3_224(text.encode())         # 56 baytes
encrypted_text = sha3_256(text.encode())         # 64 baytes
encrypted_text = sha3_384(text.encode())         # 96 baytes
encrypted_text = sha3_512(text.encode())         # 128 baytes
encrypted_text = sha224(text.encode())           # 224 baytes
encrypted_text = sha256(text.encode())           # 256 baytes
encrypted_text = sha384(text.encode())           # 384 baytes
encrypted_text = sha512(text.encode())           # 512 baytes
# hash result ( change code before execute )
print("its hash is : ",encrypted_text.hexdigest())
# --------------------------------------------------------------------------------------------------------------------------------------
# 8 - Hardware info :
# --------------------------------------------------------------------------------------------------------------------------------------
import psutil
import platform
from datetime import datetime
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")
print("="*40, "Boot Time", "="*40)
boot_time_timestamp = psutil.boot_time()
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
print("Total cores:", psutil.cpu_count(logical=True))
# CPU frequencies
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
# CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
# Memory Information
print("="*40, "Memory Information", "="*40)
# get the memory details
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
# get the swap memory details (if exists)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")
# Disk Information
print("="*40, "Disk Information", "="*40)
print("Partitions and Usage:")
# get all disk partitions
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")
# Network information
print("="*40, "Network Information", "="*40)
# get all network interfaces (virtual and physical)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
# get IO statistics since boot
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
# --------------------------------------------------------------------------------------------------------------------------------------
# 9 - functions with memory using decorator ( make your performance UP ) :
dict1 = {}                                                      # dictionary { n : func(n) }
def MyCash (func) :                                         # \    x
    def fun(n):                                             #  \
        global dict1                                        #   \
        if n not in dict1 :                                 #    | => MyCash decorator
            dict1[n] = func(n)                              #   /
        return dict1[n]                                     #  /
    return fun                                              #/

@MyCash
def fib_with_cash(n):                                           # fibanocci function as example
    if n==0 or n==1 :
        return 1
    else : return fib_with_cash(n-1) + fib_with_cash(n-2)
def fib(n):
    if n==0 or n==1 :
        return 1
    else : return fib(n-1) + fib(n-2)
print(fib_with_cash(200))                                                   
# print(fib(200))                                                # please don't open this hash it's take a lot of time to excute
print('*'*50)
for i in dict1 :
    print(f'{i} : {dict1[i]}')                                   # if you want to see dictionary values
# --------------------------------------------------------------------------------------------------------------------------------------
# 10- complex list to one dimension list :
my_list = [1,[2,3,4,5,6],7,[8],[9,[10,11,[12,13,[14,[15],16]],17],18],19] # to [1,2,3,4,5,6,7,8,9,10 ... ]
items = []
def find(element) :
    global items
    if type(element) is not list :
        items.append(element)
    else :
        for i in element :
            find(i)
    return items
print(find(my_list))