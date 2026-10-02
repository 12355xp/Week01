# 第一個錯誤， NameError錯誤，name ‘pi’ is not defined，請修正後，再次執行
# 第二個錯誤 TypeError: can only concatenate str (not "float") to str
pi = 3.14
radius = 10
print("一個圓，半徑radius是 " + str(radius))
area = pi *(radius)**2
print("此圓的面積是 " + str(area))