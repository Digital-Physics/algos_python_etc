import matplotlib.pyplot as plt
import math

complexity_dict = {"constant; O(1)": [[], lambda x: 1],
                   "log; O(log(n))": [[], lambda x: math.log(x, 2)],
                   "linear; O(n)": [[], lambda x: x],
                   "n_log_n; O(n*log(n))": [[], lambda x: x*math.log(x, 2)],
                   "n_squared; O(n**2)": [[], lambda x: x*x],
                   "2_to_n; O(2**n)": [[], lambda x: 2**x],
                   "n_factorial; O(n!)": [[], lambda x: math.factorial(x)]}

for i in range(1, 11):
    for key in complexity_dict:
        complexity_dict[key][0].append(complexity_dict[key][1](i))

# plot lines
for key in complexity_dict:
    plt.plot(range(1, 11), complexity_dict[key][0], label=key)

# 1,10 is for x axis range. 0,100 is for y axis range.
plt.axis([1, 10, 0, 100])
plt.title("Big O Complexity comparison (small n; scaled Y axis)")
plt.legend()
plt.savefig("BigO.png")
plt.show()



