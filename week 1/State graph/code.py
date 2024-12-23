"""1 is a losing state
   2 is a winning state
   3 is a losing state
   4 is a winning state
   5 is a losing state
   6 is a winning state
   7 is a losing state
   8 is a winning state
   9 is a losing state
   10 is a winning state
   The optimal strategy is that always leave the opponent with an odd number of sticks"""


if __name__ == '__main__':
    n = int(input("Enter the number of sticks in a heap: "))
    if n % 2 == 0:
        odd_divisors=[a for a in range(1,n) if n%a==0 and a%2==1]
        print("The optimal strategy(s) are :")
        for a in odd_divisors:
            print(f"Remove {a} stick(s) from the heap and leave the opponent in a losing state")
    else:
        print("It is a losing state unless the opponent leave you with an even number of sticks")
