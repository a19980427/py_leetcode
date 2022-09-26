class MapSum:

    def __init__(self):
        self.maps = {}

    def insert(self, key: str, val: int) -> None:
        self.maps[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for k, v in self.maps.items():
            if k.startswith(prefix):
                res += v
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)


