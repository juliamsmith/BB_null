from Meta_Driver import vary_params
import numpy

if __name__ == "__main__":
    #this is what gets editted most of the time -- also potentially writer
    dist_vec=[23.54644407, 46.93957688, 117.2913514, 234.06361069, 468.73044675] #the equivalent of grid dim=[450, 900, 2250, 4500, 9000]
    m_prop_vec=numpy.linspace(.05, .95, 10)#numpy.linspace(.05, .95, 19) #.05, .1, .15, ... , .95; OR: intervals of .1
    RB_time_vec=[6] #hrs
    num_sims=1
    max_m_vec=[.018]
    vary_params(dim_vec, m_prop_vec, RB_time_vec, num_sims, max_m_vec)