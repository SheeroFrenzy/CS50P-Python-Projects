command = input("What is the Answer to the Great Question of Life, the Universeand Everything? ").strip().lower()
match command:
    case "42"|"forty-two"|"forty two":
        print("Yes")
    case _:
        print("No")

