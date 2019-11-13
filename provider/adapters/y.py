class Adapter():
    def __init__(self, client):
        print('y.Adapter init oldu')
        self.client = client

    def search(self):
        print('y.search init oldu')
        response = self.client.make_request()
        response = response.json()
        if response:
            return response