lines = list(map(str.strip, open("2021/day8/input.txt").readlines()))

def decode_digits(signals):
    d = {}
    d["1"] = set(list(filter(lambda x: len(x) == 2, signals))[0])
    d["4"] = set(list(filter(lambda x: len(x) == 4, signals))[0])
    d["7"] = set(list(filter(lambda x: len(x) == 3, signals))[0])
    d["8"] = set(list(filter(lambda x: len(x) == 7, signals))[0])
    d["235"] = list(filter(lambda x: len(x) == 5, signals))
    d["690"] = list(filter(lambda x: len(x) == 6, signals))
    for x in d["235"]:
        x_set = set(x)
        if d["7"].issubset(x_set):
            d["3"] = x_set
        elif len(d["4"].intersection(x_set)) == 3:
            d["5"] = x_set
        else:
            d["2"] = x_set
    d.pop("235")
    for x in d["690"]:
        x_set = set(x)
        if d["4"].issubset(x_set):
            d["9"] = x_set
        elif d["7"].issubset(x_set):
            d["0"] = x_set
        else:
            d["6"] = x_set
    d.pop("690")
    return d


uniques = 0
output_sum = 0
for x in lines:
    output_value = ""
    signals, output = x.split(" | ")
    digits = decode_digits(signals.split(" "))
    for y in output.split(" "):
        if len(y) in [2,3,4,7]:
            uniques = uniques + 1
        output = set(y)
        for key in digits:
            if output == digits[key]:
                output_value = output_value + key
    output_sum = output_sum + int(output_value)

print(f"Part 1: {uniques}")
print(f"Part 2: {output_sum}")

