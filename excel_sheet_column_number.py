def titleTonumber(columntitle):
    # 解法一

    power = 0
    result = 0

    for i in reversed(columntitle):
        result += (pow(26, power) * (ord(i) - ord('A') + 1))
        power += 1

    print(columntitle, '=', result)

    # 解法二()
    #ans = 0
    # for i in columntitle:
    #    ans = ans*26 + ord(i)-ord('A')+1
    # return ans


def main():
    titleTonumber("A")
    titleTonumber("AB")
    titleTonumber("ZY")
    titleTonumber("FXSHRXW")


if __name__ == "__main__":
    main()
