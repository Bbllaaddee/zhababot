import os
import random

def random_zhaba():
    files = os.listdir('./zhaba_pics/')
    choice = random.choice(files)
    return open(f'./zhaba_pics/{choice}')
