class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        total=0
        time=0
        for i in timeSeries:
            if i>=time:
                total+=duration
                time=i+duration
            else:
                total+=i+duration-time
                time+=i+duration-time
        return total