import fileinput

def part1(input):
    cal_by_mice = []
    temp = 0
    for line in input:
        if line == "":
            cal_by_mice.append(temp)
            temp = 0
        else:
            temp += int(line)

    max1 = max(cal_by_mice)
    return max1

def part2(input):
    cal_by_mice = []
    temp = 0
    for line in input:
        if line == "":
            cal_by_mice.append(temp)
            temp = 0
        else:
            temp += int(line)

    max1 = max(cal_by_mice)
    cal_by_mice.remove(max1)

    max2 = max(cal_by_mice)
    cal_by_mice.remove(max2)

    max3 = max(cal_by_mice)

    return max1 + max2 + max3

if __name__ == "__main__":
    input = [line.strip() for line in fileinput.input()]

    print(f"Response part 1: {part1(input)}")
    print(f"Response part 2: {part2(input)}")
