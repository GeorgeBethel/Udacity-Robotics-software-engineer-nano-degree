import math

motions =[1.0, 1.0, 2.0, 1.0, 1.0]

measurements = [5.0, 6.0, 7.0, 9.0, 10.0]

estimates = []
predictions = []

motion_sig = 2.0

measurement_sig = 4.0

intial_estimate =[35.0, 4.0] # [mu, sig] 

def measurement_update(prior_mu, prior_sig, measurement_mu, measurement_sig):
    
    new_mu = (measurement_sig * prior_mu +  prior_sig * measurement_mu) / (measurement_sig + prior_sig)
    
    new_sig = 1 / ((1 / measurement_sig) + (1 / prior_sig))
    
    return new_mu, new_sig

def prediction(prior_mu, prior_sig, motion_mu, motion_sig):

    pred_mu = prior_mu + motion_mu

    pred_sig = prior_sig + motion_sig 

    return pred_mu, pred_sig

def Kalma_fiter():

    new_estimate, new_sigma = measurement_update(intial_estimate[0], intial_estimate[1], measurements[0],measurement_sig)
    estimates.append(new_estimate)

    for m in range(len(measurements)):

        new_estimate, new_sigma = measurement_update(new_estimate, new_sigma, measurements[m], measurement_sig)

        prediction_mu, prediction_sig = prediction(new_estimate, new_sigma, motions[m],motion_sig)

        estimates.append(new_estimate)
        predictions.append(prediction_mu)

    print("predictions: ", predictions)
    print("estimates: ", estimates)


Kalma_fiter()

# new_mu, new_sig = measurement_update(20.0, 9.0, 30.0, 3.0)

# pred_mu, pred_sig = prediction(27.5, 2.25, 7.5, 5)

# print("new mu: ", new_mu, "new sig: ", new_sig)

# print("pred mu: ", pred_mu, "pred sig: ", pred_sig)