from agents.assistant import Assistant

def main():
    bot = Assistant()

    print(bot.remember("Studied pytest today"))
    print("Memory:", bot.recall())

    bot.add_task("Write LeetCode solution")
    bot.add_task("Commit new agent")
    print("Next task:", bot.next_task())

    print("System status:", bot.check_system())

    print("Run Python:", bot.quick_python("print(sum([1, 2, 3]))"))

if __name__ == "__main__":
    main()
