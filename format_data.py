import pandas
from collections import defaultdict 
import os

parent_dir = "/"
data=pandas.read_csv('../validated.tsv',sep='\t')
d = defaultdict(list)
h = {}
fname_list = []
for _,row in data.iterrows():
	fname = row["path"][:-3]+"wav"
	d[row["client_id"]].append(fname)
	h[fname] = row["client_id"]
	fname_list.append(fname)
	

    

# get top 80 client_ids
client_ids = [item[0] for item in sorted(d.items(),key=lambda x: -len(x[1]))[:80]]


i = 1
for client_id in client_ids:
	dircounter = str(i).zfill(3)
	i+=1
	dirname = "p500"+dircounter
	#speaker_path = os.path.join(parent_dir, dirname)
	os.mkdir(dirname)
	j = 1
	print("proceeding with speaker ",dirname)
	for f in fname_list:#os.listdir("./"):
		if not os.path.isfile(f):
			continue
		if h[f] == client_id:
			filecounter = str(j).zfill(3)
			new_name = dirname+"_"+filecounter+".wav"
			os.system("mv {} {}".format(f,new_name))
			os.system("mv {} {}/.".format(new_name,dirname))
			j+=1