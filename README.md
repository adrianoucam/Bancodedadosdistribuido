# Bancodedadosdistribuido

# Adriano Lima e Souza - adrianoucam@gmail.com
# 05 de novembro de 2022
# algoritmo para calcular fragmentacao vertical de banco de dados distribuido
# Professor Daniel Cardoso Moraes de Oliveira - UFF Niteroi 

Dentro do arquivo fonte existem 3 matrizes que devem ser preenchidos

atributos_vet=[[1,'pno'],
               [2,'pname'],
               [3,'budget'],
               [4,'loc']]
               
Matriz de uso
Onde deve ser preenchido com 0 ou 1 para cada consulta(query)
matriz_uso=[[1,0,1,1],
            [0,1,1,0],
            [1,0,0,1] ]

A matriz vetor_qry deve ser preenchida com os dados das frequencias/Sites(servidores) que cada consulta é utilizada 
vetor_qry=[[15,20,10],
           [5,0,0],
           [25,25,25],
           [3,0,0]]
