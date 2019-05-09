import random
from functools import total_ordering


@total_ordering
class Individual:
    all_chromosomes = []
    n = -1

    def __init__(self, genes=None):
        if not genes:
            genes = []
            for _ in range(Individual.n):
                genes.append(random.choice(Individual.all_chromosomes))
        self.genes = genes
        self.fitness = -1

    def set_variables(n, chromosomes):
        Individual.all_chromosomes = chromosomes
        Individual.n = n
        

    def crossover(self, other):
        n = len(self.genes)
        crossover_pt = random.randint(1, n-2)
        gene1 = self.genes[:crossover_pt] + other.genes[crossover_pt:]
        gene2 = other.genes[:crossover_pt] + self.genes[crossover_pt:]
        return gene1, gene2

    def mutate(self):
        n = Individual.n
        m = len(Individual.all_chromosomes)
        i = random.randint(0, n-1)
        j = random.randint(0, m-1)
        self.genes[i] = Individual.all_chromosomes[j]

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __repr__(self):
        return f'genes: {self.genes}, fitness: {self.fitness}\n'
