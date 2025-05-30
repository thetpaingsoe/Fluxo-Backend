# CREATE DATABASE fluxo_task_db;

USE fluxo_task_db;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME, 
    create_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);