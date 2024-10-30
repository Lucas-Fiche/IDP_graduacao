while True:
 D = int(input())

 if D == -1:
  break
 
 N = input().strip()

 resultados_pares = 0
 resultados_impares = 0

 for i in range(len(N)):
  if i % 2 == 0:
    resultados_pares += int(N[i])
  else:  
    resultados_impares += int(N[i])

 soma_pares = resultados_pares
 soma_impares = resultados_impares

 resultado_subtracao = soma_pares - soma_impares

 if resultado_subtracao % 11 == 0:
    resultado_final = "sim"
 else:
   resultado_final = "nao"
 print("{}: {} - {} = {} - {}".format(N, soma_pares, soma_impares, resultado_subtracao, resultado_final))

 # 285098729
