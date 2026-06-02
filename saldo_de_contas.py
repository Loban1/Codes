receita=[]
despesa=[]
stop=-1
total_receita=0
total_despesa=0
print("Lista de receitas e despesas")
while stop!=0:
    v=int(input("Insira um valor inteiro positivo para adicionar uma receita ou um valor inteiro negativo para adicionar despesa:"))
    if(v>=0): 
        receita.append(v) 
        stop=int(input("Voce cadastrou uma receita\nDigite 0 para terminar ou 1 para continuar."))
        if(stop==0):
            total_despesa=sum(despesa)
            total_receita=sum(receita)
            break
    else: 
        despesa.append(v) 
        stop=int(input("Voce cadastrou uma receita\nDigite 0 para terminar ou 1 para continuar."))
        if(stop==0):
            total_despesa=sum(despesa)
            total_receita=sum(receita)
            break
saldo_final= total_receita + total_despesa
print("\n\n############### LISTA FINAL ###############")
print(f"\nTotal da receita: {total_receita}\tTotal da despesa: {total_despesa}")
print(f"\nSaldo final: {saldo_final}")
if(saldo_final>0):
    print("\nLucro!")
else:
    print("\nPrejuizo!")