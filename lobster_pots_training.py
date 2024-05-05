import random, math
learning_rate = 0.25
weights = [[random.random(), random.random(), random.random(), random.random(),],
           [random.random(), random.random(), random.random(), random.random(),],
           [random.random(), random.random(), random.random(), random.random(),],]

def activate(actiate_neurone):
    return 1/(1 + (math.e ** -activate_neurone))

def sum_%buy_pots
    
def buy_pots(buy_bank, buy_pot_total, buy_price, buy_pot_percentage):
    pots_purchased = round(buy_pot_percentage * (buy_bank // buy_price))     
    buy_bank -= pots_purchased * buy_price
    buy_pot_total += pots_purchased
    buy_price = 2
    return buy_bank, buy_pot_total, buy_price

def distribute_pots(distribute_pot_total, %distribute_pots_shore, %distribute_pots_bay):
    distribute = []
    distribute.append(distribute_pot_total * %distribute_pots_shore)  
    if %distribute_pots_bay + %distribute_pots_shore > 1:
        %distribute_pots_bay = 1 - %distribute_pots_shore
    distribute.extend([distribute_pot_total * %distribute_pots_bay, (1 - %distribute_pots_shore - %distribute_pots_bay) * distribute_pots_total])
    return distribute, %distribute_pots_bay

def roll_dice():
    dice = random.randint(0,2)
    if dice == 2:
        dice = random.randint(2,7)
    print(['Calm', 'Stormy', 'Pot Raid', 'Taxation', 'Bank Raid', 'Price Hike', 'Gale', 'Severe Storm'][dice])
    return dice

def outcome(outcome_bank, outcome_distribution, outcome_price, outcome_weather):
    outcome_difference = sum(outcome_distribution)
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
        return outcome_bank + outcome_distribution[1] * 1 + outcome_distribution[2] * 3, outcome_distribution, outcome_price, outcome_difference - sum(outcome_distribution)
    elif outcome_weather == 1:
        outcome_distribution[2] = 0
        return outcome_bank + outcome_distribution[1] * 2, outcome_distribution, outcome_price

bank = 20
pots = 0
price = 2
for i in range(0,10):
    bank, pots, price = buy_pots(bank, pots, price, %buy_pots)
    distribution, %bay_pots = distribute_pots(pots, %shore_pots, %bay_pots)
    weather = roll_dice()
    bank, distribution, price, pot_difference = outcome(bank, distribution, price, weather)
    pots = sum(distribution)

