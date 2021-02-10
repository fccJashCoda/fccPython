import copy
import random


class Hat:

    def __init__(self, **balls):
        self.contents = []
        for ball, quantity in balls.items():
            self.contents += [ball for x in range(quantity)]

    def draw(self, draws):
        if draws >= len(self.contents):
            return self.contents

        batch = []

        for i in range(draws):
            index = random.randint(0, len(self.contents) - 1)
            ball = self.contents[index]

            batch.append(ball)

            self.contents.remove(ball)

        return batch


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    match = 0

    for i in range(num_experiments):
        subject = copy.deepcopy(hat)
        sample = subject.draw(num_balls_drawn)

        isMatch = True
        for item, qty in expected_balls.items():
            if sample.count(item) < qty:
                isMatch = False
                break

        if isMatch:
            match += 1

    result = (match / num_experiments)
    return result
