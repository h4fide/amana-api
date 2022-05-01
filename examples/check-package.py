from example.api import TrackerApi
import time
import os
trackingnumber = 'TRACKING_CODE_HERE'

storing_file = '.storing.dat'
if TrackerApi.getLastStatut(trackingnumber) == 'Missing':
    print("Your Package Is Not Registerd In The System Yet\nScript Continue Checking!")

with open(storing_file, 'r') as file:
    current_data = file.read()

def currentdata():
    with open(storing_file, 'r') as file:
        global current_data
        current_data = file.read()

def newdata():
    with open(storing_file, 'r') as file2:
        global new_data
        new_data = file2.read()

while True:
    newdata()
    print("Checking Shipment")
    if current_data != new_data:
        print("Your Shipment Has A New Status ")
        #but some lines here to send notification/alert to your phone using pushbullet, or something else!
        currentdata()
    else:
        time.sleep(5)
        print('Nothing New Recheck After 2 Hours')
        time.sleep(7200) #Check shipment every 2 hours
        with open(storing_file, 'w') as f:
            f.write(TrackerApi.getLastStatut(trackingnumber))
