import matplotlib.pyplot as plt
import pandas as pd
import math

class ucb_calculator():
    def __init__(self,data):
        data = pd.read_csv(data)
        self.data = data
        self.length = len(data)
        self.column = len(data.iloc[1])
        self.awards = [0]* len(data)
        self.total = 0
        self.chosens = []
    def calculator(self):
        d = self.column
        l = self.length
        clicks = [0] * d
        awards = [0] * d
        for i in range(0,l):
            choice = 0
            max_ucb = 0
            for j in range(0,d):
                if (clicks[j] > 0):
                    av = int(awards[j]) / int(clicks[j])
                    delta = math.sqrt(3/2 * math.log(l) / clicks[j])
                    ucb = av + delta
                else:
                    ucb = 1
                if max_ucb <ucb:
                    max_ucb = ucb
                    choice = j
            self.chosens.append(choice)
            clicks[choice] = clicks[choice] + 1
            award = self.data.values[i,choice]
            awards[choice] = awards[choice] + award
            self.total = self.total + award
        return self.total,self.chosens
    def plot(self,chosens):
        plt.hist(self.chosens)
        plt.show()
