goal = "交換 swap， 接下來的， 兩個變數(two variables)"
a = 1
b = 99
print(goal)
print("a is: " + str(a))
print("b is: " + str(b))
# 交換過程
original_a = a # a 的內容，被儲存在 original_a

a = b      # 所以 a 的內容，已經被original_a保護，可以被 b 覆蓋
b = original_a       # 再將  original_a 的內容，覆蓋 b 
print("交換結果: ")
print("a is: " + str(a))
print("b is: " + str(b))