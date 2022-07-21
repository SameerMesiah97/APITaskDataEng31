class RsrvCurrModel:

    def __init__(self, exchange_rates):
        self.base_cur = single_pc['base_code']
        self.other_cur = self.base_cur['conversion_rates']
        self.toGBP = self.other_cur['GBP']
        self.toUSD = self.other_cur['USD']
        self.toEUR = self.other_cur['EUR']
        self.toJPY = self.other_cur['JPY']
