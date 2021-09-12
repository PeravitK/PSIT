"""[Midterm] Blackjack"""
def main():
    """[Midterm] Blackjack"""
    num = int(input())
    ans = 0
    ace1 = 0
    ace2 = 0
    for _ in range(num):
        card = input()
        if card.isnumeric() == True and 2 <= int(card) <= 10:
            ans += int(card)
        else:
            if card == "A":
                ace1 += 1
                ace2 += 1
            else:
                ans += 10
    for _ in range(ace1):
        if ace2 > 1 and ans <= 10:
            ans += 1
            ace2 -= 1
        elif ans <= 10:
            ans += 11
        else:
            ans += 1
    print(ans)
main()
