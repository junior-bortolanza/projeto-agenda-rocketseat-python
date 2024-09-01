print('''\nMɪɴʜᴀ Aɢᴇɴᴅᴀ Cᴏɴᴛᴀᴛᴏs 📒''')


def adicionar_contato(contatos, nome_pessoa, cpf, telefone, email):
    contato = { 'nome': nome_pessoa, 'cpf': cpf, 'telefone': telefone, "email": email , "favorito": False}
    contatos.append(contato)
    print(f"Contato {nome_pessoa},{cpf}, {telefone}, {email} adicionado com sucesso!")
    return


def listar_contatos(contatos):
    print("\n Lista e contatos: ")
    print(contatos)
    for i, contato in enumerate (contatos, start=1):
        informacao_contato = " ️✅ " if contato['favorito'] else " "
        nome_contato = contato['nome']
        cpf_contato = contato['cpf']
        telefone_contato = contato['telefone']
        email_contato = contato['email']
        print(f"\n{i}. [{informacao_contato}] {nome_contato} {cpf_contato}, {telefone_contato} {email_contato}")
    return
    

def editar_contato(contatos, indice_contato, novo_nome_atualizado, novo_cpf_atualizado, novo_telefone_atualizado, novo_email_atualizado):
    indice_contato_atualizado = int(indice_contato) - 1
    if indice_contato_atualizado >=0 and indice_contato_atualizado < len(contatos):
        contatos[indice_contato_atualizado]['nome'] = novo_nome_atualizado
        contatos[indice_contato_atualizado]['cpf'] = novo_cpf_atualizado
        contatos[indice_contato_atualizado]['telefone'] = novo_telefone_atualizado
        contatos[indice_contato_atualizado]['email'] = novo_email_atualizado
        print(f"Contato{indice_contato} atualizada para {novo_nome_atualizado}, {novo_cpf_atualizado}, {novo_telefone_atualizado}, {novo_email_atualizado}")
    else:
        print('Íncide do contato inválido')
    return

def desmarcar_favorito(contatos, indice_contato):
    indice_desmarcar_favorito = int(indice_contato) - 1
    contatos[indice_desmarcar_favorito]['favorito'] = False
    print(f"Contado {indice_contato} removido dos favoritos!😭")
    return


        
def adicionar_favorito(contatos, indice_contato_favorito):
    contato_favorito = int(indice_contato_favorito) - 1
    contatos[contato_favorito]['favorito'] = True
    print(f"Contato {contato_favorito} adicionado aos favoritos ")
    return


    
def apagar_contato(contatos, indice_contato):
    indice_contato_apagar = int(indice_contato) - 1
    if 0<= indice_contato_apagar < len(contatos):
        contatos.pop(indice_contato_apagar)
        print()
        print(f"Contato [{indice_contato_apagar}] deletado com sucesso! 🥺")
    else:
        print("Número errado!")

contatos = []
while True:
    print()
    print("1. Adicionar Contato")
    print("2. Editar Contato")
    print("3. Adicionar Contato aos favoritos")
    print("4. Desmarcar Contato dos favoritos")
    print("5  Lista de Contatos")
    print("6. Apagar um contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_contato = str(input("Digite o nome: "))
        cpf_contato = int(input("Digite o CPF: "))
        telefone_contato = int(input("Digite o telefone do contato: "))
        email_contato = input("Digite o E-mail: ")
        adicionar_contato(contatos, nome_contato,cpf_contato, telefone_contato, email_contato)
    
    elif escolha == "2":
        listar_contatos(contatos)
        id_contato = input("Digite o id do contato para editar:")
        novo_nome_contato = input("Digite o nome do contato: ")
        novo_cpf_contato = input("Digite o CPF do contato: ")
        novo_telefone_contato = input("Digite o Telofone do contato: ")
        novo_email_contato = input("Digite o E-mail: ")

        editar_contato(contatos,id_contato, novo_nome_contato, novo_cpf_contato, novo_telefone_contato, novo_email_contato )
    
    elif escolha == "3":
        listar_contatos(contatos)
        indice_contato_favorito = input("Digite o numero do contato que deseja favoritar: ")
        adicionar_favorito(contatos, indice_contato_favorito)
    
    elif escolha == "4":
        listar_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja apagar: ")
        desmarcar_favorito(contatos, indice_contato)

    elif escolha == "5":
        listar_contatos(contatos)


    elif escolha == "6":
        listar_contatos(contatos)
        indice_contato = input("Digite o numero do contato que deseja apagar: ")
        apagar_contato(contatos, indice_contato)


    elif escolha == "7":
        break

    print("\n Programa Finalizado!")   

    
    

