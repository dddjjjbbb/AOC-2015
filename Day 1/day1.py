from data import brackets


def whichLevel(brackets):
    up = sum(1 for x in brackets if x == '(')
    down = sum(-1 for x in brackets if x == ')')
    return(up + down)

print(whichLevel(brackets))


def firstCharacterResultingInBasement(brackets):
    counter = 0
    for i, bracket in enumerate(brackets, 1):
        counter += (1 if bracket == '(' else -1)
        if counter == -1:
            return(i)
            break

print(firstCharacterResultingInBasement(brackets))
