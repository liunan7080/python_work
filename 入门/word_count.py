def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        print("Sorry, the file " + filename + "does not exist")
    else:
        # 计算大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print("The file " + filename + "has about " + str(num_words) + " words.")

filename = input("输入文件名：")
count_words(filename)
