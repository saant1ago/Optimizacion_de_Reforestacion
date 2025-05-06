

from simpleai.search import SearchProblem, depth_first, breadth_first, uniform_cost, greedy, astar
from simpleai.search.viewers import BaseViewer, ConsoleViewer, WebViewer
import pandas as pd 
import numpy as np
import random



class Paquetes(SearchProblem):

    def __init__(self,demandas=((5.4,1),(8.0,2),(8.0,3),(7.56,4),(5.64,5),(6.11,6),(0,7),(4.92,8),(1.38,9),(5.53,10),(5.64,11),(5.05,12),(4.75,13)),capacidad=1,time=0.5,position=7,entregado=0,days = 0,regreso=False):


        costos= (
                (1, 1000, 0.005500, 0.015250, 0.025000, 0.122250, 0.108250, 0.097250, 0.137250, 0.058000, 0.074750, 0.086250, 0.151250, 0.165250),
                (2, 0.019250, 1000, 0.009750, 0.019500, 0.119000, 0.105000, 0.094000, 0.134000, 0.054750, 0.071500, 0.083000, 0.148000, 0.162000),
                (3, 0.019250, 0.001000, 1000, 0.009750, 0.128750, 0.114750, 0.103750, 0.143750, 0.064500, 0.081250, 0.092750, 0.157750, 0.171750),
                (4, 0.019250, 0.009750, 0.001000, 1000, 0.138500, 0.124500, 0.113500, 0.153500, 0.074250, 0.091000, 0.102500, 0.167500, 0.181500),
                (5, 0.122250, 0.119000, 0.128750, 0.138500, 1000, 0.001000, 0.025000, 0.015000, 0.065750, 0.036000, 0.026000, 0.029000, 0.043000),
                (6, 0.108250, 0.105000, 0.114750, 0.124500, 0.014000, 1000, 0.011000, 0.029000, 0.051750, 0.022000, 0.011000, 0.043000, 0.057000),
                (7, 0.097250, 0.094000, 0.103750, 0.113500, 0.025000, 0.011000, 1000, 0.040000, 0.040750, 0.011000, 0.001000, 0.054000, 0.068000),
                (8, 0.137250, 0.134000, 0.143750, 0.153500, 0.001000, 0.015000, 0.040000, 1000, 0.080750, 0.051000, 0.040000, 0.014000, 0.000280),
                (9, 0.058000, 0.054750, 0.064500, 0.074250, 0.065750, 0.051750, 0.040750, 0.080750, 1000, 0.018250, 0.029750, 0.094750, 0.108750),
                (10, 0.086500, 0.083000, 0.092750, 0.102500, 0.036000, 0.022000, 0.011000, 0.051000, 0.029750, 1000, 0.001000, 0.065000, 0.079000),
                (11, 0.097250, 0.094000, 0.103750, 0.113500, 0.025000, 0.011000, 0.001000, 0.040000, 0.040750, 0.011000, 1000, 0.054000, 0.068000),
                (12, 0.151250, 0.148000, 0.157750, 0.167500, 0.014000, 0.029000, 0.054000, 0.001000, 0.094750, 0.065000, 0.055500, 1000, 0.014000),
                (13, 0.165250, 0.162000, 0.171750, 0.181500, 0.028000, 0.043000, 0.068000, 0.014000, 0.108750, 0.079000, 0.069000, 0.001000, 1000)
            )


        
        
        initial_state=(capacidad,demandas,time,position,costos,entregado,days,regreso)

        SearchProblem.__init__(self, initial_state)


   

    def actions(self, state):

        capacidad,demanda,time,position,costos,entregado,days,regreso = state
        

        actions=[]
        

        for i in demanda:
            if i[0] != 0 and costos[position-1][i[1]] + time <= 8:
                actions.append(i)

        if actions == []:
            actions.append(('R'))


        
        actions=tuple(actions)
       
        return actions



    def result(self, state, action):

        
        #state(8,todas,time=0,position=(0,0))
        #action(4,1)
        capacity=state[0]
        demanda=state[1]
        time=state[2]
        position_old=state[3]
        costos=state[4]
        entregado=state[5]
        days=state[6]
        regreso=state[7]
        regreso = False

        demanda = [list(demandas) for demandas in demanda]




        

        #((4,1),(3,2),(3,3),(1,4),(3,5),(3,6),(3,7),(4,8),(1,9),(1,10))
        if action[0] == 'R':

            time = 0.5
            position = 7
            days+=1
            capacity = 1

        else:

            position = action[1]

            if capacity > demanda[position-1][0]:

                entregado=demanda[position-1][0]
                capacity -= demanda[position-1][0]
                capacity=round(capacity,2)
                demanda[position-1][0] = 0
                time += (costos[position_old-1][position] + 0.5)
                time = round(time,6)

            elif capacity <= demanda[position-1][0]:
                
                entregado = capacity
                demanda[position-1][0] -= capacity
                demanda[position-1][0]=round(demanda[position-1][0],4)
                capacity = 0
                time += (costos[position_old-1][position] + 0.5)
                time += (costos[position-1][7] + 0.5)
                position = 7
                capacity = 1
                regreso=True
    

        demanda = tuple(tuple(demandas) for demandas in demanda)
            

        return (capacity, demanda, time, position, costos, entregado,days,regreso)




    def is_goal(self, state):
    
        suma = 0
        for i in state[1]:
           suma += i[0]

        if suma == 0:
            return True
        else:
            return False
    

           


    def cost(self, state, action, state2):

        capacity=state[0]
        demanda=state[1]
        time=state[2]
        position_old=state[3]
        costos=state[4]
        time = 0

        if action[0] != 'R':

            position = action[1]

            if capacity > demanda[position-1][0]:

                time = time + costos[position_old-1][position] 
                time = round(time,6)
                

            elif capacity <= demanda[position-1][0]:
                time = time + costos[position_old-1][position] 
                time += costos[position-1][7] 


        return time
                   

    def heuristic(self, state):
 
        suma = 0
        for i in state[1]:
           suma += i[0]

        return suma



def display(result):
    if result is not None:
        for i, (action, state) in enumerate(result.path()):
            if action == None:
                print('Estado inicial')
            elif i == len(result.path()) - 1:
                print(i,'- Después de la accion', action)
                print('¡Meta lograda con costo =', result.cost,'!')
            else:
                if state[7]:
                    print(f'{i} - Después de entregar {state[5]} hectárea(s) al polígono {action[1]} y regresar al campamento')
                elif action[0] == 'R':
                    print(f'{i} - *************** Termino de la jornada laboral **************') 
                    print(f'!! Empieza el día {state[6] + 1} !!')
                else:
                    print(f'{i} - Después de entregar {state[5]} de volúmen paquetes al cliente {action[1]}')
                                  
            print(f' Posición : Polígono # {state[4][state[3]-1][0]} // Tiempo de jornada laboral : {state[2]} horas // Días totales {state[6]}')
    else:
        print('No se pudo resolver el problema')



my_viewer = None



#result = breadth_first(Paquetes(), graph_search=False)
#print()
#print('>> Búsqueda en anchura <<')
#display(result)

result = astar(Paquetes(), graph_search=False)
print()
print('>> Búsqueda A* <<')
display(result)

#result = greedy(Paquetes(), graph_search=False)
#print()
#print('>> Búsqueda Greedy <<')
#display(result)

#result = uniform_cost(Paquetes(), graph_search=False)
#print()
#print('>> Costo Uniforme <<')
#display(result)


