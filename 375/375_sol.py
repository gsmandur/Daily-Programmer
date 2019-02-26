# problem at:
# https://www.reddit.com/r/dailyprogrammer/comments/aq6gfy/20190213_challenge_375_intermediate_a_card/

# Returns the order of cards to flip to clear all cards
# Recursive backtracking solution
# A solution only exists if there is an odd # of face up cards

flipMap = {'.': '.', '0': '1', '1': '0'}

# input: string of 0's and 1's
# output: print order of cards to flip, or 'no solution' if can't complete game
def cardFlipGame(cards: str):
    cardsList = list(cards)
    # count # of face up cards
    numFaceUpCards = 0
    for c in cardsList:
        if c == '1':
            numFaceUpCards+= 1

    # if even number of face up cards, no solution exists
    if numFaceUpCards % 2 == 0:
        print("no solution")

    # if odd, find ordering
    else:
        orderList = []
        if cardFlipHelper(cardsList, orderList) == True:
            print(orderList)
        else:
            print("no solution")

# Recursive backtracking soluiton
# input: list of chars and list of ints
# return true of false if solution is found
def cardFlipHelper(cardsList: list, orderList: list):
    # print(cardsList)
    n = len(cardsList)
    # base case - all elements filled
    if len(orderList) == n:
        return True

    # remove available cards
    for i in range(n):
        if cardsList[i] == '1':
            swapCard(cardsList, i, '.')
            orderList.append(i)
            # recurse
            if cardFlipHelper(cardsList, orderList) == True:
                return True

            # backtrack
            swapCard(cardsList, i, '1')
            del orderList[-1]

    # when through each card without a success
    return False

# swap the given card with the new value, and flip its neigbours
def swapCard(cardsList: list, pos: int, newChar):
    #set card
    cardsList[pos] = newChar

    # flip neighbours
    flip(cardsList, pos-1)
    flip(cardsList, pos+1)

# flip the card at position pos using the map
def flip(cardsList: list, pos: int):
    if 0 <= pos < len(cardsList):
        cardsList[pos] = flipMap[cardsList[pos]]


def main():
    # sample inputs
    cardFlipGame("0100110")
    cardFlipGame("01001100111")
    cardFlipGame("100001100101000")

    # challange inputs
    cardFlipGame("001011011101001001000")
    cardFlipGame("1010010101001011011001011101111")
    cardFlipGame("1101110110000001010111011100110")
main()
