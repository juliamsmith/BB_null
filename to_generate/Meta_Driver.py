import os
import shutil
from Writer import in_write
#from Batch_func import BnS


def writebatchscript(num_sims, in_titles, out_titles, conditions_name):
    script=""
    for i in range(num_sims): #assume you call from inside to_run
        script+=("python3 bowerbird_prog.py ../to_store/{}/parameters/{}\n".format(conditions_name,in_titles[i]) + 
                 "mv {} ../to_store/{}/results/{}\n".format(out_titles[i],conditions_name,out_titles[i]))
    #make it run on the grid
    to_submit = ("#!/bin/bash" +
                 "\n#SBATCH -J " + conditions_name + 
                 "\n#SBATCH --time=07:00:00" +
                 "\n#SBATCH -p broadwl" + 
                 "\n#SBATCH --nodes=1" +
                 "\n#SBATCH --ntasks-per-node=1" + 
                 "\n\nmodule load Anaconda3/5.1.0\n" + 
                 script)
    return to_submit



def vary_params(dist_vec, m_prop_vec, RB_time_vec, num_sims, max_m_vec):
    for i in range(len(dist_vec)):
        male_dist = dist_vec[i]
        for k in range(len(RB_time_vec)):
            RB_time_val = RB_time_vec[k]
            for l in range(len(max_m_vec)):
                max_m_val=max_m_vec[l]
                [in_titles, out_titles, conditions_name] = in_write(male_dist, RB_time_val, num_sims, max_m_val)
#                 for l in in_titles:
#                     shutil.move(l, "{}/parameters".format(conditions_name))
                script=writebatchscript(num_sims, in_titles, out_titles, conditions_name)
                full_name="../to_run/{}.sh".format(conditions_name) #assumes it's in the to_generate file
                with open(full_name,"w") as f:
                    f.write(script)

                
                
                    
                    
                    
                #if for running them or producing batch scrut cakked 
                #####THIS IS THE UNIT WE WANT TO BE ONE BATCH (or so we thought): 1000 sims, 100 males, t_max 12*30 takes 6.67hrs or 24s/sim
                #in_write writes input files and creates a folder called conditions_name with param and res folders inside

                #writer puts them in a input folder.. try to run one input file tomorrow
#                 for l in range(len(in_titles)):
#                     in_title = in_titles[l]
#                     out_title = out_titles[l]
#                     os.system("python3 bowerbird_prog.py {}".format(in_title))
#                     # incorporate batch stuff properly -- BnS(script, JobName, queue=Q)
#                     # I believe 1000 sims (or one set of conditions) is a batch
#                     #perhaps the ideal script is the 1000sims (so just outside of this for loop)
                    
#                     shutil.move(out_title, "{}/results".format(conditions_name))
#                     #make it work in same way... os.system (move thefile)

#the batch script:                    
                    
#!/bin/bash
#SBATCH --job-name=conditions_name
#SBATCH --time=07:00:00
#SBATCH --partition=broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem-per-cpu=2000

#module load Anaconda3/5.1.0
#have a for loop that writes 1000 of these
    
