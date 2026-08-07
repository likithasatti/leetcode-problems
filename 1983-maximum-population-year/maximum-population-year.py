class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        count = [0] * 101

        for birth, death in logs:

            for year in range(birth, death):
                count[year - 1950] += 1

        max_people = 0
        answer = 1950

        for i in range(101):

            if count[i] > max_people:
                max_people = count[i]
                answer = i + 1950

        return answer