CREATE DATABASE IF NOT EXISTS login_system_db;
USE login_system_db;

CREATE TABLE IF NOT EXISTS users (
    id_user INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    passw VARCHAR(50) NOT NULL,
    nombre VARCHAR(100) NOT NULL
);

INSERT INTO users (username, passw, nombre) VALUES ('admin', 'admin123', 'Super admin');


-- ===== Tabla de productos =====
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL
);

INSERT INTO productos (nombre, precio, stock) VALUES
    ('Laptop HP', 12500.50, 10),
    ('Mouse Inalámbrico', 350.00, 25),
    ('Teclado Mecánico', 850.00, 15);
