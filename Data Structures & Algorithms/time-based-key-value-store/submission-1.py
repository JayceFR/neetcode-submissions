class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.data.get(key) is None:
            self.data[key] = []
        self.data[key].append((timestamp, value))
        self.data[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        if self.data.get(key) is None:
            return ""
        arr = self.data[key]
        fp, rp = 0, (len(arr) - 1)
        cacheValue = ""
        while fp <= rp:
            mp = (fp + rp) // 2 
            if timestamp < arr[mp][0]:
                rp = mp - 1 
            else:
                cacheValue = arr[mp][1]
                fp = mp + 1 
        return cacheValue
