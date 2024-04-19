# UBNT_EdgeSwitch-TurnON-OFF
Code is to help run an automated script through task scheduler to turn switch ports on or off for Ubiquiti Edgeswitch or similar switches

Make sure you have python downloaded or the script will not run correctly

To set the program to run automatically you will have to keep a computer on it's network on or adjust Task Scheduler settings as neccessary

Instructions:
1. Open up the task scheduler. 
2. Create a New Task with it's trigger being a specified time. 
3. Next make the condition 'Start a Program' with the program script as C:\Users\*Your User*\AppData\Local\Microsoft\WindowsApps\python.exe
4. Add in the 'Add Arguments' value put the program name. Ex.'EdgeSwitchTurnOff.py' or other
5. Add the location of the py file in the 'Start In' value. Ex. C:\Users\*Your User*\Documents 
