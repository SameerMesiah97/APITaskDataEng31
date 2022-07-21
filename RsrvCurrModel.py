import requests

class RsrvCurrModel:
    def __init__(self, exchange_rates):
        self.base_cur = exchange_rates['base_code']
        self.__other_cur = exchange_rates['conversion_rates']
        self.toGBP = self.__other_cur['GBP']
        self.toUSD = self.__other_cur['USD']
        self.toEUR = self.__other_cur['EUR']
        self.toJPY = self.__other_cur['JPY']


class RsrvCurr:
    def __init__(self, curr_code):

        API_key = "51f6162035ba3e243cfb74e0"
        self.url = "https://v6.exchangerate-api.com/v6/"+ API_key + "/latest/" + curr_code
        self.request = requests.get(self.url)
        self.response = self.request.json()

    def response_data(self):
        return RsrvCurrModel(self.response)
