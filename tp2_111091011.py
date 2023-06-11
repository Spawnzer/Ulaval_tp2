sub_str = "bb"
ini_str = "abbbbabbabbbb"
res = 0
i = 0
while i < len(ini_str):
    if ini_str[i:i+len(sub_str)] == sub_str:
        res += 1
        i += len(sub_str)
    else:
        i += 1
print(res)