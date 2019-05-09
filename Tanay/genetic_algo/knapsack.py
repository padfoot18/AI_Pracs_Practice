from genetic import Individual
import random


class Knapsack(Individual):
    weights = []
    values = []
    max_capacity = -1

    def set_n(n):
        Individual.set_variables(n, [0,1])

    def calc_fitness(self):
        weight = 0
        value = 0
        for i in range(len(self.genes)):
            if self.genes[i] == 1:
                weight += Knapsack.weights[i]
                value += Knapsack.values[i]
        if weight <= Knapsack.max_capacity:
            self.fitness = value
        else:
            self.fitness = 0

    def __repr__(self):
        return f'genes: {self.genes}, fitness: {self.fitness}\n'

Knapsack.set_n(4)
Knapsack.weights = [24, 10, 10, 7]
Knapsack.values = [24, 18 ,18, 10]
Knapsack.max_capacity = 25
SIZE = 20
population = []

# initialize random population
for _ in range(SIZE):
    population.append(Knapsack())

max_itr = 50    
for itr in range(max_itr):
    print(f'Iteration {itr}')
    # calculate fitness of all
    for ind in population:
        ind.calc_fitness()

    population.sort(reverse=True)
    print(population[0])
    if population[0].fitness == 28:
        print(f'Solution found in iteration {itr}')
        break

    new_population = []
    # crossover
    for i in range(int(SIZE/2)):
        parent1 = random.choice(population[:int(SIZE/2)])
        parent2 = random.choice(population[:int(SIZE/2)])
        while parent2.genes != parent1.genes:
            parent2 = random.choice(population[:int(SIZE/2)])

        gene1, gene2 = parent1.crossover(parent2)
        new_population.append(Knapsack(genes=gene1))
        new_population.append(Knapsack(genes=gene2))

    # mutation
    for ind in new_population:
        if random.randint(0, 5) == 1:
            ind.mutate()
    population = new_population
    itr -= 1
