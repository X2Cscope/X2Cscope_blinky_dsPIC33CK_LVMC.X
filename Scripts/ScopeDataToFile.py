#Prepared for dsPIC33CK256MP508_MCLV2.X demo
#Set-up of the scope, sample, then write the result data to a file in csv format
from threading import Timer
import time
import sys
import os
from org.netbeans.api.project.ui import OpenProjects;

#ASCII console color codes
RED = "\033[31m"
GREEN = "\033[32m"
DEFAULT = "\033[0m"

print "###########################"
print "Write scope data to a file"
print "###########################"


print "Setup scope\n"
x2c_scope.clearTrigger()
x2c_scope.clearChannelConfigs()
#set sample time to 50us
x2c_scope.setSampleTime(0.00005) 

x2c_scope.setChannelConfig(1, "myStruct.sinus", 1, 0)
x2c_scope.setChannelConfig(2, "myStruct.rad", 1, 0)
x2c_scope.sample(False) #false-> non blocking
		
print "Wait for scope sample finish"
while not x2c_scope.isSampleComplete():
	time.sleep(0.1)

x2c_scope.uploadData()

data = x2c_scope.getData()

for i in range(len(data)):
    print data[i]
print type(data[0])

#Use netbeans APIs to get and set project environment
prj = OpenProjects.getDefault().getMainProject()
prjDir = prj.getProjectDirectory().getPath() 
try :
    print prjDir
except:
    print RED + "Set as Main project"
    
os.chdir(prjDir) # change working dir to the project
print os.getcwd()

#Create the file and write data 
f = open('newfile3.csv','w')
for i in range(len(data[i])): # For all channel
    for n in range(len(data)):# For all data point in the selected channel
        f.write(str(data[n][i]) + ",") # separate the data points
    f.write("\n")# new line for channels
f.close()
