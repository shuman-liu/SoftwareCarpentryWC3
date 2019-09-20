def calculator(lower=1, upper=100):
    result = 0
    for i in range(lower, upper + 1):
        if i % 2 == 0:
            result += i
        else:
            pass
    print(result)
    return result
if __name__ == "__main__":
    calculator()