import requests

PROVIDER_URL = "http://bam.magnetomedia.de/trackinghistory.php"
lastOBool = 'true'

class TrackerApi(object):
    """ API AMANA """

    @staticmethod
    def getPackageInformation(trackingNumber):
        req = requests.post(PROVIDER_URL + '?lastOperation='+ lastOBool + '&trackingNumber=' + trackingNumber)

        if req.json()["response"] != '0':
            raise ValueError("Unknown Error!")
        else:
            return req.json()["data"]


    @staticmethod
    def getLastStatut(trackingNumber):
        info = TrackerApi.getPackageInformation(trackingNumber)
        
        if lastOBool == 'false':
            etat = info[0]['etat']
            if etat == 'Infos.Indisponibles':
                return "This Package Is Not Registerd In The System Yet"
            return etat
        if lastOBool == 'true':
            dernier_statut = info[0]["dernier_statut"]
            if dernier_statut == 'Neant':
                return "This Package Is Not Registerd In The System Yet"
            return dernier_statut
        else:
            return "Unknown"
    
