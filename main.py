import random 

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

symbol_count = {
    '🍒': 2,
    '🍊': 3,
    '🍇': 4,
    '🍉': 5,
    '🍍': 6,
}

symbol_values = {
    '🍒': 5,
    '🍊': 4,
    '🍇': 3,
    '🍉': 2,
    '🍍': 1,
}

def check_for_winning_lines(spin, number_of_lines, bet, values):
    total_winnings = 0
    for line in range(number_of_lines):
        if spin[0][line] == spin[1][line] and spin[1][line] == spin[2][line]:
            symbol_value = values[spin[0][line]]
            winnings = bet * symbol_value
            total_winnings += winnings
            print(f'You won ${winnings} on line {line + 1}!')

    return total_winnings

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols.copy()
        for _ in range(rows):
            value = random.choice(current_symbols)
            # remove the symbol from the list so it can't be chosen again
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)

    return columns

def print_slot_machine_spin(spin):
    for row in range(ROWS):
        print('|', end='')
        for column in range(COLS):
            # not spacing out the last column
            if column == COLS - 1:
                print(spin[column][row], end='|')
            else:
                print(spin[column][row], end=' | ')
        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please enter a positive amount.")
        else:
            print("Please enter a valid amount.")

    return amount

def get_number_of_lines():
    while True:
        number_of_lines = input("How many lines would you like to bet on (1-" + str(MAX_LINES) + ")? ")
        if number_of_lines.isdigit():
            number_of_lines = int(number_of_lines)
            if number_of_lines > 0 and number_of_lines <= MAX_LINES:
                break
            else:
                print("Please enter a number between 1 and " + str(MAX_LINES) + ".")
        else:
            print("Please enter a valid number.")

    return number_of_lines

def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if bet >= MIN_BET and bet <= MAX_BET:
                break
            else:
                print("Please enter a bet between $" + str(MIN_BET) + " and $" + str(MAX_BET) + ".")
        else:
            print("Please enter a valid bet.")

    return bet

def add_balance(balance, winnings):
    balance += winnings
    return balance

def game():
    balance = deposit()
    # add money to previous balance
    print("Welcome to the slot machine game!")
    print("You have $" + str(balance) + " to play with.")
    number_of_lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = number_of_lines * bet

        if total_bet > balance:
            print(f'You do not have enough money to bet ${total_bet}. You only have ${balance}.')
        else:
            break

    print(f'You are betting ${bet} on {number_of_lines} lines. Your total bet is ${total_bet}.')

    spin = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_spin(spin)
    winnings = check_for_winning_lines(spin, number_of_lines, bet, symbol_values)

    balance = add_balance(balance, -total_bet)
    balance = add_balance(balance, winnings)
    print(f'You now have ${balance}.')

    return balance

def main():
    while True:
        spin = input("Would you like to spin the slot machine? (y/n). ")
        if spin == 'y':
            balance = game()
            if balance <= 0:
                print("You are out of money!")
                break
        elif spin == 'n':
            print("Thanks for playing!")
            break
        else:
            print("Please enter a valid option.")    

main()

