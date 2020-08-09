import scipy
import mibian
from datetime import date


underlyingPrice = 1.4565
strikePrice = 1.45
interestRate = 1
callPrice = 0.00359
putPrice = 0.00306
warrantPrice = 0.00359
expirationDate = date(2020, 7, 17)
parity = 10
type = 1    # 1 = call, 2 = put


class Warrant:

    def __init__(self, underlyingPrice, strikePrice, interestRate, warrantPrice, expirationDate, parity, type):
        self.underlyingPrice = underlyingPrice
        self.strikePrice = strikePrice
        self.interestRate = interestRate
        self.warrantPrice = warrantPrice
        self.expirationDate = expirationDate
        self.parity = parity
        self.type = type

        #   Get days to expiration
        self.daysToExpiration = self.expirationDate - date.today()
        self.daysToExpiration = self.daysToExpiration.days

        # Adjust for parity
        self.paritizedWarrantPrice = self.warrantPrice*self.parity

        # Get implied volatility
        if type == 1:
            w = mibian.BS([self.underlyingPrice, self.strikePrice, self.interestRate, self.daysToExpiration], callPrice = self.paritizedWarrantPrice)
        elif type == 2:
            w = mibian.BS([self.underlyingPrice, self.strikePrice, self.interestRate, self.daysToExpiration], putPrice = self.paritizedWarrantPrice)
        else:
            print("Type not defined, call/put!!!")
            quit()

        self.volatility = w.impliedVolatility

        # Construct warrant
        w = mibian.BS([self.underlyingPrice, self.strikePrice, self.interestRate, self.daysToExpiration], volatility = self.volatility)

        # Get greeks(s)
        if type == 1:
            self.delta = w.callDelta
            self.delta2 = w.callDelta2
            self.theta = w.callTheta
            self.rho = w.callRho
        elif type == 2:
            self.delta = w.putDelta
            self.delta2 = w.putDelta2
            self.theta = w.putTheta
            self.rho = w.putRho

        self.vega = w.vega
        self.gamma = w.gamma
        # TODO: some of the greeks need to be paritized...



call = Warrant(underlyingPrice, strikePrice, interestRate, warrantPrice, expirationDate, parity, type)

print(call.delta)
print(call.volatility)
print(call.warrantPrice)
print(call.paritizedWarrantPrice)

put = Warrant(underlyingPrice, strikePrice, interestRate, 0.00306, expirationDate, parity, 2)

print(put.delta)
print(put.volatility)
print(put.warrantPrice)
print(put.paritizedWarrantPrice)
print(put.gamma, put.rho, call.theta, call.delta2)

print("To delta neutral", round((-put.delta/call.delta),2) ,"calls are needed for every put")
