# Autor: Fulano João [Nome do autor que gerou este documento] 
# Data: 01/01/2025 [dd/mm/yyyy]
# Atualização: Cicrano 05/02/2025 [Nome da pessoa e data de atualização]
# Descrição: [O que este arquivo deve fazer]"

def nome_da_funcao(
                    param1: tipo,
                    param2: tipo = valor_padrao
                    ) -> tipo_retorno:
    """
    [Título resumido do que a função faz]

    ### Descrição:
    [Explicação detalhada sobre o propósito da função, como funciona e onde pode ser usada.]

    ### Parâmetros:
    - **param1** (*tipo*): [Descrição detalhada do primeiro parâmetro.]
    - **param2** (*tipo*, opcional): [Descrição do segundo parâmetro, se for opcional, indique o valor padrão.]

    ### Retorno:
    - (*tipo_retorno*): [Descrição do valor retornado pela função.]

    ### Exceções:
    - **TipoErro**: [Se aplicável, descreva as exceções que podem ser levantadas.]
    - **ValueError**: [Outra exceção relevante, se houver.]

    ### Exemplo de Uso:
    ```python
    resultado = nome_da_funcao(valor1, valor2)
    print(resultado)  # Saída esperada: [...]
    ```

    ### Notas:
    - [Observações adicionais sobre o comportamento da função.]
    - [Restrições ou considerações especiais.]

    ### Autor:
    - Nome: [Seu Nome]
    - Data de criação: [DD/MM/AAAA]
    - Versão: [1.0]
    """
    ...  # Implementação da função

# EXEMPLOS DE CRIAÇÃO DA FUNÇÃO

def calcular_desconto(
    preco_original: float, 
    percentual_desconto: float, 
    aplicar_arredondamento: bool = False
) -> float:
    """
    Calcula o preço final após aplicar um desconto percentual sobre o valor original.

    ### Descrição:
    Esta função recebe um preço original e um percentual de desconto e calcula o 
    valor final após a aplicação do desconto. Opcionalmente, o valor final pode 
    ser arredondado para duas casas decimais.

    ### Parâmetros:
    - **preco_original** (*float*): O preço original do produto ou serviço.  
    - **percentual_desconto** (*float*): O percentual de desconto a ser aplicado (de 0 a 100).  
    - **aplicar_arredondamento** (*bool*, opcional): Se `True`, o resultado será arredondado para 2 casas decimais.  
      O padrão é `False`.

    ### Retorno:
    - (*float*): O preço final após o desconto aplicado. Se `aplicar_arredondamento` for `True`, o valor retornado 
      será arredondado para duas casas decimais.

    ### Exceções:
    - **ValueError**: Se `preco_original` for negativo.
    - **ValueError**: Se `percentual_desconto` não estiver no intervalo de 0 a 100.

    ### Exemplo de Uso:
    ```python
    # Exemplo 1: Desconto de 20% sem arredondamento
    preco_final = calcular_desconto(100.0, 20)
    print(preco_final)  # Saída: 80.0

    # Exemplo 2: Desconto de 35% com arredondamento
    preco_final = calcular_desconto(199.99, 35, aplicar_arredondamento=True)
    print(preco_final)  # Saída: 129.99

    # Exemplo 3: Tentativa de usar um percentual inválido
    try:
        calcular_desconto(100.0, -10)
    except ValueError as e:
        print(e)  # Saída: "O percentual de desconto deve estar entre 0 e 100."
    ```

    ### Notas:
    - Se o desconto for 100%, o retorno será 0.0.
    - Se o desconto for 0%, o retorno será igual ao preço original.

    ### Autor:
    - Nome: João Silva
    - Data de criação: 03/03/2025
    - Versão: 1.0
    """
    if preco_original < 0:
        raise ValueError("O preço original não pode ser negativo.")
    
    if not (0 <= percentual_desconto <= 100):
        raise ValueError("O percentual de desconto deve estar entre 0 e 100.")

    preco_final = preco_original * (1 - percentual_desconto / 100)

    return round(preco_final, 2) if aplicar_arredondamento else preco_final

# Explicação da Estrutura da Docstring
#   Descrição Geral → Explica o que a função faz.
#   Parâmetros (Args: ou Parâmetros:) → Lista os argumentos, seus tipos e detalhes adicionais.
#   Retorno (Returns: ou Retorno:) → Explica o que a função retorna.
#   Exceções (Raises: ou Exceções:) → Indica quais exceções podem ser lançadas e em quais situações.
#   Exemplo de Uso (Example:) → Mostra exemplos práticos de uso.
#   Notas Adicionais (Notes:) → Detalhes extras sobre o funcionamento.
#   Autor e Versão (Author:) → Informações sobre a criação da função.