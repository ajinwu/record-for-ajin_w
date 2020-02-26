from collections import namedtuple

Result = namedtuple("Result", "count, average")

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

def grouper(result, key):
    while True:
        result[key] = yield from averager()

    
def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    report(results)

def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print("{:2} {:5} averaging {:.2f}{}".format(result.count, group, result.average, unit))


data = {
    "girls;kg":
    [40,38,44]
}

if __name__ == "__main__":
     main(data)