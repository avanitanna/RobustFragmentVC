import os
from pathlib import Path
import sys
  
parent_dir = './names_loud_noisy/' #'./names_noisy/' # './names_low/' #./wavs_names/'    #'./cv-corpus/en/clips/'


# make output subdirs 

#original ckpt
# output_path = Path('./outputs-all/outputs-fragmentvc/noisy/')
# output_path.mkdir(exist_ok=True)

# cv-finetune
output_path = Path('./outputs-all/outputs-cv-finetune-denoise/steps1000000-loud-noisy/')
output_path.mkdir(exist_ok=True)

# cv-vctk
output_path = Path('./outputs-all/outputs-cv-vctk-denoise/steps1000000-loud-noisy/')
output_path.mkdir(exist_ok=True)


for f in os.listdir(parent_dir): #loop through subdirs
    
    d = str(f.split("_")[0])
    f_path = os.path.join(parent_dir,f)
    print("Starting with file,",f_path)
# for d in os.listdir(parent_dir): #loop through subdirs
#     print("Starting with speaker",d)
#     d_path = os.path.join(parent_dir,d)
#     f_path = os.path.join(d_path,"{}_001.wav".format(d))
#     print("Starting with file,",f_path)

    # original ckpt
    # os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c fragmentvc.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-all/outputs-fragmentvc/noisy/{}xp227.wav > output.log".format(f_path,d))
    # # target female speaker p228
    # os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c fragmentvc.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-all/outputs-fragmentvc/noisy/{}xp228.wav".format(f_path,d))


    # # cv-finetune
    # # target male speaker p227
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-all/ckpts-cv-finetune-denoise/retriever-step1000000-loss0dot7367.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-all/outputs-cv-finetune-denoise/steps1000000-loud-noisy/{}xp227.wav".format(f_path,d))
    # target female speaker p228
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-all/ckpts-cv-finetune-denoise/retriever-step1000000-loss0dot7367.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-all/outputs-cv-finetune-denoise/steps1000000-loud-noisy/{}xp228.wav".format(f_path,d))

    # cv-vctk
    # target male speaker p227
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-all/ckpts-cv-vctk-denoise/retriever-step1000000-loss0dot6561.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-all/outputs-cv-vctk-denoise/steps1000000-loud-noisy/{}xp227.wav".format(f_path,d))
    # target female speaker p228
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-all/ckpts-cv-vctk-denoise/retriever-step1000000-loss0dot6561.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-all/outputs-cv-vctk-denoise/steps1000000-loud-noisy/{}xp228.wav".format(f_path,d))




# for f in os.listdir(parent_dir): #loop through subdirs
    
#     d = str(f.split("_")[0])
#     f_path = os.path.join(parent_dir,f)
#     print("Starting with file,",f_path)

#     # original ckpt
#     os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c fragmentvc.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs/noisy/{}xp227.wav".format(f_path,d))
#     # target female speaker p228
#     os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c fragmentvc.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs/noisy/{}xp228.wav".format(f_path,d))


#     # # cv-finetune
#     # # target male speaker p227
#     os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-finetune-denoise/retriever-step200000-loss0dot8057.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-cv-finetune-denoise/steps200000-noisy/{}xp227.wav".format(f_path,d))
#     # target female speaker p228
#     os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-finetune-denoise/retriever-step200000-loss0dot8057.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-cv-finetune-denoise/steps200000-noisy/{}xp228.wav".format(f_path,d))

#     # cv-vctk
#     # target male speaker p227
#     os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-vctk-denoise/retriever-step200000-loss0dot7195.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-cv-vctk-denoise/steps200000-noisy/{}xp227.wav".format(f_path,d))
#     # target female speaker p228
#     os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-vctk-denoise/retriever-step200000-loss0dot7195.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-cv-vctk-denoise/steps200000-noisy/{}xp228.wav".format(f_path,d))






