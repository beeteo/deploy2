import random
import os

class randomize:
    def __init__(self):
        self.img = []

    def get_kiss_gif(self):
        DIR = 'Core/Data/Gifs/Kiss'
        data = [name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]
        random_data = random.choice(data)
        split_kiss = random_data.split('kiss_')[1]
        get_number = split_kiss.split('.gif')[0]
        gif_url = 'https://beete.xyz/gifs/kiss/kiss_{}.gif'.format(get_number)
        return gif_url