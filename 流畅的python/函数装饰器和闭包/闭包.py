def average():
    series = []
    def make_average(new_value):            # 1
        series.append(new_value)            # 2
        return sum(series) / len(series)    # 3
    return make_average                     # 4

# avg = average()
# print(avg(10))  # 运行顺序 4->1->2->3
# print(avg(11))


def make_aver():
    count = 0
    total = 0
    def aver(new_value):
        nonlocal count, total 
        count += 1
        total += new_value
        return total / count
    return aver

maker = make_aver()
print(maker(10))
print(maker(11))
