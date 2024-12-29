
from week2.Grundy_Number.MEX import Calculate_MEX

"""The game starts with a pile of n stones,
 and the player to move may take any positive number of stones."""
def Grundy(n):
    possible_position_for_opponent=[n-i for i in range(1,n+1)]
    return Calculate_MEX(possible_position_for_opponent).calculate_value()
n=int(input("Enter number of stones in pile: "))

if n==0:
    print("Losing State, as there are no stones to pick.")
else:
    print(f"Pick {Grundy(n)} number of stones and leave the opponent in a losing state ")
