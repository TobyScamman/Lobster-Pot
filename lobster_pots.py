import random, math

def buy_pots(buy_bank, buy_pot_total, buy_price):
    try:
        pots_purchased = int(input(f'You have £{buy_bank}. How many pots would you like to buy? '))
        while pots_purchased > buy_bank / buy_price: 
            pots_purchased = int(input(f'Invalid. How many pots would you like to buy? '))
        buy_bank -= pots_purchased * buy_price
        buy_pot_total += pots_purchased
        buy_price = 2
        return [buy_bank, buy_pot_total, buy_price]
    except:
        return buy_pots(buy_bank, buy_pot_total, buy_price)

def distribute_pots(distribute_pot_total):
    try:
        distribute = list(map(int, input(f'How would you like to distribute your {distribute_pot_total} pots, on shore, in the bay or at sea? ').split())) #converts 0 3 7 into a list of integers
        while sum(distribute) != distribute_pot_total or len(distribute) != 3:
            distribute = list(map(int, input('Invalid. How would you like to distribute your pots, on shore, in the bay or at sea? ').split())) #converts 0 3 7 into a list of integers
        return distribute
    except:
        return distribute_pots(distribute_pot_total)

def roll_dice():
    dice = random.randint(0,2)
    if dice == 2:
        dice = random.randint(3,8)
    print(['Calm', 'Stormy', '', 'Pot Raid', 'Taxation', 'Bank Raid', 'Price Hike', 'Gale', 'Severe Storm'][dice])
    return dice

def outcome(outcome_bank, outcome_distribution, outcome_price, outcome_weather):
    match outcome_weather:
        case 3: #pot raid
            outcome_distribution[0] == 0
            outcome_weather = 0
        case 4: #taxation
            outcome_bank = outcome_bank + (outcome_bank - 100) // 2 if outcome_bank > 100 else 0
            outcome_weather = 0
        case 5: #bank raid
            outcome_bank = 0
            outcome_weather = 0
        case 6: #price hike
            outcome_price = 4
            outcome_weather = 0
        case 7: #gale
            outcome_distribution[1] = math.ceil(outcome_distribution[1] / 2)
            outcome_distribution[2] = 0
            outcome_weather = 1
        case 8: #severe storm
            outcome_distribution[1], outcome_distribution[2] = [0,0]
            return [outcome_bank, outcome_distribution, outcome_price]
    if outcome_weather == 0:
        return [outcome_bank + outcome_distribution[1] * 1 + outcome_distribution[2] * 3, outcome_distribution, outcome_price]
    elif outcome_weather == 1:
        outcome_distribution[2] = 0
        return [outcome_bank + outcome_distribution[1] * 2, outcome_distribution, outcome_price]

bank = 20
pots = 0
price = 2
for i in range(0,9):
    bank, pots, price = buy_pots(bank, pots, price)
    distribution = distribute_pots(pots)
    weather = roll_dice()
    bank, distribution, price = outcome(bank, distribution, price, weather)
    pots = sum(distribution)
print(f'You finished with {pots} pots, so your total is £{bank + pots * 2}')
