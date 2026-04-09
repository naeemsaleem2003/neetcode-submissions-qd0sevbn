class Solution:
    def calPoints(self, operations: List[str]) -> int:
        """
An integer x: Record a new score of x.
'+': Record a new score that is the sum of the previous two scores.
'D': Record a new score that is the double of the previous score.
'C': Invalidate the previous score, removing it from the record.

Input: ops = ["5","D","+","C"]
Output: [5, 10] = 15
"""
        values = []
        for i in range(len(operations)):
            if operations[i] == "+":
                values.append(values[-1] + values[-2])
            elif operations[i] == "D":
                values.append(values[-1] + values[-1])
            elif operations[i] == "C":
                values.pop(-1)
            else:
                values.append(int(operations[i]))
        return sum(values)

