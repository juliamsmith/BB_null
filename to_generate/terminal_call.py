from Meta_Driver import vary_params
import numpy as np

if __name__ == "__main__":
    #this is what gets editted most of the time -- also potentially writer
    dist_vec=[117.2913514] #the equivalent of grid dim=[450, 900, 2250, 4500, 9000] 23.54644407, 46.93957688, 117.2913514, 234.06361069, 468.73044675
    m_prop_vec = np.linspace(.05, .95, 10)#numpy.linspace(.05, .95, 19) #.05, .1, .15, ... , .95; OR: intervals of .1
    RB_time_vec=[6] #hrs
    n_males_vec=[4,6,8,12,24]
    num_sims=1000
    max_m_vec=[0.054] #one succesful attempt a day
    vary_params(dist_vec, m_prop_vec, RB_time_vec, num_sims, max_m_vec, n_males_vec)