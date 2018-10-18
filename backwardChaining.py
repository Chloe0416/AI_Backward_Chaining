def backward_chaining(kb, goals):
    print("The goal now is: " + goals)
    for rule in kb:
        head = rule[0]
        if head == goals[0]:
            print("Check: " + head)
            if len(rule) == 1:
                print("[" + goals + "] is known to be true.")
                return True
            new_goal = rule[1:]
            print("[" + new_goal + "] => [" + goals + "]")
            for x in range(len(new_goal)):
                if backward_chaining(kb, new_goal[x]):
                    print("[" + new_goal[x] + "] is proving [" + head + "]")
                    if len(new_goal) == 1:
                        return True
                elif not rule == kb[-1]:
                    new_kb = kb
                    new_kb.remove(rule)
                    if backward_chaining(new_kb, goals):
                        return True
                else:
                    print("[" + new_goal[x] + "] fails, so [" + head + "] is false.")
                    return False
        elif rule == kb[-1]:
            print("We have not enough knowledge to show [" + goals + "] is true or false.")
    return False


file = input("Please enter your file containing rules: ")
rules_file = open(file, "r")
get_rules = rules_file.readlines()
size = len(get_rules)

rules_file.close()

rules = [" "] * size
for i in range(size):
    length = len(get_rules[i])
    actural_len = 0
    for j in range(length):
        if get_rules[i][j] in "abcdefghijklmnopqrstuvwxyz":
            actural_len += 1
    rules[i] = [" "] * actural_len
    y = 0
    for j in range(length):
        if get_rules[i][j] in "abcdefghijklmnopqrstuvwxyz":
            rules[i][y] = get_rules[i][j]
            y += 1

for i in range(size):
    rules[i] = ''.join(rules[i])

print("Our knowledge base is: ")
for line in rules:
    print("[" + line + "]")

queries = input("Please enter your queries: ")

for i in queries:
    for j in range(size):
        if i in rules[j]:
            if i == rules[j][0]:
                if backward_chaining(rules, i):
                    print("From rule [" + rules[j] + "] shows that your query [" + i + "] is true.")
                    break
                else:
                    print("Your query [" + i + "] fails because rule [" + rules[j] + "] fails.")
                    break
            elif j == size - 1:
                print("Sorry, we have not enough rules to show your query [" + i + "] is true or false.")
        elif j == size - 1:
            print("Your query [" + i + "] is not in the knowledge base. Cannot tell true or false.")

