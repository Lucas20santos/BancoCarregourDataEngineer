import os
os.system("clear")

def criarAquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'w')
    arquivo.close()

def atualizarArquivos(nomeArquivo, texto):
    arquivo = open(nomeArquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    texto = arquivo.read()
    print(texto)

def mediaNotas(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    notasAluno = arquivo.read()
    alunos = notasAluno.split("\n")

    print(alunos)

def cadastroAlunos(cadastro):
    for c in cadastro:
        texto = ','.join(c)
        atualizarArquivos('notas.txt', texto + "\n")

def lerCadastroAlunosTirarMedia(nomeArquivo):
    arquivo = open(nomeArquivo, 'r')
    Alunos = arquivo.read().split("\n")
    
    for a in Alunos:
        aluno = a.split(",")
        notas = aluno[1:]
        
        media = lambda notas: sum([int(i) for i in notas]) / 4
        
        print(f"aluno: {aluno[0]:^10}  notas: {aluno[1:]} média: {media(notas):^3}")

if __name__ == "__main__":
    cadastro1 = [
            ['lucas','10', '10', '10', '10'],
            ['joao','10', '10', '10', '10'],
            ['luiz','10', '10', '10', '10'],
            ['fernanda','10', '10', '10', '10'],
            ['maria','10', '10', '10', '10'],
            ['joana','10', '10', '10', '10'],
            ['camila','10', '10', '10', '10'],
            ['mario','10', '10', '10', '10'],
            ['jeremias','10', '10', '10', '10'],
        ]
    cadastro2 = [
            ['gustava','10', '10', '10', '10'],
            ['pablo','10', '10', '10', '10'],
            ['felipe','10', '10', '10', '10'],
            ['pondé','10', '10', '10', '10'],
            ['renato','10', '10', '10', '10'],
            ['eliana','10', '10', '10', '10'],
            ['valentina','10', '10', '10', '10'],
            ['renata','10', '10', '10', '10'],
            ['ana','10', '10', '10', '10'],
        ]

    # cadastroAlunos(cadastro1)
    # cadastroAlunos(cadastro2)
    lerCadastroAlunosTirarMedia("notas.txt")