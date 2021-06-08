import heapq


class MedianFinder:
    def __init__(self):
        self.center = None
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        assert len(self.low) == len(self.high)
        if self.center is None:
            if len(self.low) > 0 and num < -self.low[0]:
                self.center = -heapq.heappop(self.low)
                heapq.heappush(self.low, -num)
            elif len(self.high) == 0 or num <= self.high[0]:
                self.center = num
            else:
                self.center = heapq.heappop(self.high)
                heapq.heappush(self.high, num)
        else:
            if num < self.center:
                heapq.heappush(self.low, -num)
                heapq.heappush(self.high, self.center)
            else:
                heapq.heappush(self.low, -self.center)
                heapq.heappush(self.high, num)
            self.center = None

    def findMedian(self) -> float:
        return self.center if self.center is not None else (self.high[0] - self.low[0]) / 2
