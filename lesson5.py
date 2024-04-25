# 创建数字列表
numbers = [10, 20, 30, 40, 50]

# 询问用户号码
user_number = int(input("请输入一个数字："))

# 检查号码是否在列表中
if user_number in numbers:
    print("恭喜，您猜对了号码！")
else:
    print("没有这个号码！")

# 打印原始列表
print("原始列表：", numbers)

# 创建列表
my_list = [1, 2, 3, 4, 4, 5]

# 检查重复元素
duplicates = set(x for x in my_list if my_list.count(x) > 1)

if duplicates:
    print("重复元素：", duplicates)
else:
    print("没有重复元素。")

# 一周中各天名称列表
days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# 询问用户休息天数
rest_days = int(input("您想要休息多少天："))

# 计算休息和工作日
weekend_days = days[-rest_days:]
work_days = days[:-rest_days]

print("您的周末：", weekend_days)
print("您的工作日：", work_days)

# 创建学生姓名列表
group1 = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Helen", "Ivan", "Jack"]
group2 = ["Kate", "Liam", "Mia", "Noah", "Olivia", "Peter", "Quinn", "Rose", "Sam", "Tom"]

# 创建运动队
team = tuple(group1[:5] + group2[:5])

# 显示原始组列表和新生成的元组
print("原始组列表1：", group1)
print("原始组列表2：", group2)
print("新生成的运动队：", team)

# 打印长度
print("运动队长度：", len(team))

# 按字母顺序排序
sorted_team = sorted(team)
print("排序后的运动队：", sorted_team)

# 确定“Ivanov”是否在团队中，并计算出现次数
ivanov_count = sorted_team.count("Ivanov")
if ivanov_count:
    print(f"‘Ivanov’在团队中，出现了{ivanov_count}次。")
else:
    print("‘Ivanov’不在团队中。")