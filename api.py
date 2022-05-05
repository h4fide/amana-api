import requests

PROVIDER = "http://bam.magnetomedia.de/trackinghistory.php"
LOBool = 'true'

class Tracker(object):
    """ 
    It's a class that makes a POST request to a URL, and returns the JSON response
    """
    @staticmethod
    def PackageInfo(trackingNumber: str):
        """
        It takes a tracking number, and returns a dictionary of information about the package
        
        :param trackingNumber: The tracking number of the package
        :return: A dictionary of the package information.
        """
        try:
            req = requests.get(f'{PROVIDER}?lastOperation={LOBool}&trackingNumber={trackingNumber}' ,timeout=5.0)
        except requests.exceptions.Timeout:
            print('Timeout')
        except requests.exceptions.RequestException as er:
            print('OOps Somthing Wrong')
            raise SystemExit(er)

        if req.status_code == 200:
            return req.json()["data"][0]
        else:
            SystemExit('Http Error')


    @staticmethod
    def LastStatus(trackingNumber: str) -> None:
        """
        It returns the last status of the package
        
        :param trackingNumber: The tracking number of the package
        :return: The last status of the package
        """
        info = Tracker.PackageInfo(trackingNumber)
        try:
            if LOBool == 'false':
                etat = info['etat']
                if etat == 'Infos.Indisponibles':
                    return 'Missing'
                return etat
            if LOBool == 'true':
                last_status = info["dernier_statut"]
                if last_status == 'Neant':
                    return 'Missing' # This Package Is Not Registerd In The System Yet or Tracking Code is Wrong
                return last_status
            else:
                return "Unknown"
        except:
            print('No response')
    
