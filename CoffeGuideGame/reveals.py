import os
def reveals(cup1,cup2):
    os.system("cls")
    print("You Win")
    header = " Your Cup : Needed Cup"
    w1 = max((len(str(x)) for x in cup1), default=1)
    w2 = max((len(str(x)) for x in cup2), default=1)
    total = max(len(header), w1 + 3 + w2)
    print(header.center(total))
    print("-" * total)
    max_len = max(len(cup1), len(cup2))
    for i in range(max_len):
        a = str(cup1[i]) if i < len(cup1) else ""
        b = str(cup2[i]) if i < len(cup2) else ""
        print(f"{a:^{w1}} | {b:^{w2}}")

def reveals_lose(cup1,cup2):
    os.system("cls")
    print("Game Over You Wrong")
    header = " Your Cup : Needed Cup"
    w1 = max((len(str(x)) for x in cup1), default=1)
    w2 = max((len(str(x)) for x in cup2), default=1)
    total = max(len(header), w1 + 3 + w2)
    print(header.center(total))
    print("-" * total)
    max_len = max(len(cup1), len(cup2))
    for i in range(max_len):
        a = str(cup1[i]) if i < len(cup1) else ""
        b = str(cup2[i]) if i < len(cup2) else ""
        print(f"{a:^{w1}} | {b:^{w2}}")
    