# ============================================
# 南大附中 - AI 創意導航
# 第 1 週實作鷹架模板：個人專屬自我介紹產生器 (lesson01.py)
# 檔案儲存路徑：文件/AI/Week01/
# 完成後請另存或執行：lesson01.py
# ============================================

# 【步驟一：設定預設變數 (賦值觀念練習)】
# 請在右側引號內填入你的個人資訊 (將值存入左邊的變數容器中)
student_name = "陳韋桀"
school_name = "南大附中"
grade = "高一"
favorite_hobby = "看小說"

# 【步驟二：互動式輸入 (使用 input 函數)】
# 使用 input() 讓使用者在 Terminal 輸入內容，並儲存到變數 target_goal 中
print(f"👋 嗨！我是 {student_name}，歡迎來到我的 Python 程式基地！")
target_goal = input("🎯 請輸入你這學期在 AI 創意導航課最想完成目標：")

# 【步驟三：變數串接與動態輸出】 💡 觀念說明：
# 1. f"..."是 Python 的「格式化字串」語法。
# 2. 大括號 {} 裡面的變數內容抽出來，轉化為文字後，與引號內的文字拼接在一起。
# 3. 外層的圓括號 () 只是用來把多行的字串連接起來，並不會改變它的資料類型。

print("\n" + "=" * 40)
print("✨【個人專屬自我介紹卡片】✨")

# 請補全下方 f-string 中的變數名稱：
profile_card = (
    f"學校：{school_name} {grade}\n"
    f"創作者：{student_name}\n"
    f"個人興趣：{favorite_hobby}\n"
    f"本學期目標：{target_goal}"
)


print(profile_card)
print("=" * 40)
print("🚀 恭喜你成功在 VS Code 完成並執行了人生第一個本機 Python 專案！")