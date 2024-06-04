CREATE TABLE plants (
    id INTEGER PRIMARY KEY,
    name TEXT,
    port INTEGER
);

CREATE TABLE nutrients (
    id INTEGER PRIMARY KEY,
    name TEXT,
    port INTEGER
);

CREATE TABLE routines (
    id INTEGER PRIMARY KEY,
    plant_id INTEGER,
    nutrient_id INTEGER,
    frequency_per_hour INTEGER,
    ppm_quantity REAL,
    last_watering TIMESTAMP,
    FOREIGN KEY (plant_id) REFERENCES plants(id),
    FOREIGN KEY (nutrient_id) REFERENCES nutrients(id)
);

INSERT INTO plants (port, name) VALUES (1, 'Planta A');
INSERT INTO nutrients (port, name) VALUES (2, 'Nutriente X');
INSERT INTO routines (plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering) VALUES (1, 1, 1, 200.0, '2024-03-20 00:00:00');
