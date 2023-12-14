import numpy as np
import scipy.stats as stats

sample_size = 36
avg = 560
sd = 80

random_grade = np.random.normal(avg, sd, sample_size)
sample_mean = np.mean(random_grade)
sample_std = np.std(random_grade, ddof=1)
# print(random_grade)

confidence = 0.95
alpha = 1 - confidence
z_value = stats.norm.ppf(alpha/2)
print(z_value)
