from week2.Grundy_Number.MEX import Calculate_MEX

"""The game starts with a pile of n stones,
 and the player to move may take any positive number of stones up to 3 only"""
def Grundy(n):
    if n<4:
        possible_options_opponent=[n-i for i in range(1,n+1)]
        return Calculate_MEX(possible_options_opponent).calculate_value()
    else:
        return Calculate_MEX([Grundy(n-1),Grundy(n-2),Grundy(n-3)]).calculate_value()

n=int(input("Enter number of stones in pile: "))
if n==0:
    print("No stone to pick.")
if Grundy(n)==0:
    print("Whatever number i you will pick, the opponent will always pick 4-i and leave you in the loosing state")
else:
    print(f"Pick {Grundy(n)} number of stones and leave the opponent in a losing state ")
