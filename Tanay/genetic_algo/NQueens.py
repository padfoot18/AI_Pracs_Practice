from genetic import Individual
import random


class NQueens(Individual):
    def set_n(n):
        Individual.set_variables(n, list(range(n)))

    def calc_fitness(self):
        fitness = 28
        for i in range(8):
            j = self.genes[i]
            for k in range(8):
                if k != i:
                    l = self.genes[k]
                    # column
                    if j == l:
                        fitness -= 1
                    elif i+j == k+l or i-j == k-l:
                        fitness -= 1
        self.fitness = fitness



NQueens.set_n(8)
SIZE = 50
population = []

# initialize random population
for _ in range(SIZE):
    population.append(NQueens())

max_itr = 10000
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
        new_population.append(NQueens(genes=gene1))
        new_population.append(NQueens(genes=gene2))

    # mutation
    for ind in new_population:
        if random.randint(0, 5) == 1:
            ind.mutate()
    population = new_population
    itr -= 1
