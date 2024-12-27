import __bot__.faucet.mangofaucet as mangofaucet
import __bot__.swap.perena.perenaNumeraire as perenaNumeraire

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

def swap_menu():
    # print("1. Perena Numerarire")
    print("No Bot Available")
    return

def main_menu():
    print("============= Anybot Menu =============")
    print("1. Bot faucet")
    print("2. Bot swap")
    choice = input("Choice bot type: ")
    
    if choice == "1":
        faucet_menu()
    if choice == "2":
        swap_menu()

if __name__ == "__main__":
    main_menu()
