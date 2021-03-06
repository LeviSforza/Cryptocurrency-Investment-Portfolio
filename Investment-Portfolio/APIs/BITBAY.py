from abc import ABC
from APIs.API import Api


class Bitbay(Api, ABC):
    def __init__(self):
        super().__init__('Bitbay', 'https://api.bitbay.net/rest/trading', 0.0043, 'ra', 'ca')
        self._fees = {
            "AAVE": 0.54, "ALG": 426.0, "AMLT": 1743.0,
            "BAT": 156.0, "BCC": 0.001, "BCP": 1237.0,
            "BOB": 11645.0, "BSV": 0.003, "BTC": 0.0005,
            "BTG": 0.001, "COMP": 0.1, "DAI": 81.0,
            "DASH": 0.001, "DOT": 0.1, "EOS": 0.1,
            "ETH": 0.006, "EXY": 520.0, "GAME": 479.0,
            "GGC": 112.0, "GNT": 403.0, "GRT": 84.0,
            "LINK": 2.7, "LML": 1500.0, "LSK": 0.3,
            "LTC": 0.001, "LUNA": 0.02, "MANA": 100.0,
            "MKR": 0.025, "NEU": 572.0, "NPXS": 46451.0,
            "OMG": 14.0, "PAY": 1523.0, "QARK": 1019.0,
            "REP": 3.2, "SRN": 5717.0, "SUSHI": 8.8,
            "TRX": 1.0, "UNI": 2.5, "USDC": 125.0,
            "USDT": 190.0, "XBX": 6608.0, "XIN": 5.0,
            "XLM": 0.005, "XRP": 0.1, "XTZ": 0.1,
            "ZEC": 0.004, "ZRX": 56.0
        }
        self._markets = self.markets_list

    def transferFee(self, symbol):
        if symbol in self._fees:
            return float(self._fees[symbol])
        else:
            raise ValueError(f'Incorrect symbol: {symbol}')

    @property
    def markets_list(self):
        response = self.data_request(f'{self._url}/ticker')
        markets = []
        for market in response.json()['items']:
            markets.append(market)
        return markets

    def orderbook(self, symbol):
        if symbol in self._markets:
            response = self.data_request(f'{self._url}/orderbook/{symbol}')
            bids = response.json()['buy']
            asks = response.json()['sell']
            return {'bid': bids, 'ask': asks}
        else:
            return 0
