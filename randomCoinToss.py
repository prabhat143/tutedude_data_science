import random

# ------------------------------
# Part A: Tossing a coin 10,000 times
# ------------------------------
def coin_toss_simulation(trials=10000):
    heads = 0
    tails = 0
    
    for _ in range(trials):
        toss = random.choice(["H", "T"])
        if toss == "H":
            heads += 1
        else:
            tails += 1
    
    prob_heads = heads / trials
    prob_tails = tails / trials
    
    print("Coin Toss Simulation (10,000 trials)")
    print(f"Heads: {heads}, Probability: {prob_heads:.4f}")
    print(f"Tails: {tails}, Probability: {prob_tails:.4f}")
    print("-" * 50)


# ------------------------------
# Part B: Rolling two dice and computing probability of sum = 7
# ------------------------------
def dice_roll_simulation(trials=10000):
    sum_seven = 0
    
    for _ in range(trials):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 == 7:
            sum_seven += 1
    
    prob_sum_seven = sum_seven / trials
    
    print("Dice Roll Simulation (10,000 trials)")
    print(f"Sum = 7 occurred: {sum_seven} times")
    print(f"Experimental Probability of Sum = 7: {prob_sum_seven:.4f}")
    print("-" * 50)


# ------------------------------
# Run both simulations
# ------------------------------
if __name__ == "__main__":
    coin_toss_simulation()
    dice_roll_simulation()
