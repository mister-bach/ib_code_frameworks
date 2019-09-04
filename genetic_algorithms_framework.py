from random import randint, triangular, random


#FITNESS
#######################################
def get_weight(backpack, weights):
    weight = 0

    # Calculate the weight of the backpack

    return weight


def get_cost(backpack, costs):
    cost = 0
    
    # Calculate the cost of the backpack

    return cost


def sorted_by_fitness(backpacks, fitness_values):

    # Sort by fitness from least to greatest

    return backpacks


def selection(backpacks, weights, costs, max_weight):
    valid_backpacks = []
    fitness_values = []

    # Determine which backpacks are valid and then calculate
    # the fitness values. 

    return sorted_by_fitness(valid_backpacks, fitness_values)
    

#REPRODUCTION
#######################################

def reproduction(backpacks, population_size):
    new_backpacks = []
    
    # You can do 

    return new_backpacks[:population_size]


#MUTATION
#######################################

def mutation(backpacks, mutation_rate, population_size, strand_length):

    # Mutation based on the given rate

    return backpacks


def get_initial_population(strand_length, population_size):
    backpacks = [] 
    
    # Create the initial backpacks 

    return backpacks


def main():
    weights = [5, 6, 2, 3, 7, 9]
    costs   = [1, 2, 6, 7, 3, 2]
    strand_length = len(weights)
    population_size = 100
    max_weight = 15


if __name__ == '__main__':
    main()