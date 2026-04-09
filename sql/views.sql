-- View 1 Média de temperatura por data
CREATE OR REPLACE VIEW avg_temp_por_dispositivo AS
SELECT 
    noted_date,
    AVG(temp) as avg_temp
FROM temperature_readings
GROUP BY noted_date;

-- View 2 Contagem de leituras por hora do dia
-- Extrai a hora diretamente do texto da data (formato: DD-MM-YYYY HH:MI)
DROP VIEW IF EXISTS leituras_por_hora;
CREATE VIEW leituras_por_hora AS
SELECT 
    CAST(SPLIT_PART(SPLIT_PART(noted_date, ' ', 2), ':', 1) AS INTEGER) as hora,
    COUNT(*) as contagem
FROM temperature_readings
GROUP BY hora
ORDER BY hora;

-- View 3 Temperatura máxima e mínima por dia
DROP VIEW IF EXISTS temp_max_min_por_dia;
CREATE VIEW temp_max_min_por_dia AS
SELECT 
    SUBSTRING(noted_date FROM 1 FOR 10) as data,
    MAX(temp) as temp_max,
    MIN(temp) as temp_min
FROM temperature_readings
GROUP BY data
ORDER BY data;