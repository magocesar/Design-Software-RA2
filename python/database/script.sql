CREATE SCHEMA IF NOT EXISTS `bd_design`;

USE bd_design;

CREATE TABLE IF NOT EXISTS fornecedor(
    id_fornecedor INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    cnpj VARCHAR(100) NOT NULL,
    cep VARCHAR(100) NOT NULL
)
