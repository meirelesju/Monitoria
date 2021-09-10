import pandas as pd
from pandas.core.frame import DataFrame

def main():
    alunosTotal = pd.read_csv('alunos.csv', sep = ';')
    alunosGrupo = pd.read_csv('alunos_no_grupo.csv', sep = ';')

    namesTotal = alunosTotal['Nome'].tolist()
    namesGrupo = alunosGrupo['Nome'].tolist()

    part=[]
    for i in range(len(namesGrupo)):
        for j in range(len(namesTotal)):
            word = namesGrupo[i]
            word1 = namesTotal[j]

            sepName1=word.split()
            sepName2=word1.split()

            aux=0
            for a in range(len(sepName1)):
                for b in range(len(sepName2)):
                    if (sepName1[a]==sepName2[b]):
                        aux+=1
            
            if aux > 1:
                part.append(alunosTotal.iloc[j])
                #print("achou")
            
            if aux >= 1 and len(sepName1) == 1:
                part.append(alunosTotal.iloc[j])
                #print("achou")
            
            
    dfParticipantes = DataFrame(part, columns=['Matricula', 'Nome'])
    final =pd.concat([alunosTotal, dfParticipantes]).drop_duplicates(keep=False)

    print(final)

    final.to_csv (r'C:\Users\Julianny Meireles\Desktop\monitoria\alunos_faltando.csv', index = False, header=True,sep=';')
    print("done!")

main()