import numpy as np
import random as rd
from random import randint

class Population:
  def __init__ (self, genes, thresh, mutRate, crossRate):
    self.genes = genes
    self.thresh = thresh
    self.mutRate = mutRate
    self.crossRate = crossRate
  
  def calcFitness(self, population):
    fitness = np.empty(population.shape[0])
    worth = list(self.genes)
    weight = list(self.genes)
    quantity = list(self.genes)

    for i, v in enumerate(self.genes):
      worth[i] = self.genes[i].getWorth()
      quantity[i] = self.genes[i].getQuantity()
      weight[i] = self.genes[i].getWeight() * quantity[i]

    for i in range(population.shape[0]):
      sumWorth = np.sum(population[i] * worth)
      sumWeight = np.sum(population[i] * weight)
      if sumWeight <= self.thresh:
        fitness[i] = sumWorth
      else:
        fitness[i] = 0    

    return fitness

  def selection(self, fitness, numParents, population):
    fitness = list(fitness)
    parents = np.empty((numParents, population.shape[1]))
    for i in range(numParents):
      maxID = np.where(fitness == np.max(fitness))
      parents[i,:] = population[maxID[0][0],:]
      fitness[maxID[0][0]] = -9999999
    
    return parents

  def crossover(self, parents, numOffspring):
    offsprings = np.empty((numOffspring, parents.shape[1]))
    crossover_point = int(parents.shape[1]/2)
    i=0
    while (parents.shape[0] < numOffspring):
      parent1_index = i%parents.shape[0]
      parent2_index = (i+1)%parents.shape[0]
      x = rd.random()
      if x > self.crossRate:
        continue
      parent1_index = i%parents.shape[0]
      parent2_index = (i+1)%parents.shape[0]
      offsprings[i,0:crossover_point] = parents[parent1_index,0:crossover_point]
      offsprings[i,crossover_point:] = parents[parent2_index,crossover_point:]
      i=+1
    return offsprings

  def mutation(self, offsprings):
    mutants = np.empty((offsprings.shape))
    for i in range (mutants.shape[0]):
      randVal = rd.random()
      mutants[i,:] = offsprings[i,:]
      if randVal > self.mutRate:
        continue
      intRandVal = randint(0, offsprings.shape[1] - 1)
      if mutants[i, intRandVal] == 0:
        mutants[i, intRandVal] = 1
      else:
        mutants[i, intRandVal] = 0

    return mutants
