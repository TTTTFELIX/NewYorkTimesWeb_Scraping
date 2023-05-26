import json
import matplotlib.pyplot as plt

outp = json.load(open("articles.json", "r"))

count = [0] * 12
month_index = [x for x in range(1, 13)]

for data in outp:
    try:
        ur = data["url"]
        month = int(ur.split("/2022/")[1][:2])
        count[month - 1] += 1
    except:
        pass
print(count)

plt.bar(count,month_index )
plt.xlabel("month")
plt.ylabel("numbers")
plt.show()