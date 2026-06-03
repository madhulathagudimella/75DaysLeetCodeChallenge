class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        ans = float('inf')
        minLand = float('inf')
        for i in range(len(landStartTime)):
            minLand = min(minLand, landStartTime[i] + landDuration[i])
        minWater = float('inf')
        for j in range(len(waterStartTime)):
            minWater = min(minWater, waterStartTime[j] + waterDuration[j])
        for j in range(len(waterStartTime)):
            start = max(minLand, waterStartTime[j])
            ans = min(ans, start + waterDuration[j])
        for i in range(len(landStartTime)):
            start = max(minWater, landStartTime[i])
            ans = min(ans, start + landDuration[i])
        return ans