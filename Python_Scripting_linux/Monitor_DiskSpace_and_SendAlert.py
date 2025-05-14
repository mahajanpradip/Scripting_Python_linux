import shutil

def checkDisk(thrashold=80):
    usage=shutil.disk_usage("/")
    percentUsed=(usage.used/usage.total)*100
    if percentUsed > thrashold :
        sendAlert(percentUsed)
    else:
        print(f"Disk is usage at {percentUsed:.2f}%")
        
def sendAlert(usage):
    print(f"ALERT Disk usage is high at {usage:.2f}%")
    
checkDisk()