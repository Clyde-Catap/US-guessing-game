# xx = input("butu")
#
#
# count = 0
#
# for g in xx:
#     if g == " ":
#         count += 1
#
# print(count)


answer_state = input("butu")

z = []
ww = answer_state.split()
for w in ww:
    xww = w.capitalize()
    z.append(xww)

answer_state = " ".join(z)

print(answer_state)