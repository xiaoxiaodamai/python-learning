todos = ["买菜", "洗衣服", "写作业"]

todos.append("发邮箱")
todos.insert(0,"交电费")
todos.remove("洗衣服")
popped = todos.pop()

print("剩下的待办：",todos)
print("pop删掉的是：", popped)