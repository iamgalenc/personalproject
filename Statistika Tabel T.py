#Penduga bagi rata-rata n kurang dari 30 (tabel t)
import numpy as np
import scipy.stats as st

sample_size = 20
avg = 560
sd = 80

random_grade = np.random.normal(avg, sd, sample_size)
sample_mean = np.mean(random_grade)
sample_std = np.std(random_grade, ddof=1)

confidence = 0.95
alpha = (1 + confidence) 
t_value = st.t.ppf(alpha/2, sample_size-1)

moe = t_value * (sample_std/np.sqrt(sample_size)) 

lower = sample_mean - moe
upper = sample_mean + moe

print(f"Diket\nRata-rata sampel = {sample_mean}\nUkuran sampel = {sample_size}\nStandar deviasi = {sample_std}\nKepercayaan = {confidence}")

print(f"P({lower}< P <{upper})= 0.95")