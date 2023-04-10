import requests
import sys
import json

class FuckSnus:
    def __init__(self):
        pass

    def search(self, term):
        f = requests.get(f"https://beta.snusbase.com/v2/combo/{term}")
        out = f.json()["result"]
        l = []
        for item in out:
            for item2 in out[item]:
                l.append(item2)
        with open(f"output_{term}.json", "w") as file:
            json.dump(l, file)


if __name__ == '__main__':
    search = FuckSnus()
    search.search(sys.argv[1])
