import pandas as pd

with open("2021/day3/input.txt", "r") as file:
    _input = [x.strip() for x in file.readlines()]
# explode for making dataframe easier
l = []
for x in _input:
    l.append([y for y in x])

def to_decimal(b):
    return int(b,2)

def lfr(df, mode):
    i = 0
    while df.shape[0] > 1:
        n = df[i].value_counts()
        if n[0] == n[1]:
            common = 1 if mode == "ogr" else 0
        else:
            common = n.index[0] if mode =="ogr" else n.index[-1]
        df = df[df[i]==common]
        i = i+1
    return to_decimal("".join([str(x) for x in df.values.tolist()[0]]))

# Part 1
df = pd.DataFrame(np.array(l))
gamma_rate = "".join(df.mode().values.tolist()[0])
epsilon_rate = "".join(['1' if i == '0' else '0' for i in gamma_rate])
answer = to_decimal(gamma_rate)*to_decimal(epsilon_rate)
print(f"part1: {answer}")

# Part 2
df = pd.DataFrame(np.array(l))
df = df.apply(pd.to_numeric)
ogr = lfr(df,"ogr")
co2 = lfr(df,"co2")
print(f"part2: {ogr*co2}")
