import __bot__.faucet.mangofaucet as mangofaucet

def faucet_menu():
    print("1. Mango faucet")
    faucet_choice = input("Choice bot faucet:")

    if faucet_choice == "1":
        env_choice = input("ENV (1 Devnet, 2 Testnet): ")
           
        if env_choice == "1":
            env = "devnet"
        elif env_choice == "2":
            env = "testnet"
        else:
            print("Invalid input!")
            return
            
        address = input("Address: ")
        mangofaucet.mangoFaucet(env, address)
    else:
        print("Invalid input!")

def main_menu():
    print("============= Anybot Menu =============")
    print("1. Bot faucet")
    choice = input("Choice bot type: ")
    
    if choice == "1":
        faucet_menu()

if __name__ == "__main__":
    main_menu()
