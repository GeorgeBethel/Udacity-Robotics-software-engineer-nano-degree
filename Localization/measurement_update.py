import math

def measurement_update(prior_mu, prior_sig, measurement_mu, measurement_sig):
    
    new_mu = (measurement_sig * prior_mu +  prior_sig * measurement_mu) / (measurement_sig + prior_sig)
    
    new_sig = 1 / ((1 / measurement_sig) + (1 / prior_sig))
    
    return new_mu, new_sig

def prediction(prior_mu, prior_sig, motion_mu, motion_sig):

    pred_mu = prior_mu + motion_mu

    pred_sig = prior_sig + motion_sig 

    return pred_mu, pred_sig

new_mu, new_sig = measurement_update(20.0, 9.0, 30.0, 3.0)

pred_mu, pred_sig = prediction(27.5, 2.25, 7.5, 5)

print("new mu: ", new_mu, "new sig: ", new_sig)

print("pred mu: ", pred_mu, "pred sig: ", pred_sig)