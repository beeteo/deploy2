import os
import random

DIR = 'Core/Data/Gifs/Kiss'
data = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]
random_data = random.choice(data)
split_kiss = random_data.split('kiss_')[1]
get_number = split_kiss.split('.gif')[0]
print(get_number)