'''
Create different accounts, and transactions from each
'''

# Define the function to collect data
def create_bank():
    # Define the primary dictionary
    bank = {}

    # collect data for bank
    while True:
        account = input("Enter the name of the account (type 'done' to exit): ").strip()

        if account.lower() == 'done': 
            break

        if account not in bank:
            bank[account] = {} # create a key in the bank dictionary called account, set to an empty dictionary 

        while True: 
            trans_type = input("Enter a type of transaction (or type 'done' to exit): ").strip()

            if trans_type.lower() == 'done':
                break


            trans_amt = float(input("Enter the amount: "))
                
            # bank[account][trans_type] = trans_type
            bank[account][trans_type] = trans_amt

    print(f"\n{bank}\n") # Testing what has been entered see the dictionary
    return bank

def display_bank(bank):
    print("\nBank Accounts & Transactions\n")

    for account, trans_amt in bank.items():
        print(f"Account: {account}")

        for transaction, amount in trans_amt.items():
            print(f" - Amount: ${amount:.2f}")

bank_accounts = create_bank()

display_bank(bank_accounts)
