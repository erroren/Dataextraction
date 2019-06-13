import random


def getrandom(list1):
    a =random.randint(0, len(list1)-1)
    return list1[a]


if __name__ == "__main__":
    with open('./ip1.csv') as file1:
        a = file1.read()
    a1 = a.split('\n')
    list1 = []
    for i in range(len(a1)-1):
        list1.append(a1[i].split(',')[1])
    print("随机IP"+getrandom(list1))
