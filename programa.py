import os
import sqlite3

#funcção que "apaga" telas
def apagarTela():
    os.system('cls' if os.name == 'nt' else 'clear')

#criando banco de dados
#conexão
conn = sqlite3.connect('produtos.db')

#cursor, responsável pela execução dos comandos
c = conn.cursor()

#criando a tabela do bd
def criandoTB():
    c.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        qnt TEXT NOT NULL,
        vlr_compra TEXT NOT NULL,
        vlr_venda TEXT NOT NULL,
        grupo TEXT NOT NULL
    )
    ''')

#função responsável por inserir os produtos na tabela
def inserirProd():
    print('''
 ----------------------------------------------------
         ADEGA GOMES DISTRIBUIDORA DE BEBIDAS
 ----------------------------------------------------
                  + CADASTRO +
    ''')
    p_nome = input('NOME DO PRODUTO: ')
    p_qnt = input('QUANTIDADE DO PRODUTO: ')
    p_vlrCompra = input('VALOR DE COMPRA: R$ ')
    p_vlrVenda = input('VALOR DE VENDA: R$ ')
    p_grupo = input('GRUPO: ')

    inserir = input('''
               CONFIRA OS DADOS
    PRESSIONE 1 PARA ENVIAR OU 2 PARA CANCELAR!
    ''')
    if inserir == '1':
        criandoTB() #chamando a abertura da tabela, para reconhecimento

        #inserindo as respostas do usuario nas colunas do bd
        c.execute('''
        INSERT INTO produtos (nome, qnt, vlr_compra, vlr_venda, grupo)
        VALUES(?,?,?,?,?)
        ''',(p_nome, p_qnt, p_vlrCompra, p_vlrVenda, p_grupo))

        #enviando respostas
        conn.commit()
        print('''
        * Dados inseridos com sucesso! *
        ''')

        opc_cad = input('Deseja continuar cadastrando (S/N)?')
        if opc_cad == 'S' or opc_cad == 's':
            apagarTela()
            inserirProd()
        else:
            apagarTela()
            subMenuEstoque()
    else:
        input('Cadastro cancelado, pressione ENTER para voltar ao menu anterior.')
        apagarTela()
        subMenuEstoque()

#função responsável por consultar produtos no estoque
def consultProd():
    print('''
  ----------------------------------------------------
          ADEGA GOMES DISTRIBUIDORA DE BEBIDAS
  ----------------------------------------------------
                   + CONSULTA +

    ''')
    criandoTB()
    c.execute('''
    SELECT * FROM produtos;
    ''')

    for linha in c.fetchall():
        print(' ',linha)

    input('''
  Pressione qualquer tecla para voltar...''')
    apagarTela()
    subMenuEstoque()

#função responsável por editar cadastros do bd
def editProd():
    print('''
  ----------------------------------------------------
          ADEGA GOMES DISTRIBUIDORA DE BEBIDAS
  ----------------------------------------------------
                  + ALTERAÇÕES +
    ''')

    criandoTB() #chamando a tb para reconhecimento

    #mesmo comando da função consultProd() a fim de mostrar os produtos para o usuario
    c.execute('''
    SELECT * FROM produtos;
    ''')
    print("""
  Utilize as tags abaixo para modificar os produtos em estoque.

  (ID, 'Nome','Quantidade', 'Valor compra', 'Valor venda', 'Grupo')
    """)
    for linha in c.fetchall():
        print(' ',linha)

    #pedindo os paramentros de mudança para o usuario
    print('')
    id_produto = input('  Digite o ID do produto: ')
    opc_edit = input('  Digite o nome da coluna que deseja alterar: ')

    if opc_edit == 'Nome' or opc_edit == 'nome':
        novo_nome = input('  Digite o novo nome: ')

        #comando que efetivamente modifica o dado informado
        c.execute('''
        UPDATE produtos
        SET nome = ?
        WHERE id = ?;
        ''',(novo_nome, id_produto))
        criandoTB()
        confir = input('  Confirma essa alteração (S/N)? ')
        if confir == 'S' or confir == 's':
            conn.commit()
            print('''
         * Dados atualizados com sucesso! *''')
        else:
            apagarTela()
            subMenuEstoque()
    elif opc_edit == 'Quantidade' or opc_edit == 'quantidade':
        nova_qnt = input('  Digite a nova quantidade: ')
        c.execute('''
        UPDATE produtos
        SET qnt = ?
        WHERE id = ?;
        ''',(nova_qnt, id_produto))
        conn.commit()
        print('''
     * Dados atualizados com sucesso! *''')
        criandoTB()
        confir = input('  Confirma essa alteração (S/N)? ')
        if confir == 'S' or confir == 's':
            conn.commit()
            print('''
         * Dados atualizados com sucesso!''')
        else:
            apagarTela()
            subMenuEstoque()
    elif opc_edit == 'Valor compra' or opc_edit == 'valor compra':
        novo_vlrCompra = input('  Digite o novo valor de compra: ')
        c.execute('''
        UPDATE produtos
        SET vlr_compra = ?
        WHERE id = ?;
        ''',(novo_vlrCompra, id_produto))
        conn.commit()
        print('''
     * Dados atualizados com sucesso! *''')
        criandoTB()
        confir = input('  Confirma essa alteração (S/N)? ')
        if confir == 'S' or confir == 's':
            conn.commit()
            print('''
         * Dados atualizados com sucesso!''')
        else:
            apagarTela()
            subMenuEstoque()
    elif opc_edit == 'Valor venda' or opc_edit == 'valor venda':
        novo_vlrVenda = input('  Digite o novo valor de venda: ')
        c.execute('''
        UPDATE produtos
        SET vlr_venda = ?
        WHERE id = ?;
        ''',(novo_vlrVenda, id_produto))
        conn.commit()
        print('''
     * Dados atualizados com sucesso! *''')
        criandoTB()
        confir = input('  Confirma essa alteração (S/N)? ')
        if confir == 'S' or confir == 's':
            conn.commit()
            print('''
         * Dados atualizados com sucesso! *''')
        else:
            apagarTela()
            subMenuEstoque()
    elif opc_edit == 'Grupo' or opc_edit == 'grupo':
        novo_grupo = input('  Digite o novo grupo: ')
        c.execute('''
        UPDATE produtos
        SET grupo = ?
        WHERE id = ?;
        ''',(novo_grupo, id_produto))
        conn.commit()
        print('''
     * Dados atualizados com sucesso! *''')
        criandoTB()
        confir = input('  Confirma essa alteração (S/N)? ')
        if confir == 'S' or confir == 's':
            conn.commit()
            print('''
         * Dados atualizados com sucesso! *''')
        else:
            apagarTela()
            subMenuEstoque()

    v_menu = input('  Deseja continuar editando (S/N)? ')
    if v_menu == 'S' or v_menu == 's':
        apagarTela()
        editProd()
    else:
        apagarTela()
        subMenuEstoque()

#função sub menu estoque
def subMenuEstoque():
    opc_estoque = input('''
  ----------------------------------------------------
          ADEGA GOMES DISTRIBUIDORA DE BEBIDAS
  ----------------------------------------------------
                   * MENU ESTOQUE *

       1 - Cadastro / 2 - Consulta / 3 - Alterações

       4 - Exclusão                  0 - Voltar

   Escolha uma opção para continuar: ''')
    if opc_estoque == '1':
        apagarTela()
        inserirProd()
    elif opc_estoque == '2':
        apagarTela()
        consultProd()
    elif opc_estoque == '3':
        apagarTela()
        editProd()
    else:
        apagarTela()
        menuInicial()

#criando menu inicial
def menuInicial():
    opc_inicial = input('''
  ----------------------------------------------------
          ADEGA GOMES DISTRIBUIDORA DE BEBIDAS
  ----------------------------------------------------
                   + Menu Inicial +

       1 - Estoque / 2 - Clientes / 3 - Vendas

   Escolha uma opção para continuar: ''')
   #criando as opções que levaram aos submenus
    if opc_inicial == '1':
        apagarTela()
        subMenuEstoque()
    elif opc_inicial == '2':
        apagarTela()
        subMenuClientes()
    elif opc_inicial == '3':
        apagarTela()
        subMenuVendas()

menuInicial()

conn.close()
