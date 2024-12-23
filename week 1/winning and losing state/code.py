if __name__=='__main__':
    n=int(input("Enter the number of sticks in a heap: "))
    if n%4==0:
        print("It is a losing state if the opponent plays optimally")
    else:
        print(f"Remove {n%4} sticks from the heap to leave the opponent in a losing state")