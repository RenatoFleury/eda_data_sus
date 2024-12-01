


def mes_para_numero(nome_mes):
    """
    Converte o nome de um mês para o número correspondente.
    
    Args:
        nome_mes (str): O nome do mês (exemplo: "janeiro", "Fevereiro").
    
    Returns:
        int: O número do mês (1 para janeiro, 12 para dezembro).
        None: Caso o nome do mês não seja válido.
    """
    meses = {
        "janeiro": 1, "fevereiro": 2, "março": 3, "abril": 4, 
        "maio": 5, "junho": 6, "julho": 7, "agosto": 8, 
        "setembro": 9, "outubro": 10, "novembro": 11, "dezembro": 12
    }
    
    # Converter para minúsculas para lidar com nomes maiúsculos ou mistos
    nome_mes = nome_mes.lower().strip()
    return meses.get(nome_mes)


def categorize_period(year):
    if year < 2020:
        return "pre_pand"
    elif year > 2021:
        return "pos_pand"
    else:
        return "pand"