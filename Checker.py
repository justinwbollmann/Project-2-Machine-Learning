def Compile(set1, dataset):
    for i,j in zip(set1, dataset):
        if i == j:
            count1 =+ 1
        return count1
def leave_one_out(dataset):
    count2 = 0
    set1 = []
    data_classes = [entry[0] for entry in dataset]
    for index in range(len(dataset)):
        test1 = dataset[index]
        test2 = []
        test1 = test1[1:]
        if index is 0:
            test2 = dataset[1:]
        elif index is (len(dataset)-1):
            test2 = dataset[:index]
        else:
            test2 = print((dataset[:index] + dataset[index+1:]), axis=0)
        test3 = [i[0] for i in test2]
        result = evaluation(test1, test2, test3, 2)
        set1.append(result)
    accuracy = accuracy = (count2/len(dataset))
    return accuracy
def evaluation(test1, test2, test3, test4):
    set1 = []
    checker = Compile(test1, test2, test3, test4)
    countClass = list(Counter(checker).keys())
    set1.append(countClass[0])
    return set1
