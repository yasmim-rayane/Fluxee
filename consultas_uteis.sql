-- ========================================
-- CONSULTAS SQL ÚTEIS - Sistema WA
-- ========================================

-- ========================================
-- 1. CONSULTAS DE PRODUTOS
-- ========================================

-- Ver todos os produtos com suas categorias
SELECT 
    p.id,
    p.nome AS produto,
    c.nome AS categoria,
    p.valor_unitario,
    p.quantidade_estoque
FROM produtos p
LEFT JOIN categorias c ON p.categoria_id = c.id
ORDER BY c.nome, p.nome;

-- Produtos com estoque baixo (menos de 20 unidades)
SELECT 
    p.nome,
    c.nome AS categoria,
    p.quantidade_estoque,
    p.valor_unitario
FROM produtos p
LEFT JOIN categorias c ON p.categoria_id = c.id
WHERE p.quantidade_estoque < 20
ORDER BY p.quantidade_estoque ASC;

-- Produtos mais caros
SELECT 
    nome,
    valor_unitario,
    quantidade_estoque,
    (valor_unitario * quantidade_estoque) AS valor_total_estoque
FROM produtos
ORDER BY valor_unitario DESC
LIMIT 10;

-- Total de produtos por categoria
SELECT 
    c.nome AS categoria,
    COUNT(p.id) AS total_produtos,
    SUM(p.quantidade_estoque) AS total_estoque
FROM categorias c
LEFT JOIN produtos p ON c.id = p.categoria_id
GROUP BY c.id
ORDER BY total_produtos DESC;

-- ========================================
-- 2. CONSULTAS DE VENDAS
-- ========================================

-- Ver todas as vendas com detalhes
SELECT 
    v.id,
    v.codigo,
    v.data_hora,
    c.nome AS cliente,
    v.valor_total,
    v.forma_pagamento
FROM vendas v
LEFT JOIN clientes c ON v.cliente_id = c.id
ORDER BY v.id DESC;

-- Total de vendas por forma de pagamento
SELECT 
    forma_pagamento,
    COUNT(*) AS total_vendas,
    SUM(valor_total) AS valor_total
FROM vendas
GROUP BY forma_pagamento
ORDER BY valor_total DESC;

-- Vendas por cliente
SELECT 
    c.nome AS cliente,
    COUNT(v.id) AS total_vendas,
    SUM(v.valor_total) AS valor_total_gasto
FROM clientes c
LEFT JOIN vendas v ON c.id = v.cliente_id
GROUP BY c.id
ORDER BY valor_total_gasto DESC;

-- Produtos mais vendidos
SELECT 
    p.nome AS produto,
    SUM(iv.quantidade) AS quantidade_vendida,
    SUM(iv.quantidade * iv.valor_unitario) AS valor_total_vendido
FROM itens_venda iv
LEFT JOIN produtos p ON iv.produto_id = p.id
GROUP BY iv.produto_id
ORDER BY quantidade_vendida DESC;

-- Detalhes de uma venda específica
SELECT 
    v.codigo,
    v.data_hora,
    c.nome AS cliente,
    p.nome AS produto,
    iv.quantidade,
    iv.valor_unitario,
    (iv.quantidade * iv.valor_unitario) AS subtotal
FROM vendas v
LEFT JOIN clientes c ON v.cliente_id = c.id
LEFT JOIN itens_venda iv ON v.id = iv.venda_id
LEFT JOIN produtos p ON iv.produto_id = p.id
WHERE v.id = 1; -- Altere o ID conforme necessário

-- ========================================
-- 3. CONSULTAS DE CLIENTES
-- ========================================

-- Clientes mais ativos (que mais compraram)
SELECT 
    c.nome,
    c.cpf,
    COUNT(v.id) AS total_compras,
    SUM(v.valor_total) AS total_gasto
FROM clientes c
LEFT JOIN vendas v ON c.id = v.cliente_id
GROUP BY c.id
ORDER BY total_compras DESC;

-- Clientes por gênero
SELECT 
    genero,
    COUNT(*) AS total_clientes
FROM clientes
GROUP BY genero;

-- ========================================
-- 4. CONSULTAS DE ENTRADA DE ESTOQUE
-- ========================================

-- Histórico completo de entradas
SELECT 
    e.id,
    p.nome AS produto,
    e.quantidade,
    e.data_hora
FROM entradas_estoque e
LEFT JOIN produtos p ON e.produto_id = p.id
ORDER BY e.id DESC;

-- Total de entradas por produto
SELECT 
    p.nome AS produto,
    COUNT(e.id) AS total_entradas,
    SUM(e.quantidade) AS quantidade_total_entrada
FROM produtos p
LEFT JOIN entradas_estoque e ON p.id = e.produto_id
GROUP BY p.id
HAVING COUNT(e.id) > 0
ORDER BY quantidade_total_entrada DESC;

