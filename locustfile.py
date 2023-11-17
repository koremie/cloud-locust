import locust

endpoints = [
    '/api/addresses',
    '/api/cities',
    '/api/counties',
    '/api/machine-models',
    '/api/menus',
    '/api/restocks',
    '/api/service-staff',
    '/api/snacks',
    '/api/vending-machines',
]

class UserPool(locust.FastHttpUser):
    @locust.task
    def flood_requests(self):
        for endpoint in endpoints:
            self.client.get(endpoint)