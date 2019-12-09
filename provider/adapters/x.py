from provider.serializers import CarListSerializer

class Adapter():
    def __init__(self, client):
        print('x.Adapter init oldu')
        self.client = client

    def search(self):
        print('x.search init oldu')
        response = self.client.make_request()
        response = response.json()
        if response:
            my_response_data = []
            curr = 1.10775 #$ 	
            for resp in response["results"]:
                my_response = {
                    "vehicle_name": resp['vehicle_name'],
                    "is_available": resp['is_available'],
                    "total_amount": resp['total_amount'],
                    "currency": resp['currency'],
                }
                if resp['currency'] == 'usd':
                    my_response_data.append(my_response)
                else:
                    my_response['currency'] = "usd"                    
                    my_response['total_amount'] *= curr 
                    my_response_data.append(my_response)
            print(my_response_data)
            return my_response_data