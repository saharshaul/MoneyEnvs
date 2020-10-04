import random


class Automatic_BaseStrategy(BaseStategy):
  def perform_startegy(self, counter):
      rnd = random.randint(100)
      return envelopes[rnd]


class N_max_srategy(BaseStategy):
  def __init__(self, n):
    self.n = n

  def perform_startegy(self, counter):
      pass


class More_then_N_percent_group_srategy(BaseStategy):
    def __init__(self, percent):
        self.percent = percent

    def perform_startegy(self, counter):
        pass


