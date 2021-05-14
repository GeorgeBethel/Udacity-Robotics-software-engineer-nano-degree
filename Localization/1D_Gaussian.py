import math

def compute_gaussian(mu,sigma,state):

    prob = 1.0 /sigma * math.sqrt(2 * math.pi) * math.exp(- (state - mu)**2 / (2 * sigma**2))
    return prob


probability = compute_gaussian(10.0, 4.0, 8.0)

print(probability)