import neat
import pygame
import sys
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# ticker: str = "AMD"
# data = pd.read_csv("../Data/{}_test_train_data.csv".format(ticker))

# X = data.iloc[:,:-3]
# y = data["Profit-Bool"] #.iloc[:,-3:]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1800
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Investor:
    pass

def eval_genomes(genomes, config):
    global ge, nets, points
    clock = pygame.time.Clock()
    points = 0

    investors = []
    ge = []
    nets = []
    
    for genome_id, genome in genomes:
        investors.append(Investor())
        ge.append(genome)
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        genome.fitness = 100
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                

# Setup the NEAT Neural Network
def run(config_path):
    global pop
    config = neat.config.Config(
        neat.DefaultGenome,
        neat.DefaultReproduction,
        neat.DefaultSpeciesSet,
        neat.DefaultStagnation,
        config_path                                                                                                                                                                                     
    )

    pop = neat.Population(config)
    pop.run(eval_genomes, 50)


if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')
    run(config_path)