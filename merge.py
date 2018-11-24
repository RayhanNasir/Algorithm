# Code for merge sort


def sorting(a1, a2):  # merging two list ( main work of merge_sort )
    x = a1.pop(0)
    y = a2.pop(0)
    lst = []

    while True:
        if x < y:
            lst.append(x)
            if len(a1) is 0:
                lst.append(y)
                lst += a2
                return lst
            x = a1.pop(0)

        else:
            lst.append(y)
            if len(a2) is 0:
                lst.append(x)
                lst += a1
                return lst
            y = a2.pop(0)


def main_process(ary):  # Main recursion call for merge_sort.
    if len(ary) <= 1:
        return ary

    a1 = ary[:(len(ary) // 2)]
    a2 = ary[(len(ary) // 2):]
    a1 = main_process(a1)
    a2 = main_process(a2)
    return sorting(a1, a2)


def merge_sort():
    try:
        # Code for taking an array as string
        array = input("Enter an array using ' ' as the separator  : ")
        ary = array.split()
        a = []

        # Code for making input string as integer
        for i in ary:
            a.append(int(i))
        print("\nInput : ", a, end="\n\n")

        # Code for calling main work's environment
        a = main_process(a)
        print("After merge sorting : ", a)

        # Code for making infinite loop using recursion.
        x = input("\nEnter X for exit : ")
        if x is not 'X':
            merge_sort()

    except Exception as e:
        print("Input Error..!\n", e)
        merge_sort()


# Def calling
merge_sort()