"""
# make output subdirs 
# cv-finetune
output_path = Path('./outputs-cv-finetune/steps200000/')
output_path.mkdir(exist_ok=True)
# cv-scratch
output_path = Path('./outputs-cv-scratch/steps200000/')
output_path.mkdir(exist_ok=True)
# cv-vctk
output_path = Path('./outputs-cv-vctk/steps200000/')
output_path.mkdir(exist_ok=True)

for d in os.listdir(parent_dir): #loop through subdirs
    print("Starting with speaker",d)
    d_path = os.path.join(parent_dir,d)
    f_path = os.path.join(d_path,"{}_001.wav".format(d))
    print("Starting with file,",f_path)
    # cv-finetune
    # target male speaker p227
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-finetune/retriever-step200000-loss0dot6726.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-cv-finetune/steps200000/{}xp227.wav > out.log".format(f_path,d))
    # target female speaker p228
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-finetune/retriever-step200000-loss0dot6726.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-cv-finetune/steps200000/{}xp228.wav".format(f_path,d))
    
    # # cv-scratch
    # # target male speaker p227
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-scratch/retriever-step200000-loss0dot6879.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-cv-scratch/steps200000/{}xp227.wav".format(f_path,d))
    # # target female speaker p228
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-scratch/retriever-step200000-loss0dot6879.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-cv-scratch/steps200000/{}xp228.wav".format(f_path,d))

    # # cv-vctk
    # # target male speaker p227
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-vctk/retriever-step200000-loss0dot6090.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-cv-vctk/steps200000/{}xp227.wav".format(f_path,d))
    # # target female speaker p228
    os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-vctk/retriever-step200000-loss0dot6090.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-cv-vctk/steps200000/{}xp228.wav".format(f_path,d))

"""









# for d in os.listdir(parent_dir): #loop through subdirs
#     print("Starting with speaker",d)
#     d_path = os.path.join(parent_dir,d)

#     # cv-finetune
#     output_path = Path('./outputs-cv-finetune/steps50000/{}'.format(d))
#     output_path.mkdir(parents=True,exist_ok=True)
#     # cv-scratch
#     output_path = Path('./outputs-cv-scratch/steps50000/{}'.format(d))
#     output_path.mkdir(parents=True,exist_ok=True)
#     # cv-vctk
#     output_path = Path('./outputs-cv-vctk/steps50000/{}'.format(d))
#     output_path.mkdir(parents=True,exist_ok=True)

#     for f in os.listdir(d_path): #loop through files in the subdir
#         f_path = os.path.join(d_path,f)

#         # cv-finetune
#         # target male speaker p227
#         os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-finetune/retriever-step50000-loss1dot0852.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-cv-finetune/steps50000/{}/p227x{}.wav".format(f_path,d,d))
#         #os.system("mv ./outputs-cv-finetune/steps50000/{}/output.wav" "./outputs-cv-finetune/steps50000/{}/p227x{}".format(d,d,f))
#         # target female speaker p228
#         os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-finetune/retriever-step50000-loss1dot0852.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-cv-finetune/steps50000/{}/p228x{}.wav".format(f_path,d,d))
#         #os.system("mv ./outputs-cv-finetune/steps50000/{}/output.wav" "./outputs-cv-finetune/steps50000/{}/p228x{}".format(d,d,f))

#         # cv-scratch
#         # target male speaker p227
#         os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-scratch/retriever-step50000-loss0dot8961.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-cv-scratch/steps50000/{}/p227x{}.wav".format(f_path,d,d))
#         # target female speaker p228
#         os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-scratch/retriever-step50000-loss0dot8961.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-cv-scratch/steps50000/{}/p228x{}.wav".format(f_path,d,d))

#         # cv-vctk
#         # target male speaker p227
#         os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-vctk/retriever-step50000-loss0dot8177.pt {} ./wavs_names/p227/p227_002.wav ./wavs_names/p227/p227_003.wav ./wavs_names/p227/p227_004.wav --output_path ./outputs-cv-vctk/steps50000/{}/p227x{}.wav".format(f_path,d,d))
#         # target female speaker p228
#         os.system("python3 convert.py -w wav2vec_small.pt -v vocoder.pt -c ./ckpts-cv-vctk/retriever-step50000-loss0dot8177.pt {} ./wavs_names/p228/p228_002.wav ./wavs_names/p228/p228_003.wav ./wavs_names/p228/p228_004.wav --output_path ./outputs-cv-vctk/steps50000/{}/p228x{}.wav".format(f_path,d,d))