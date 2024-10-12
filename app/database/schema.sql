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
    watering_interval_days INTEGER,
    on_duration INTEGER,
    last_watering TIMESTAMP,
    FOREIGN KEY (plant_id) REFERENCES plants(id),
    FOREIGN KEY (nutrient_id) REFERENCES nutrients(id)
);

INSERT INTO plants (port, name) VALUES (1, 'Planta A');
INSERT INTO nutrients (port, name) VALUES (2, 'Nutriente X');
INSERT INTO routines (plant_id, nutrient_id, watering_interval_days, on_duration, last_watering) VALUES (1, 1, 1, 3, '2024-03-20 00:00:00');
