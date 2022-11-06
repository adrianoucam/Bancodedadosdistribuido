
# Adriano Lima e Souza - adrianoucam@gmail.com
# 05 de novembro de 2022
# algoritmo para calcular fragmentacao vertical de banco de dados distribuido
# Professor Daniel Cardoso Moraes de Oliveira - UFF Niteroi 


numero_de_sites=1 # valor inicial - sera ajustado em main ()
numero_de_queries=3
numero_de_atributos=4

atributos_vet1=[[1,'matricula'],
               [2,'nomecliente'],
               [3,'filiacao'],
               [4,'anosocio'],
               [5,'idade']]

atributos_vet=[[1,'pno'],
               [2,'pname'],
               [3,'budget'],
               [4,'loc']]
#           S1,S2,S3
#         Q1  
#         Q2
#         Q3 

vetor_qry2=[[70,50,3],
           [20,30,5],
           [10,20,10]]

vetor_qry1=[[15,20,10],
           [5,0,0],
           [25,25,25],
           [3,0,0]]

# simplificando 15+20+10 = 45
# simplificando 5 = 5
# simplificando 25+25+25 = 75
# simplificando 3 = 3

vetor_qry2=[[45],
           [5],
           [75],
           [3],]

vetor_qry3=[[70],
           [50],
           [10]]


vetor_qry=[[10],
           [20],
           [15]]

vetor_qry=[[35],
           [20],
           [10]]
# matriz_uso    A1,A2,A3,A4
#            Q1
#            Q2
#            Q3

matriz_uso1=[[1,0,1,0],
            [0,1,1,0],
            [0,1,0,1],
            [0,0,1,1]]

matriz_uso2=[[1,1,1,0,1],
            [1,0,0,1,1],
            [1,1,1,1,1] ]

matriz_uso3=[[1,0,0,1],
            [0,1,0,0],
            [1,1,1,0] ]

matriz_uso=[[1,0,1,1],
            [0,1,1,0],
            [1,0,0,1] ]

vetor_aff2=[[0 for j in range(5)] for i in range(5)]

def matmult(a,b):
    zip_b = zip(*b)    
    return [[sum(ele_a*ele_b for ele_a, ele_b in zip(row_a, col_b)) 
             for col_b in zip_b] for row_a in a]
    
    
    
def calcula_qryx(qryvet,l,c): # não usada
    sum=0
    for x in range(len(qryvet)):                
        for y in range(len(qryvet[0])):                
            print(qryvet[x][y])  
            if (x==l)  and  (y==c):
                sum=qryvet[x][y]
    return sum



def preenche_vet_aff(vet_att,qryvet,usovet): 
    # CRIAR MATRIZ QUADRADA PARA CALCULAR  A AFINIDADE
    vet= [[0 for col in range(len(vet_att))] for row in range(len(vet_att))]

    # lista as linhas e colunas que contem 1 na matriz de uso
    for linha in range(len(vet_att)):
        #print('----------------------------------')                                                    
        for coluna in range(len(vet_att)):                          
            #sum=0     
            for q in range(len(qryvet)):
                # sites
                for s in range(len(qryvet[0])):                
                    if usovet[q][linha]==1 and usovet[q][coluna]==1:
                        # print (linha,coluna,q,qryvet[q][0])
                        # adiciona o valor do peso da consulta
                        vet[linha][coluna] = vet[linha][coluna]+qryvet[q][s]
             
    
    return vet

        
def calculateBond(_ptr, left,  right) :
        sum = 0;        
        left=left-1
        right=right-1
        # print ('left  ',left)
        #print ('right ',right)
        print ('Calculando Bond ',left+1,right+1)
        if (left<=0) or (left>=len(_ptr) or right>=len(_ptr)):
            print ('zerando porque os valores para left e right foram ',left+1,' ',right+1)
            sum=0
        else:
            for i in range(len(_ptr)):                
                if (i>0) :
                    # print (i,left,_ptr[i][left],' ',_ptr[i][right],' ',_ptr[i][left] * _ptr[i][right])
                    sum = sum + (_ptr[i][left] * _ptr[i][right]);
        
            
        # print('soma dos valores ',left+1 ,' e ',right+1,' = ',sum)
        return sum;
def CalculaCont(vetor,esquerda,meio,direita):
    retorno=0
    print ('tamanho do vetor ',len(vetor),' valores para ',esquerda,meio,direita)
    if esquerda==0:
        esquerda=-1
    if direita>len(vetor):        
        direita=999
    
        
    retorno =(2*calculateBond(vetor,esquerda,direita))+(2*calculateBond(vetor,direita,meio))-(2*calculateBond(vetor,esquerda,meio))
    print('resultado do calculcaCont ',retorno)
    return retorno
    
def melhor_arranjo(vetorafinidade,matrizuso,atributos):    
    vetcont=[]
    if len(matrizuso[0])!=len(atributos):
        print ('numero de atributos diferentes (matriz de uso x atributos_vet')
        return vetcont
    for j in atributos:
            print(j[1])                
    print ('armazenando vetores para ',len(atributos),' atributos ')
    for i in range(2,len(matrizuso[0])):        
            n=i-1
            if i==1:
                n=0        
            vetcont.append(CalculaCont(vetor_aff2,n,i,i+1))    
    for j in vetcont:
        print(j)
        

    
# print (vetor_aff2)    
# exemplo de como o vetor vai ficar preenchido depois de calcular afinidade de atributos com queries
vetor_aff2=[[130,80,80,60,60],
           [80,80,80,10,10],
           [80,80,80,10,10],
           [60,10,10,60,60],
           [60,10,10,60,60]]
# FIM do exemplo de como o vetor vai ficar preenchido depois de calcular afinidade de atributos com queries
def main():
    numero_de_sites=len(vetor_qry[1])
    numero_de_queries=len(vetor_qry[0])
    numero_de_atributos=len(atributos_vet[0])
    
    print('------------- Lista de atributos')
    for i in atributos_vet:
        print(i)
    vetor_aff2=preenche_vet_aff(atributos_vet,vetor_qry,matriz_uso)
    print('------------- Matriz de afinidade')
    for i in vetor_aff2:
        print(i)
    print('------------- Outros dados ')
        
    print('Numero de atributos :',numero_de_atributos)
    print('Numero de sites :',numero_de_sites)
    print('Numero de qyeries :',numero_de_queries)
    #print (vetor_aff2)
    '''
    print (calculateBond(vetor_aff2,0,2))
    print (calculateBond(vetor_aff2,3,2))
    print (calculateBond(vetor_aff2,3,6))

    print (calculateBond(vetor_aff2,2,3))
    print (calculateBond(vetor_aff2,2,4))
    print (calculateBond(vetor_aff2,2,5))
    print (calculateBond(vetor_aff2,3,3))
    print (calculateBond(vetor_aff2,3,4))
    print (calculateBond(vetor_aff2,4,5))
    print (calculateBond(vetor_aff2,4,5))
    print ('------------------------------------------')
    print (CalculaCont(vetor_aff2,0,3,2))
    print ('------------------------------------------')
    print (CalculaCont(vetor_aff2,2,3,99))
    print ('------------------------------------------')
    print (CalculaCont(vetor_aff2,2,5,3))
    print ('------------------------------------------') 
    '''
    melhor_arranjo(vetor_aff2,matriz_uso,atributos_vet) 

#print(np.dot(vetor_qry,matriz_uso))



if __name__ == '__main__':
    main()

