# Morocco Post API
Poste Maroc · Aaman · Barid Al Maghrib

![Logo](https://seeklogo.com/images/A/amana-messagerie-logo-859E7C8309-seeklogo.com.png)

## Usage

```python3
from api import Tracker

Tracker.LastStatus('TRACKING_CODE')
Tracker.PackageInfo('TRACKING_CODE')

}
```


## Examples

Shipment last status

```python3
  Tracker.LastStatus('TRACKING_CODE')
```

Get all the information about the parcel as JSON

```python3
  Tracker.PackageInfo('TRACKING_CODE')
```

```json
        {
            "code_bordereau": "LD8******25MA",
            "libelle_produit": "Express - PRN",
            "date_depot": "10-02-2021",
            "destination": "TAZA",
            "date_livraison": "13-02-2022",
            "poids": "5.787",
            "destinataire": "h4fide",
            "dernier_statut": "Envoi livré",
            "lieu_depot": "RABAT AL MADINA CD",
            "id_statut": "liv",
            "mtt_crbt": "2070.00",
        }
```
Example to get price of the package use this command
```python3
  Tracker.PackageInfo('TRACKING_CODE')['mtt_crbt']
```
Output
```bash
  2070.00
```

## API Reference

#### GET

```http
  GET http://bam.magnetomedia.de/trackinghistory.php
```

| KEY             | VALUAE           | Required  | Description                                         |
| :---------------| :--------------- | :-------- |:--------------------------------------------------- |
| `lastOperation` | `false` or `true`| **No**    | Show its current status and hide other informations |
| `trackingNumber`| `TRACKING_CODE`  | **Yes**   | Package tracking number                             |


## Contributing

Contributions are always welcome!
Feel free :)
