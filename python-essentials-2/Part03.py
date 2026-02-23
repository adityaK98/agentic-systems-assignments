class StudentPerformance:
    def __init__(self, scores):
        self.scores = scores

    def score_difference(self):
        try:
            if len(self.scores) == 0:
                raise ValueError
            difference = self.scores[-1] - self.scores[0]
            print("Difference between last and first score is:", difference)
        except ValueError:
            print("No scores available to calculate difference")


# Example
scores = [55, 65, 75, 85]
student = StudentPerformance(scores)
student.score_difference()