-- ========================================
-- 5. RELATÓRIOS E ESTATÍSTICAS
-- ========================================

-- Dashboard geral
SELECT 
    (SELECT COUNT(*) FROM categorias) AS total_categorias,
    (SELECT COUNT(*) FROM produtos) AS total_produtos,
    (SELECT COUNT(*) FROM clientes) AS total_clientes,
    (SELECT COUNT(*) FROM vendas) AS total_vendas,
    (SELECT COALESCE(SUM(valor_total), 0) FROM vendas) AS valor_total_vendas,
    (SELECT COALESCE(SUM(quantidade_estoque * valor_unitario), 0) FROM produtos) AS valor_total_estoque;

-- Vendas por mês (últimos 12 meses)
SELECT 
    strftime('%Y-%m', data_hora) AS mes,
    COUNT(*) AS total_vendas,
    SUM(valor_total) AS valor_total
FROM vendas
GROUP BY strftime('%Y-%m', data_hora)
ORDER BY mes DESC;

-- Top 10 produtos por valor em estoque
SELECT 
    nome,
    quantidade_estoque,
    valor_unitario,
    (quantidade_estoque * valor_unitario) AS valor_estoque
FROM produtos
ORDER BY valor_estoque DESC
LIMIT 10;

-- ========================================
-- 6. CONSULTAS DE MANUTENÇÃO
-- ========================================

-- Verificar integridade das Foreign Keys
PRAGMA foreign_key_check;

-- Ver estrutura de uma tabela
PRAGMA table_info(produtos);

-- Listar todas as tabelas
SELECT name FROM sqlite_master WHERE type='table';

-- Ver índices
SELECT * FROM sqlite_master WHERE type='index';

-- ========================================
-- 7. CONSULTAS AVANÇADAS
-- ========================================

-- Produtos nunca vendidos
SELECT 
    p.id,
    p.nome,
    p.quantidade_estoque
FROM produtos p
WHERE p.id NOT IN (SELECT DISTINCT produto_id FROM itens_venda)
ORDER BY p.nome;

-- Ticket médio por venda
SELECT 
    AVG(valor_total) AS ticket_medio
FROM vendas;

-- Melhor dia de vendas
SELECT 
    DATE(data_hora) AS data,
    COUNT(*) AS total_vendas,
    SUM(valor_total) AS valor_total
FROM vendas
GROUP BY DATE(data_hora)
ORDER BY valor_total DESC
LIMIT 1;

-- Produtos com margem de lucro (assumindo custo = 60% do preço)
SELECT 
    nome,
    valor_unitario,
    (valor_unitario * 0.40) AS margem_unitaria,
    quantidade_estoque,
    (valor_unitario * 0.40 * quantidade_estoque) AS margem_total_estoque
FROM produtos
ORDER BY margem_total_estoque DESC;

-- ========================================
-- 8. ANÁLISES DE VENDAS
-- ========================================

-- Análise de vendas por categoria
SELECT 
    c.nome AS categoria,
    COUNT(DISTINCT v.id) AS total_vendas,
    SUM(iv.quantidade) AS quantidade_vendida,
    SUM(iv.quantidade * iv.valor_unitario) AS valor_total
FROM categorias c
JOIN produtos p ON c.id = p.categoria_id
JOIN itens_venda iv ON p.id = iv.produto_id
JOIN vendas v ON iv.venda_id = v.id
GROUP BY c.id
ORDER BY valor_total DESC;

-- Análise temporal de vendas (por hora)
SELECT 
    strftime('%H', data_hora) AS hora,
    COUNT(*) AS total_vendas,
    SUM(valor_total) AS valor_total
FROM vendas
GROUP BY strftime('%H', data_hora)
ORDER BY hora;

-- ========================================
-- 9. EXPORTAÇÕES
-- ========================================

-- Exportar catálogo completo
SELECT 
    c.nome AS categoria,
    p.nome AS produto,
    p.valor_unitario AS preco,
    p.quantidade_estoque AS estoque,
    'R$ ' || printf('%.2f', p.valor_unitario) AS preco_formatado
FROM produtos p
LEFT JOIN categorias c ON p.categoria_id = c.id
ORDER BY c.nome, p.nome;

-- Exportar lista de clientes
SELECT 
    nome,
    cpf,
    data_nascimento,
    genero
FROM clientes
ORDER BY nome;

-- ========================================
-- FIM DAS CONSULTAS
-- ========================================

-- Para executar estas consultas:
-- 1. Abra o DB Browser for SQLite
-- 2. Carregue o arquivo sistema_wa.db
-- 3. Vá na aba "Execute SQL"
-- 4. Cole e execute as consultas desejadas
