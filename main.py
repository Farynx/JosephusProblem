# This program will implement the josephusProblem and output list of
# unlucky individuals and a value of the lucky one
# Made by: Ferencz Dominguez

def josephus(nbrPeople, stepSize):

    index = stepSize - 1
    stepSize -= 1

    print('Dead people:')
    while (len(nbrPeople) > 1):
        print(nbrPeople.pop(index))
        index = (stepSize + index) % len(nbrPeople)
    print('Last man standing: ', nbrPeople.pop(0))

nbrPeople = list(range(1, 10+1))
stepSize = 3

josephus(nbrPeople, stepSize)