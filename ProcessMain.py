#Importing Required Python Libraries
import time
import Process
import schedule
from sys import *

#Execution of Program starts from main
def main():
    #Displays Header of Application
    print("--------------Python Automation and Machine Learning--------------")
    print("------------------------------------------------------------------")
    print(" Periodic Process Logger with Auto Scheduled Log Report Facility")
    print("------------------------------------------------------------------")
    print("\tApplication name : "+argv[0])

    #Condition for command line argument
    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()

    if(argv[1] == "-h" or argv[1] == "-H"):
        print("This script is used to record running processess with periodic execution")
        exit()
    
    if(argv[1] == "-u" or argv[1] == "-U"):
        print("Usage : Application_Name Periodic_Time_inMinutes")
        exit()

    #Periodic Process Logger and calling it after particular interval
    try:
        schedule.every(int(argv[1])).minutes.do(Process.ProcessDisplay)

        while(True):
            schedule.run_pending()
            time.sleep(1)
    
    #Handling Exception
    except ValueError:
        print("Error : Invalid datatype of input")
    except Exception:
        print("Error : Invalid Input")

#Application Starter
if __name__ == "__main__":
    main()
