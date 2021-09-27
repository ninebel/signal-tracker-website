"""
=========================================
                INDICATORS

                By: Lindtrs

All indicators in this code came from
the book 'Come into my trading room'
written by Dr. Alexander Elder
=========================================
"""

# Simple Moving Average

# n - integer for calculation of the avg. price of n samples
# prices - list close prices

def SMA (n, prices):

  sma = []

  for i in range (0, n-1):

     sma.append(prices[0])

  for i in range (n-1 , len(prices)):

     summ = 0

     for j in range (0, n):

        summ += prices[i-j]

     sma.append(summ/n)

  return sma

#--------------------

# Exponential Moving Average

# n - integer for calculation of the avg. price of n samples
# prices - list of prices

def EMA (n, prices):

  ema = [prices[0]]
  k = 2/(n+1)

  for i in range (1, len(prices), 1):

     ema.append(prices[i] * k + ema[len(ema)-1] * (1-k))

  return ema

#--------------------

# Moving Average Convergence/Divergence

# prices - list of close prices

def MACD (prices):

  ema12 = EMA(12, prices)
  ema26 = EMA(26, prices)

  fastMACD = []

  for i in range (0, len(ema12), 1):
  
     fastMACD.append(ema12[i] - ema26[i])

  slowMACD = []
  slowMACD = EMA(9, fastMACD)

  return fastMACD, slowMACD

#--------------------

# Moving Average Convergence/Divergence Histogram

# prices - list of close prices


def MACDhistogram (prices):

  fastMACD , slowMACD = MACD(prices)

  MACDhist = []

  for i in range (0, len(fastMACD), 1):

     MACDhist.append(fastMACD[i] - slowMACD[i])

  return MACDhist

#--------------------

# Strength Index

# prices - list of close prices
# volumes - list of traded volume for each price in prices

def StrengthIndex(prices, volumes):

  strengthIndex = []

  strengthIndex.append(0)
  
  for i in range (1, len(prices), 1):

     strengthIndex.append( (prices[i] - prices[i-1])*volumes[i])
  
  strengthIndex = self.EMA(2, strengthIndex)

  return strengthIndex

#--------------------

# Stochastic

# prices - list close prices
# highs - list of maximum price for each close price
# lows - list of minimum price for each close price

def Sthocastic (prices, highs, lows):

    #k - fast line
    #d - slow line

    k = []
    d = []

    # For k line
    for i in range (0, len(prices), 1):

        k.append( (prices[i] - lows[i]) / (highs[i] - lows[i]) * 100 )

    # For d line
    d = SMA(3, k)

    return k, d

#--------------------

