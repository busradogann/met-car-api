class Adapter():
    def __init__(self, client):
        print('x.Adapter init oldu')
        self.client = client

    def search(self):
        print('x.search init oldu')
        response = self.client.make_request()
        response = response.json()
        if response:
            return response