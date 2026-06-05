class TimeMap:

    def __init__(self):
        self.tmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.tmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        val = self.tmap[key]

        l = 0
        r = len(val) - 1
        res = ""

        while l <= r:
            m = (l + r) // 2
            if val[m][1] <= timestamp:
                res = val[m][0]
                l += 1
            else:
                r = m - 1
        return res
