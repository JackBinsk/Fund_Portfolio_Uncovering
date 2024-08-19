import pandas as pd


def explodir_fundo(nome_fundo,output_externo,modo_output=None):



    """
    Executa a função com base nos parâmetros fornecidos.

    Args:
        nome_fundo (str): Nome do fundo a ser processado.
        
        output_externo (str): Aceita 'exportar' ou 'noexportar'.
        Caso o argumeto output_externo seja 'exportar' a função irá exportará um excel no diretório do script contendo uma aba com todos os ativos e fundos investidos
        diretos e indiretos pelo fundo, junto com outra aba contendo somente os ativos, excluindo os fundos, investidos pelo fundo raiz
        
        modo_output (str): Aceita 'all' ou 'nofunds'. 
        O parametro modo_output só funcionará caso o argumento output_extorno seja "noexterno". O output pode também ser ignorado, para caso o argumento anterior seja "externo"
        Caso o argumento modo_output seja 'all' a função irá retornar uma variável que contém TODOS OS ATIVOS investidos diretamente e indiretamente pelo fundo.
        Caso o argumento modo_output seja 'nofunds' a função irá retornar uma variável que contém SOMENTE OS ATIVOS NÃO FUNDOS investidos direto ou indiretamente pelo fundo.
        

    Raises:
        ValueError: Se os valores de 'output_externo' ou 'modo_output' não forem válidos.
    """


# Verificação dos valores aceitos para output_externo e modo_output
    if output_externo not in ['exportar', 'noexportar']:
        raise ValueError("O parâmetro 'output_externo' deve ser 'exportar' ou 'noexportar'.")
    
    if modo_output not in ['all', 'nofunds','agrupado',None]:
        raise ValueError("O parâmetro 'modo_output' deve ser 'all' ou 'nofunds'.")
    
    nome_carteira = nome_fundo

# Importa a carteira do fundo para ser processada
    fundos_list = pd.read_excel("Explodir carteiras.xlsx")
    fundos_list['Fundos'] = fundos_list['Fundos'].str.lower()


    df_fundo = pd.read_excel(f"carteiras/{nome_carteira}.xlsx")
    fundo = df_fundo
    fundo['Carteira'] = nome_carteira
    fundo['Ativo'] = fundo['Ativo'].str.lower()
    fundo['Caminho'] = nome_carteira
    fundo['Check'] = 0

    empty_list = []
    contagem = 0

#### ======= Processamento de Explosão dos Fundos ======= ####

    while contagem < 6:
        for key, asset in enumerate(fundo['Ativo']):
            if asset in fundos_list['Fundos'].unique() and fundo.loc[key, 'Check'] == 0:

                # Marca o ativo como processado
                fundo.loc[key, 'Check'] = 1

                caminho = fundo.loc[key, 'Caminho']
                financeiro_pi_investor_on_asset = fundo.loc[key, 'Financeiro']

                # Carrega a carteira do fundoo investido
                invested_fundo = pd.read_excel(f'carteiras/{asset}.xlsx')
                invested_fundo['Carteira'] = asset
                invested_fundo['Check'] = 0
                invested_fundo['Financeiro'] = invested_fundo['%PI'] * financeiro_pi_investor_on_asset
                invested_fundo['%PI'] = invested_fundo['Financeiro'] / sum(fundo['Financeiro'])
                invested_fundo['Caminho'] = caminho + '_' + asset

                # Concatena os novos ativos ao DataFrame original
                fundo = pd.concat([fundo, invested_fundo], ignore_index=True)

        contagem += 1
    
    
# Filtra o DataFrame para remover fundos da lista e recalcula o percentual
    fundo_filtrado = fundo[~fundo['Ativo'].isin(fundos_list['Fundos'])]
    fundo_filtrado = fundo_filtrado.copy()

    fundo_filtrado['%PI'] = fundo_filtrado['Financeiro']/sum(fundo_filtrado['Financeiro'])

    fundo_agrupado = fundo_filtrado[['Ativo','Financeiro','%PI']].groupby('Ativo').sum().sort_values(by='Financeiro',ascending=False)
#### ======= Verificação de Consistência dos Dados ======= ####
    
    print(f"""
##########  Checando explosão ###########

Fundos encontrados na varredura: {len(fundo[fundo['Ativo'].isin(fundos_list['Fundos'])])}      
Fundos processados: {len(fundo[fundo['Check']==1])}

PL Original: {sum(df_fundo['Financeiro'])}
PL Explodido: {sum(fundo_filtrado['Financeiro'])}""")
    


# Verifica se o valor explodido bate com o valor original
    if sum(df_fundo['Financeiro']) == sum(fundo_filtrado['Financeiro']):
        print(f"Diferencia: {sum(df_fundo['Financeiro']) - sum(fundo_filtrado['Financeiro'])} \n\nPL: OK.")
    else:
        print(f"Diferencia: {sum(df_fundo['Financeiro']) - sum(fundo_filtrado['Financeiro'])} \n\nPL: Not OK.")
    
    if len(fundo[fundo['Ativo'].isin(fundos_list['Fundos'])]) == len(fundo[fundo['Check']==1]):
        print("Fundos Processados: OK.")
    else:
        print("Fundos Processados: Not OK.")

    
#### ======= Exportação dos Resultados ======= ####
        
# parametro exportar
    if output_externo == 'exportar':

        result = fundo[fundo['Ativo'].isin(fundos_list['Fundos'])]

        with pd.ExcelWriter('fundo explodido.xlsx') as writer:
            fundo.to_excel(writer, sheet_name='all_assets',index=False)
            fundo_filtrado.to_excel(writer, sheet_name='without_funds',index=False)
            fundo_agrupado.reset_index().to_excel(writer, sheet_name ='agrupado',index=False)
        
        print("\nExportado!")

# parametro noexportar
    if output_externo == 'noexportar':
        if modo_output == 'all':
            return fundo
        elif modo_output == 'nofunds':
            return fundo_filtrado
        elif modo_output =='agrupado':
            return fundo_agrupado.reset_index()
        else:
            raise ValueError("O parâmetro 'modo_output' deve ser 'all' ou 'nofunds'.")
