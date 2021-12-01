import pandas as pd

with open("input.txt", "r") as file:
    _input = [int(x.strip()) for x in file.readlines()]

#Part 1
i = 0
increases = 0
while i < len(_input):
    if i == 0:
        pass
    else:
        if _input[i] > _input[i-1]:
            increases = increases + 1
    i = i+1

print(f"day1: {increases}")


# Part 2
s = pd.Series(_input)

rolling_s = s.rolling(3).sum()
prev_s = rolling_s.shift(1)

df = pd.concat([rolling_s, prev_s], axis=1)
df["increased"] = (df[0] > df[1])
print(df["increased"].value_counts())

