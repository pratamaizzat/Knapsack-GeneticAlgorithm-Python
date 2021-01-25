import matplotlib.pyplot as plt
from GA import GeneticAlgorithm
from stuff import gens

# input total dna satu populasi
spp = 100
popSize = (spp, len(gens))

thres = 3500 #10 Kg
mutRate = 0.4
crossRate = 0.8
numGen = 5000
choise = list()
weight = 0
worth = 0

geneticAlgo = GeneticAlgorithm(gens, thres, mutRate, crossRate, popSize, numGen)
parameter, history = geneticAlgo.optimize()

for i, v in enumerate(parameter[0]):
  if v == 1:
    choise.append(gens[i])  

for i in range(len(choise)):
  weight += choise[i].weight
  worth += choise[i].worth
  choise[i].print()

print('\nTotal berat = {0}; Total Value = {1}'.format(weight, worth))