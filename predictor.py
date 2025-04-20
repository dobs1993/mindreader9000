from collections import defaultdict, Counter

class PatternGuesser:
    def __init__(self):
        self.patterns = defaultdict(Counter)
        self.n = 2  # Length of input history to consider

    def train(self, sequence):
        if len(sequence) < self.n + 1:
            return

        for i in range(len(sequence) - self.n):
            key = tuple(sequence[i:i+self.n])
            next_item = sequence[i + self.n]
            self.patterns[key][next_item] += 1

    def predict_next(self, sequence):
        if len(sequence) < self.n:
            return "?"

        key = tuple(sequence[-self.n:])
        if key in self.patterns:
            return self.patterns[key].most_common(1)[0][0]

        return "?"
