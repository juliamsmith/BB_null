def namewrite(C_or_D,max_maraud,prop_maraud,x_dim,damage_to_bower, j): #j is the random seed
    in_titles=[]
    out_titles=[]
    conditions_name='{}_strat={}_pmar={}_dim={}_repair_{}'.format(C_or_D,max_maraud,prop_maraud,x_dim,damage_to_bower)
    correcter=''
    if j<10:
        correcter='0'
    out_title='res_{}{}'.format(correcter,j) + conditions_name + '.csv'
    in_title='in_{}{}'.format(correcter,j) + conditions_name
    return [in_title, out_title, conditions_name]


def writescript(in_titles, out_titles, conditions_names):
    script=""
    num_sims=len(in_titles)
    for i in range(num_sims): #assume you call from inside to_run
        script+=("python3 bowerbird_prog.py ../to_store/{}/parameters/{}\n".format(conditions_names[i],in_titles[i]) + 
                 "mv {} ../to_store/{}/results/{}\n".format(out_titles[i],conditions_names[i],out_titles[i]))
    return script

rands=[]
in_titles=[]
out_titles=[]
conditions_names=[]
C_or_D='D'
max_maraud=.009 #changes
prop_maraud=.95 #changes
nums=range(924,1000) #changes
x_dim=2250
damage_to_bower=4
for j in nums:
    names=namewrite(C_or_D,max_maraud,prop_maraud,x_dim,damage_to_bower, j)
    rands.append(j)
    in_titles.append(names[0])
    out_titles.append(names[1])
    conditions_names.append(names[2])

max_maraud=.018 #changes
prop_maraud=.05 #changes
nums=range(927,1000) #changes    
for j in nums:
    names=namewrite(C_or_D,max_maraud,prop_maraud,x_dim,damage_to_bower, j)
    rands.append(j)
    in_titles.append(names[0])
    out_titles.append(names[1])
    conditions_names.append(names[2])
    
prop_maraud=.15 #changes
nums=range(925,1000) #changes    
for j in nums:
    names=namewrite(C_or_D,max_maraud,prop_maraud,x_dim,damage_to_bower, j)
    rands.append(j)
    in_titles.append(names[0])
    out_titles.append(names[1])
    conditions_names.append(names[2])
    
prop_maraud=.25 #changes
nums=range(925,1000) #changes    
for j in nums:
    names=namewrite(C_or_D,max_maraud,prop_maraud,x_dim,damage_to_bower, j)
    rands.append(j)
    in_titles.append(names[0])
    out_titles.append(names[1])
    conditions_names.append(names[2])

script=writescript(in_titles, out_titles, conditions_names)

full_name="../to_run/missed.sh" #assumes it's in the to_generate file
with open(full_name,"w") as f:
    f.write(script)