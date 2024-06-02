def verificar_idades(n, albuns):
    anos_possiveis_nascimento = set()
    
    for album in albuns:
        ano = album[0]
        idade = album[1]
        ano_nascimento = ano - idade
        anos_possiveis_nascimento.add(ano_nascimento)
    
    if len(anos_possiveis_nascimento) == 1:
        return "idades corretas"
    else:
        return "mentiu a idade"

def main():
    n = int(input())
    albuns = []
    
    for _ in range(n):
        ano, titulo = map(int, input().split())
        albuns.append((ano, titulo))
    
    resultado = verificar_idades(n, albuns)
    print(resultado)

if __name__ == "__main__":
    main()
