import mangofaucet

def main_menu():
    print("============= Anybot Menu =============")
    print("1. Bot faucet Mangowallet")
    choice = input("Pilih menu: ")
    
    if choice == "1":
        env_choice = input("ENV (1 untuk Devnet, 2 untuk Testnet): ")
        
        if env_choice == "1":
            env = "devnet"
        elif env_choice == "2":
            env = "testnet"
        else:
            print("Pilihan ENV tidak valid!")
            return
        
        address = input("Address: ")
        mangofaucet.mangoFaucet(env, address)
    else:
        print("Pilihan menu tidak valid!")

if __name__ == "__main__":
    main_menu()
