import sys
def main():
    name=sys.argv[1]
    balance=float(sys.argv[2])
    deposit=float(sys.argv[3])
    withdraw=float(sys.argv[4])
    
    new_balance=balance+deposit-withdraw
    print("Name:", name)
    print("Balance:", new_balance)
    print("Deposit:", deposit)
    print("Withdrawal:", withdraw)
if __name__=="__main__":
    main()