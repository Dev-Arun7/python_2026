"""
--------------------------------------------------
SIMPLE SLOT MACHINE GAME 🎰
--------------------------------------------------

🧠 Game Rules:

1. Player starts with $100 balance.
2. Player enters bet amount.
3. 5 random symbols will spin.
4. Minimum 3 matching symbols required to win.
5. Payout system:
      - 5 same  → bet × 100  (JACKPOT)
      - 4 same  → bet × 50
      - 3 same  → bet × 10
      - Less than 3 → No win
6. Game continues until player exits or balance becomes 0.

Symbols used:
🍎 Apple
🍉 Watermelon
🍌 Banana
🍇 Grape
⭐ Star
--------------------------------------------------
"""

import random


# Generate 5 random symbols
def spin_row():
    symbols = ["🍎", "🍉", "🍌", "🍇", "⭐"]

    # Using list comprehension (short and clean way)
    return [random.choice(symbols) for _ in range(5)]

    # ---------------- Traditional for loop ----------------
    # row = []
    # for i in range(5):
    #     random_symbol = random.choice(symbols)
    #     row.append(random_symbol)
    #
    # return row


# Display the row nicely
def print_row(row):
    print(" | ".join(row))


# LOGIC METHOD: Calculate winnings
def calculate_payout(bet, row):
    """
    This function calculates how much the player wins based on the spun symbols.
    Rules:
      - Minimum 3 symbols must match to win.
      - 3 same → 5x bet
      - 4 same → 10x bet
      - 5 same → 50x bet
    If less than 3 match → player loses the bet (win = 0)
    """

    # Step 1: Count how many times each symbol appears
    counts = {}  # dictionary to store symbol:count
    for symbol in row:
        if symbol in counts:
            counts[symbol] += 1  # if symbol already in dict, increase count
        else:
            counts[symbol] = 1   # first time symbol appears, set count = 1

    # Step 2: Find the symbol with the highest occurrence
    max_match = max(counts.values())  # gives the highest number of same symbols

    # Step 3: Determine payout based on highest match
    if max_match == 5:
        # All 5 symbols are same → Jackpot
        print("🎉 JACKPOT! 5 symbols matched!")
        return bet * 50

    elif max_match == 4:
        # 4 symbols match → Big win
        print("🔥 4 symbols matched!")
        return bet * 10

    elif max_match == 3:
        # 3 symbols match → Small win
        print("🙂 3 symbols matched!")
        return bet * 5

    else:
        # Less than 3 match → No win
        print("😢 No winning combination.")
        return 0


# Main game controller
def main():

    balance = 100  # Starting balance
    print("-------- 🎰 Welcome to the Slot Game -------")
    print(f"Balance : {balance}")

    while balance > 0:

        print(f"\nCurrent Balance: ${balance}")

        bet = int(input("Enter your bet amount (0 to exit): "))

        if bet == 0:
            print("👋 Exiting game...")
            break

        if bet <= 0:
            print("❌ Bet must be greater than 0.")
            continue

        if bet > balance:
            print("❌ Insufficient balance.")
            continue

        # Deduct bet first
        balance -= bet

        # Spin
        row = spin_row()
        print("\nSpinning...")
        print_row(row)

        # Calculate winnings
        winnings = calculate_payout(bet, row)

        # Add winnings back
        balance += winnings
        print(f"Current Balance: {balance}")

    print(f"\nGame Over. Final Balance: ${balance}")


# Dunder Method
if __name__ == "__main__":
    main()