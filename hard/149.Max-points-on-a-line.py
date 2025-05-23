# Slope formula : (y2-y1)/(x2-x1)
class Solution(object):
    def maxPoints(self, points):
        res = 1
        for i in range(len(points)):
            hashMap = collections.defaultdict(int)
            p1 = points[i]
            for j in range(i +1, len(points)):
                p2 = points[j]
                if p1[0] - p2[0] == 0:
                    slope = float("inf")
                else:
                    slope = (p2[1]-p1[1]) / (p2[0]-p1[0])
                hashMap[slope] += 1
                res = max(res, hashMap[slope] +1)
        return res
