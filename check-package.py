from example.api import TrackerApi
import time
import os

statut = TrackerApi.getLastStatut('TRACKING_CODE_HERE')
storing_file = '.storing.dat'


# Post Maroc · Aaman · Barid Al Maghrib
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
        print('Nothing New :(\nRecheck After 2 Hours')
        with open(storing_file, 'w') as f:
            f.write(statut)
    time.sleep(7200) #Check shipment every 2 hours