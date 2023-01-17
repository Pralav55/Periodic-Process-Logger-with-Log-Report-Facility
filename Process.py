#Importing required Header File
import os
import psutil 
import time 
import MailSender
from sys import *

#Function which creates file and write into file with content of running processes
def ProcessDisplay(log_dir = "CurrentProcess"):
    listprocess = []

    #creating folder on same file path
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass
    
    seperator = "-" * 80

    #Creating a file with a particular name
    log_path = os.path.join(log_dir , "ProcessLog%s.log" %(time.ctime()))
    
    #Opening the created file in write mode
    f = open(log_path,'w')

    #Writing content into the file
    f.write(seperator+"\n")
    f.write("Periodic Process Logger : "+time.ctime()+"\n")
    f.write(seperator+"\n")

    #Extracting running process like pid,name,username,vms into a list
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            vms = proc.memory_info().vms/ (1024 * 1024)
            pinfo['vms'] = vms
            listprocess.append(pinfo)
        except (psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess):
            pass

    #Writing the extracted list into the created file
    for element in listprocess:
        f.write("%s\n"%element)

    print("Process Log successfully created at %s"%(time.ctime()))

    #This method is used to check whether device is connected to internet or not
    connected = MailSender.is_connected()

    if connected:
        StartTime = time.time()

        #Calling Mail sender method which sends the mail with attachment
        MailSender.MailSender(log_path,time.ctime())
        
        EndTime = time.time()

        print("Took %s seconds to send mail"%(EndTime-StartTime))
        print("------------------------------------------------------------------")

    else:
        print("There is no internet connection")
        print("------------------------------------------------------------------")

