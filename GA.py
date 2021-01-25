import numpy as np
import random as rd
from random import randint
from Population import Population


class GeneticAlgorithm:
  def __init__(self, gens, thres, mutRate, crossRate, popSize, numGen):
    self.gens = gens
    self.thres = thres
    self.mutRate = mutRate
    self.crossRate = crossRate
    self.popSize = popSize
    self.numGen = numGen
    self.history = []
    self.parameter = []

    self.numParents = int(popSize[0] / 2)
    self.numOffspring = popSize[0] - self.numParents
    
    self.populations = np.random.randint(2, size = self.popSize)
    self.populations = self.populations.astype(int)
    self.fitness = np.empty(self.populations.shape[0])
    self.parents = np.empty((self.numParents, self.populations.shape[1]))
    self.offspring = np.empty((self.numOffspring, self.populations.shape[1]))
    self.mutants = np.empty((self.offspring.shape))
    self.population = Population(self.gens, self.thres, self.mutRate, self.crossRate)
    
  def optimize(self):
    for i in range(self.numGen):
      self.fitness = self.population.calcFitness(self.populations)
      self.history.append(self.fitness)
      self.parents = self.population.selection(self.fitness, self.numParents, self.populations)
      self.offspring = self.population.crossover(self.parents, self.numOffspring)
      self.mutants = self.population.mutation(self.offspring)

      self.populations[0:self.parents.shape[0], :] = self.parents
      self.populations[self.parents.shape[0]:, :] = self.mutants
    
    print('Last generation: \n{}\n'.format(self.populations))
    fitnessLast = self.population.calcFitness(self.populations)
    print('Fitness of the last generation: \n{}\n'.format(fitnessLast))
    maxFitness = np.where(fitnessLast == np.max(fitnessLast))
    self.parameter.append(self.populations[maxFitness[0][0],:])

    return self.parameter, self.history

