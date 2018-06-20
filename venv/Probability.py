import copy




def prob(n):
    final = []
    # helper function; interpreted languages?
    def prob_helper(array, index):
        i = index
        while i <= len(array) - 1:
            list_tmp = copy.deepcopy(array)
            list_tmp[i] = not list_tmp[i]
            i += 1
            prob_helper(list_tmp, i)
            final.append(list_tmp)

    list_tmp = [False] * n
    print(list_tmp)
    final.append(list_tmp)
    prob_helper(list_tmp, 0)
    return final


print(str(prob(4)) + "\n" + "List's length is : " + str(len(prob(4))))