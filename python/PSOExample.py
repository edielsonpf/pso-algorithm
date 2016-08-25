# Simulador de colonia de passaros na solucao de problemas.
# Baseado no artigo Partical Swarm Optimization de James Kennedy.
#
# Por Edielson Prevato Frigieri

import numpy as np
from ParticleSwarmOptimization.pso import pso
import matplotlib.pyplot as plt

if __name__ == '__main__': 
 
    #define as constantes da colonia
    NUM_BIRDS = 200
    NUM_INTERACTIONS = 200
    MAX_SIZE = 10
    MAX_ERRO = 0.1
    NUM_VARS = 3
    
    #Define a posicao da comida.
    roostPoint = np.random.randn(NUM_VARS)*5
    
     
    swarm = pso(NUM_BIRDS,NUM_VARS,NUM_INTERACTIONS)
    gbest = swarm.search(roostPoint,MAX_ERRO)
    plt.plot(gbest)
    plt.show()  
    
