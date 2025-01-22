import __bot__.faucet.mangofaucet as mangofaucet
# import __bot__.swap.perena.perenaNumeraire as perenaNumeraire
import __bot__.others.fraction as fraction

def main_menu():
    print("============= Anybot Menu =============")
    print("1. Mango faucet")
    print("2. Fraction initiate")
    faucet_choice = input("Choice bot faucet : ")

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
    elif faucet_choice == "2":
        userid = input("Please input user id : ")
        token = input("Please input token : ")
        print(f'Lets run with user id {userid}')
        fraction.fraction(token, userid)
    else:
        print("Invalid input!")
        
if __name__ == "__main__":
    main_menu()
