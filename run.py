#This page contains interface used to test the typing bot, the scirpt which does the typing is in bot.custom_typer

from bot.test_bot import TestTyping

def main():
    while True:
        print("\nChoose a typing test website:")
        print( " "+"_"*40)
        print("|\t1.\t typing.com")
        print("|\t2.\t ratatype.com")
        print("|\t3.\t livechat.com")
        print("|\t4.\t 10fastfingers.com")
        print("|\t5.\t speedytypingonline.com")
        print("|\t6.\t typing-speed.net")
        print("|\t7.\t keyhero.com")
        print("|\t8.\t w3schools.com")
        print("|\t9.\t thetypingcat.com")
        print("|\t10.\t Create you own Bot...")
        print("|\t0.\t Exit")
        print("|"+"_"*40)

        choice = input("Enter your choice (0-10): ")

        if choice == "0":
            print("\nExiting Typing Bot... Goodbye!\n")
            break

        speed = float(input("Enter the maximum sleep time between keystrokes (e.g., 0.097): "))
        typing_bot = TestTyping(speed)

        if choice == "1":
            typing_bot.typing_com_typer()
        elif choice == "2":
            typing_bot.ratatype_typer()
        elif choice == "3":
            typing_bot.livechat_com_typer()
        elif choice == "4":
            typing_bot.ten_fast_fingers_typer()
        elif choice == "5":
            typing_bot.speedy_typing_online_typer()
        elif choice == "6":
            typing_bot.typing_speed_net_typer()
        elif choice == "7":
            typing_bot.keyhero_typer()
        elif choice == "8":
            typing_bot.w3schools_typer()
        elif choice == "9":
            typing_bot.thetypingcat_com_typer()
        elif choice == "10":
            typing_bot.custom_typing_bot()
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")

if __name__ == "__main__":
    main()


