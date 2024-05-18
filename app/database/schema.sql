CREATE TABLE plantas (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    porta INTEGER
);

CREATE TABLE nutrientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    porta INTEGER
);

CREATE TABLE rotinas (
    id INTEGER PRIMARY KEY,
    planta_id INTEGER,
    nutriente_id INTEGER,
    frequencia_por_hora INTEGER,
    quantidade_ppm REAL,
    ultima_rega TIMESTAMP,
    FOREIGN KEY (planta_id) REFERENCES planta(id),
    FOREIGN KEY (nutriente_id) REFERENCES nutrientes(id)
);

INSERT INTO plantas (porta, nome) VALUES (1, 'Planta A');
INSERT INTO nutrientes (porta, nome) VALUES (2, 'Nutriente X');
INSERT INTO rotinas (planta_id, nutriente_id, frequencia_por_hora, quantidade_ppm, ultima_rega) VALUES (1, 1, 1, 200.0, '2024-03-20 00:00:00');
