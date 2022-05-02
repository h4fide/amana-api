import requests

PROVIDER_URL = "http://bam.magnetomedia.de/trackinghistory.php"
lastOBool = 'true'

class TrackerApi(object):
    """ 
    It's a class that makes a POST request to a URL, and returns the JSON response
    """
    @staticmethod
    def getPackageInformation(trackingNumber: str):
        """
        It takes a tracking number, and returns a dictionary of information about the package
        
        :param trackingNumber: The tracking number of the package
        :return: A dictionary of the package information.
        """
        req = requests.get(PROVIDER_URL + '?lastOperation='+ lastOBool + '&trackingNumber=' + trackingNumber)

        if req.json()["response"] != '0':
            raise ValueError("Unknown Error!")
        else:
            return req.json()["data"][0]


    @staticmethod
    def getLastStatut(trackingNumber: str) -> None:
        """
        It returns the last status of the package
        
        :param trackingNumber: The tracking number of the package
        :return: The last status of the package
        """
        info = TrackerApi.getPackageInformation(trackingNumber)
        
        if lastOBool == 'false':
            etat = info['etat']
            if etat == 'Infos.Indisponibles':
                return 'Missing' # This Package Is Not Registerd In The System Yet Or Tracking Code is Wrong
            return etat
        if lastOBool == 'true':
            dernier_statut = info["dernier_statut"]
            if dernier_statut == 'Neant':
                return 'Missing' # This Package Is Not Registerd In The System Yet 
            return dernier_statut
        else:
            return "Unknown"
    
