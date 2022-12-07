file = input("Type in the name of the file to test: ")

dataset = []
with open(file, 'r') as f:
    for line in f:
        thing = []
        for number in line.split():
            thing.append(float(number))
        dataset.append(thing)


features = len(dataset[0]) - 1

algorithm = int(input("Enter algorithm choice: 1)Forward Selection 2) Backwards Elimination "))

if algorithm == 1:
    forwardSelection(dataset)

if algorithm == 2:
    backwardElimination(dataset)
