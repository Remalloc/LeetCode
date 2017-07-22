class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        mission = {}
        result = 0
        for i in tasks:
            mission[i] = mission.get(i, 0) + 1
        l_mission = []
        for value in mission.values():
            l_mission.append(value)
        l_mission.sort(reverse=True)
        max_total = 0
        max_num = l_mission[0]
        for i in l_mission:
            if max_num == i:
                max_total += 1
            else:
                break
        return max(len(tasks), (max_num - 1) * (n + 1) + max_total)