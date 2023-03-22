import requests
import os

class ApiClient:
    def __init__(self):
        self.url = os.environ['ACTITIME_URL']
        self.username = os.environ['ACTITIME_USERNAME']
        self.password = os.environ['ACTITIME_PASSWORD']

    def fetch_data(self, **kwargs):
        url = f"{self.url}timetrack"
        headers = {"Content-Type": "application/json"}
        auth = (self.username, self.password)

        stop_after = int(kwargs.pop("stopAfter", 1000))
        date_from = kwargs.pop("dateFrom", "1970-01-01")
        date_to = kwargs.pop("dateTo","3000-12-31")
        
        if stop_after > 1000:
            stop_after = 1000
        elif stop_after < 1:
            stop_after = 1
        
        params = {"dateFrom": date_from, "dateTo": date_to, "stopAfter": stop_after}
        params.update(kwargs)

        records = []

        while True:
            
            response = requests.get(url, headers=headers, auth=auth, params=params)
            
            if not response.ok:
                response.raise_for_status()

            data = response.json()
            records.extend(data["data"])

            if "nextDateFrom" not in data:
                break

            params["dateFrom"] = data["nextDateFrom"]

        return records
