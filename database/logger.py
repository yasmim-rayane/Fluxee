"""
Módulo para gerenciamento do registro de operações do sistema
"""
from datetime import datetime
from typing import Optional


def registrar_operacao(tipo_operacao: str,
                      nome_produto: str,
                      quantidade: int,
                      estoque_restante: int,
                      valor_total: Optional[float] = None) -> None:
    """
    Registra uma operação no arquivo de log.
    
    Args:
        tipo_operacao (str): Tipo da operação (VENDA, ENTRADA, etc)
        nome_produto (str): Nome do produto envolvido
        quantidade (int): Quantidade de itens na operação
        estoque_restante (int): Quantidade restante em estoque
        valor_total (float, opcional): Valor total da operação
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Preparar a linha de log
    log_entry = f"[{timestamp}] {tipo_operacao}"
    log_entry += f" | Produto: {nome_produto}"
    log_entry += f" | Quantidade: {quantidade}"
    
    if valor_total is not None:
        log_entry += f" | Total: R$ {valor_total:.2f}"
        
    log_entry += f" | Estoque Restante: {estoque_restante}"
    log_entry += "\n"
    
    # Abrir arquivo em modo append e escrever o log
    with open("registro.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)
