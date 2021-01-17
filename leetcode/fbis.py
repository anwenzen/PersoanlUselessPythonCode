

def fibs(n):
    # 斐波那次数列
    if n <= 2:
        return [0, 1, 1][n]
    else:
        a, b, c = 0, 1, 1
        while n > 2:
            a = b + c
            a, b, c = b, c, a
            n -= 1
        return c
# 数组最好，递归最垃圾


if __name__ == '__main__':
    try:
        for i in range(0, 40):
            print(fibs(i))
    except Exception as e:
        print(e)
        print('except')
    else:
        print('try success')
    finally:
        print('finally')