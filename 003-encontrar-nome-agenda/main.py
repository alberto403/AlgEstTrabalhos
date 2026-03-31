from find import find
from quick_sort import quick_sort


def main():
    agenda = [
        "Luiz",
        "Maria",
        "Joao",
        "Ana",
        "Carlos",
        "Diana",
        "Eduardo",
        "Ze",
        "Strauss",
        "Nicholas",
        "Alberto",
        "Lanza",
        "Jose Arthur",
        "Brafman",
        "Jose Baptista",
        "Teodosio",
        "Diogo"
    ]

    quick_sort(array=agenda, low=0, high=len(agenda)-1)

    print('-' * 20)
    print("Sua Agenda:")
    for i in range(len(agenda)):
        print(f"{i} - {agenda[i]}")

    search_name = input("Digite o nome a ser encontrado: ")

    if search_name is None or search_name.strip() == "":
        print("Nome invalido")
        return
    
    agenda = [name.lower() for name in agenda]
    
    index = find(array=agenda, low=0, high=len(agenda)-1, value=search_name.lower())

    if index is not None:
        print(f"{search_name} encontrado no indice {index}")
        return
    
    print(f"{search_name} nao encontrado")


if __name__ == "__main__":
    main()

    