import numpy
import math
from sortedcontainers import SortedDict
import random
import numpy 
import matplotlib.pyplot as plt
from scipy.stats import truncnorm
import os

def in_write(male_dist, RB_time_val, num_sims, max_m_val):
    #timeline = SortedDict()
    t_max = 12 * 30 # time when simulation ends

    # MALES
    males = 2 # number of male birds

    # FEMALES
    F_per_M = 9 #The number of sexualy mature females per sexually mature male
    females = males * F_per_M # number of female birds
    #BELOW: FV_std * truncnorm.rvs(FV_norm_range[0], FV_norm_range[1]) + FV_mean
    FV_std = t_max / 4 
    FV_mean = t_max / 2
    FV_range = [0, t_max]
    FV_norm_range =  [(FV_range[0] - FV_mean) / FV_std, (FV_range[1] - FV_mean) / FV_std]
    female_visit_param = [FV_std, FV_mean, FV_norm_range[0], FV_norm_range[1]]  

    # POSITIONS AND TRAVEL TIME
    #note male_dist=male_dist
    bird_speed = 12 * 3600 # m/hr (12 m/s)
    
    #Previously had preferance, but now only two birds, so not necessary
    # now choose lambda_dist, controlling the probability of traveling to a neighbor
    # the probability of choosing a neighbor at distance x is proportional to exp(-\lambda x)
    # choose lambda such that 99% of the mass is before 800 meters
    #improb_dist = 800
    #improb_sds = 2
    #if using exp decay
    #lambda_dist = - math.log(1.0 - improb) / improb_distance


    # ACTION DISTRIBUTIONS
    # Time of forage
    FG_tau_mean, FG_tau_std = .4, .167 #mean and sd of truncated normal distribution rv to find a male's time until next FG
    FG_tau_range = [0, 1] #maximum and minimum FG taus
    FG_tau_norm_range = [(FG_tau_range[0] - FG_tau_mean) / FG_tau_std, (FG_tau_range[1] - FG_tau_mean) / FG_tau_std] #normalized
    # Duration of forage
    FG_k=1.5 #the shape of the gamma distribution rv used to generate FG taus
    FG_theta=5 #the scale of the gamma distribution rv used to generate FG taus
    FG_divisor=60 #helps scale gamma distritbution
    # Duration of repair bower / stay at bower
    RBSB_tau_mean, RBSB_tau_std = .1583, .09755 #mean and sd of truncated normal distribution rv to find duration of repair bower / stay at bower
    RBSB_tau_range = [0,.5] #maximum and minimum taus
    RBSB_tau_norm_range = [(RBSB_tau_range[0] - RBSB_tau_mean) / RBSB_tau_std, (RBSB_tau_range[1] - RBSB_tau_mean) / RBSB_tau_std] #normalized
    
    time_spent_marauding=.1

    damage_to_bower = RB_time_val

    #Male strategies
    C_or_D='D'

    max_maraud=max_m_val
    
    #DISCRETE: 0, max_maraud
    #'numpy.random.random(males)*{}'.format(max_maraud) #UNIFORM DISTRIBUTION of strategies capped at max_maraud


    name_vec=['t_max', 
              'males', 
              'F_per_M', 
              'females', 
              'female_visit_param',
              'male_dist', 
              'bird_speed', 
              'FG_tau_mean', 
              'FG_tau_std',
              'FG_tau_range', 
              'FG_tau_norm_range', 
              'FG_k', 
              'FG_theta', 
              'FG_divisor',
              'RBSB_tau_mean', 
              'RBSB_tau_std', 
              'RBSB_tau_norm_range',
              'damage_to_bower',
              'time_spent_marauding',
              'max_maraud'
             ]
    value_vec=[t_max, 
              males, 
              F_per_M, 
              females, 
              female_visit_param, 
              male_dist,
              bird_speed, 
              FG_tau_mean, 
              FG_tau_std,
              FG_tau_range, 
              FG_tau_norm_range, 
              FG_k, 
              FG_theta, 
              FG_divisor,
              RBSB_tau_mean, 
              RBSB_tau_std, 
              RBSB_tau_norm_range,
              damage_to_bower,
              time_spent_marauding,
              max_maraud
             ]
    in_titles=[]
    out_titles=[]
    conditions_name='{}_pmar={}_dim={}_repair_{}'.format(C_or_D,max_maraud,round(male_dist,3),damage_to_bower)
    os.makedirs("../to_store/{}".format(conditions_name))
    os.makedirs("../to_store/{}/parameters".format(conditions_name))
    os.makedirs("../to_store/{}/results".format(conditions_name))
    for j in range(num_sims):
        correcter=''
        if j<10:
            correcter='0'
        out_title='res_{}{}'.format(correcter,j) + conditions_name + '.csv'
        out_titles.append(out_title)
        my_string=('random_seed = ' + str(j) + '\n'+
                   'out_title = ' +  "'" + out_title + "'" + '\n')
        for i in range(len(name_vec)):
            tack_on= str(name_vec[i]) + ' = ' + str(value_vec[i]) + '\n'
            my_string+=tack_on
        in_title='in_{}{}'.format(correcter,j) + conditions_name
        in_titles.append(in_title)
        with open("../to_store/{}/parameters/{}".format(conditions_name, in_title),"w") as f:
            f.write(my_string)
    return [in_titles, out_titles, conditions_name]


#for j in range(num_sims):
#    os.remove("in_{}_{}_strat={}_dim={}_repair={}".format(j,C_or_D,max_maraud,x_dim,damage_to_bower))
    