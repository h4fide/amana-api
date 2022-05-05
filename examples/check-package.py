from time import sleep
import sys

try:
    from examples.api import Tracker
except ImportError :
    try:
        from api import Tracker
    except ImportError:
        sys.exit("Move api.py to the same folder as this script")

trackingnumber = 'TRACKING_CODE_HERE'


laststatut = Tracker.LastStatus(trackingnumber)
if laststatut == 'Missing':
    print("Your Package Is Not Registerd In The System Yet\nOr Tracking Number Wrong")
    sleep(2)
    print('Script Continue Checking Anyway!')
    pass

storing_file = '.storing.dat'
try:
    with open(storing_file, 'r') as file:
        current_data = file.read()
except:
    with open(storing_file, 'w') as f:
        f.write(laststatut)


def currentdata():
    with open(storing_file, 'r') as file:
        global current_data
        current_data = file.read()

def newdata():
    with open(storing_file, 'r') as file2:
        global new_data
        new_data = file2.read()

print('Running')
while True:
    newdata()
    laststatut = Tracker.LastStatus(trackingnumber)
    print("Checking Shipment")

    if laststatut == 'Envoi livré':
        print("Your Shipment Has Arrived :)")
        break
    try:
        if current_data != new_data:
            print(f"Your Shipment Has A New Status\nParcel Satuts: {new_data}")
            #Put some lines here to send notification/alert to your phone using Pushbullet, Telegram or something else!
            currentdata()
        else:
            print('Nothing New\nRecheck After 2 Hours')
            sleep(7200) #Check shipment every 2 hours
            with open(storing_file, 'w') as f:
                f.write(laststatut)
    except KeyboardInterrupt:
        sys.exit('Keyboard Interrupt')
    except:
        currentdata()
