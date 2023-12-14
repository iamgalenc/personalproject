#Penduga bagi rata-rata n Lebih dari 30 (tabel z)
import numpy as np
import scipy.stats as st

sample_size = 36
avg = 560
sd = 80

random_grade = np.random.normal(avg, sd, sample_size)
sample_mean = np.mean(random_grade)
sample_std = np.std(random_grade, ddof=1)

confidence = 0.95
alpha = (1 + confidence) / 2
z_value = st.norm.ppf(alpha)

moe = z_value * (sample_std/np.sqrt(sample_size)) 

lower = sample_mean - moe
upper = sample_mean + moe

print(f"Diket\nRata-rata sampel = {sample_mean}\nUkuran sampel = {sample_size}\nStandar deviasi = {sample_std}\nKepercayaan = {confidence   }")

print(f"P({lower}< P <{upper})= 0.95")
