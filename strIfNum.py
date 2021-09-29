
def is_number(s):
    try:
        float(s)
        print('我进来第一个float')
        return True
    except ValueError:
        #在编写代码时只写框架思路，具体实现还未编写就可以用 pass 进行占位，
        # 使程序不报错，不会进行任何操作。
        pass

    try:
        import unicodedata
        #如果能转成numeric，说明是一个数字
        # for ch in s:
        #     print('ch:',ch)
        unicodedata.numeric(s)
        return True
    except (TypeError,ValueError):
        pass
    return False

print(is_number('一二三四五上山打老虎'))