import random
import bisect


# Returns a random value, considering the weights of each item.
class WeightedChoice:
    """
Takes an argument in this format only: [['Name', weight(int type)], ..., ['Something', 3]]
    """
    def __init__(self, weights):
        self.totals = list()
        self.weights = weights
        self.__load_weights()

    # for weights loading only (also for reloading when using "increase_chance" method)
    def __load_weights(self):
        if self.totals:
            self.totals = list()
        running_total = 0
        for w in self.weights:
            running_total += w[1]
            self.totals.append(running_total)

    def get_item(self):
        rnd = random.random() * self.totals[-1]
        i = bisect.bisect_right(self.totals, rnd)
        return self.weights[i][0]

    def increase_chance(self, action_name, chance):
        for item in self.weights:
            if action_name == item[0]:
                item[1] = chance
                self.__load_weights()
                break
