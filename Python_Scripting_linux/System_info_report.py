#first create directory by using => mkdir directoryuname
#second go in the directory by using => cd nameofdirectory which has been created
#Third use any text editor like => nano andfilename.py
#fourth =>Write script inside that file



#!/usr/bin/env python3
import platform
import psutil
#platform and psutil are library required for work with system script

#platform =>it is used for retrieve the name and version and when that was release this info like any system linux etc

#psutil => it is used for getting the memory cpu and cors info 

print("os : ",platform.system(),platform.release())
print("cpu cors :",psutil.cpu_count(logical=True))
print("Memory(Gb) :",round(psutil.virtual_memory().total/(1014**3),2))
print("Disk usage :")
for part in psutil.disk_partitions():
    usage=psutil.disk_usage(part.mountpoint)
    print(f"{part.mountpoint}-{usage.percent}% used")
    
#each line explanation
#platform.system() =>used for retrieve name of os
#platform.release() => is used to retrieve the data when that will be released
#psutil.cpu_count()=> it retrieves the numbers of coures which are in cpu
#logical=True => it is used for logical cores which retrieve the logical cores number in cpu logical cores is nothing but it was the that coures which make the physical core can handel multiple cores which cpu has multiple cores that cpu has done the multiple task parallealy 
#more cores ore performance
#for development used more then 8 cores 
#for gaming used 3-5 cores 
# for crome and  notepad likes used 2 or more cores

#psutil.virtual_memory()=> it return the memory in kb kilobytes
#.total means it will return all the total memory
#/ by 1024**3 used for convert thet memory into the gb gigabytem
#round for the 2 decimal points

#loop for diskusage part => mens is is a part which is partitions of cpu and the psutil.disk_partitions => it retereve all the partitions parts of disk 
#psutil.disk_usage()=> it return all usage part and par.mountpart which wil return the mounted means path of the part full path
#part.mountpoint - usage.percent means uaage storage minus the actual storage it will return the free space and usage storage 
