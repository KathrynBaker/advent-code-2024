from collections import Counter

available_string = "r, wr, b, g, bwu, rb, gb, br"
available = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"]
available_3 = ["bwu"]
available_2 = ["wr", "rb", "gb", "br"]
available_1 = ["r", "b", "g"]
max_available = 3

looking_for = "brwrr"
chars_looking_for = ["b", "r", "w"]

chars_available = Counter(available_string).keys()

target = len(looking_for)
count = 0
for char in looking_for:
    print(char)
    if char not in chars_available:
        print("Nope, not here, this is impossible")
        break
    if char in available:
        print("Available on own")
        count += 1

print(count)

if count == target:
    print("Possible, great")
else:
    print("Need to go to next level")

    check_len = 1
    count = 0
    for i in range(target):
        if looking_for[i:i+check_len] in available:
            print(f"I have {looking_for[i:i+check_len]} available")
            count += check_len
        else:
            print(f"{looking_for[i:i+check_len]} isn't available")
    print(f"I've gotten to a length of {count} with {check_len}")

    # todo
    # This is certainly a recursion type thing, I like having the quick check for any unavailable colours
    # but I think I need to do the checks in reverse order, as the longer the better

    check_len = max_available


