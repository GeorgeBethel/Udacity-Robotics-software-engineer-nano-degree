import math

def compute_gaussian(mu,sigma,state):

    prob = 1.0 /math.sqrt(2 * math.pi * sigma) * math.exp(-(state - mu)**2 / (2 * sigma))
    return prob


probability = compute_gaussian(10.0, 4.0, 8.0)

print(probability)