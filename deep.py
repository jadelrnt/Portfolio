answer = input("What is the Answer to the Great Question of Life, the Universe and Everything ? ")
answer = answer.lower().strip()
match answer:
    case "42" | "forty-two" | "forty two" | "Forty Two":
        print("Yes")
    case _:
        print("No")
