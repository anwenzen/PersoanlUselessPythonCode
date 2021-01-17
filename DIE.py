from random import randint
class Die():
    def __init__(self,num_sides =6):
        self.num_sides = num_sides
    def roll(self):
        return randint(1,self.num_sides)

import pygal
die_1 = Die()
die_2 = Die()
die_3 = Die()
# 掷几次骰子，并将结果存储在一个列表中
results = []
for roll_num in range(10000):
    result = die_1.roll()+die_2.roll()+die_3.roll()
    results.append(result)
# 分析结果
frequencies = []
max_result = die_1.num_sides+die_2.num_sides+die_3.num_sides
for value in range(3,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# 可视化结果
hist = pygal.Bar()
hist.title = "Results of rolling one D6 10000 times."
hist.x_labels = [str(i) for i in range(3, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D6',frequencies)
hist.render_to_file('die_visual.svg')