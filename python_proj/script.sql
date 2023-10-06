CREATE SCHEMA IF NOT EXISTS `bd_design`;

USE bd_design;

CREATE TABLE IF NOT EXISTS Cliente(
    id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(11) NOT NULL,
    telefone VARCHAR(20) NOT NULL,
    cep VARCHAR(12) NOT NULL,
    numero INT NOT NULL,
    complemento VARCHAR(32)
);

CREATE TABLE IF NOT EXISTS Adm(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    login VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL
);

INSERT INTO Cliente (nome, cpf, telefone, cep, numero, complemento) VALUES
('João Silva', '123.456.789-01', '(11) 1234-5678', '12345-678', 123, 'Apt 101'),
('Maria Oliveira', '987.654.321-09', '(22) 9876-5432', '54321-876', 456, 'Casa'),
('Pedro Santos', '456.789.012-34', '(33) 5678-9012', '98765-432', 789, 'Sala 3'),
('Ana Pereira', '789.012.345-67', '(44) 8765-4321', '87654-321', 101, 'Lote 5'),
('Carlos Souza', '234.567.890-12', '(55) 7654-3210', '23456-789', 202, 'Fundos'),
('Fernanda Lima', '890.123.456-78', '(66) 6543-2109', '65432-109', 303, 'Loja 7'),
('Rafael Costa', '345.678.901-23', '(77) 5432-1098', '32109-876', 404, 'Andar 2'),
('Isabela Santos', '789.012.345-67', '(88) 4321-0987', '10987-654', 505, 'Bloco B'),
('Lucas Oliveira', '901.234.567-89', '(99) 3210-9876', '76543-210', 606, 'Casa Verde'),
('Mariana Silva', '543.210.987-65', '(10) 2109-8765', '43210-987', 707, 'Apto 22'),
('Roberto Pereira', '678.901.234-56', '(21) 1098-7654', '21098-765', 808, 'Sala 5'),
('Larissa Souza', '345.678.901-23', '(32) 9876-5432', '87654-321', 909, 'Cobertura'),
('Gustavo Lima', '876.543.210-98', '(43) 7654-3210', '54321-098', 111, 'Fundos'),
('Amanda Costa', '012.345.678-90', '(54) 6543-2109', '32109-876', 222, 'Loja 3'),
('Marcos Santos', '234.567.890-12', '(65) 5432-1098', '10987-654', 333, 'Casa Amarela'),
('Laura Oliveira', '456.789.012-34', '(76) 4321-0987', '09876-543', 444, 'Sala 8'),
('Leonardo Pereira', '789.012.345-67', '(87) 3210-9876', '76543-210', 555, 'Andar 3'),
('Camila Souza', '098.765.432-10', '(98) 2109-8765', '54321-098', 666, 'Bloco C'),
('Rodrigo Lima', '567.890.123-45', '(09) 1098-7654', '21098-765', 777, 'Apto 15'),
('Juliana Costa', '210.987.654-32', '(20) 9876-5432', '87654-321', 888, 'Sala 6'),
('Daniel Santos', '345.678.901-23', '(31) 7654-3210', '54321-098', 999, 'Casa Azul'),
('Leticia Oliveira', '456.789.012-34', '(42) 6543-2109', '10987-654', 1010, 'Loja 1'),
('Bruno Pereira', '567.890.123-45', '(53) 5432-1098', '21098-765', 1212, 'Cobertura'),
('Carolina Lima', '678.901.234-56', '(64) 4321-0987', '09876-543', 1313, 'Fundos'),
('Henrique Souza', '789.012.345-67', '(75) 3210-9876', '76543-210', 1414, 'Sala 2'),
('Natasha Santos', '123.456.789-01', '(86) 2109-8765', '54321-098', 1515, 'Apto 18'),
('Renato Oliveira', '234.567.890-12', '(97) 1098-7654', '21098-765', 1616, 'Loja 4'),
('Vanessa Costa', '345.678.901-23', '(08) 9876-5432', '87654-321', 1717, 'Casa Vermelha'),
('Guilherme Lima', '456.789.012-34', '(19) 6543-2109', '10987-654', 1818, 'Sala 9'),
('Carla Pereira', '567.890.123-45', '(20) 5432-1098', '21098-765', 1919, 'Andar 4'),
('Felipe Souza', '678.901.234-56', '(31) 4321-0987', '09876-543', 2020, 'Bloco D'),
('Aline Santos', '789.012.345-67', '(42) 3210-9876', '76543-210', 2121, 'Apto 12'),
('Luciano Oliveira', '890.123.456-78', '(53) 2109-8765', '54321-098', 2222, 'Sala 7'),
('Patricia Lima', '901.234.567-89', '(64) 1098-7654', '21098-765', 2323, 'Casa Laranja'),
('Vinicius Costa', '012.345.678-90', '(75) 9876-5432', '87654-321', 2424, 'Loja 2'),
('Silvia Santos', '123.456.789-01', '(86) 6543-2109', '10987-654', 2525, 'Cobertura'),
('Tiago Pereira', '234.567.890-12', '(97) 5432-1098', '21098-765', 2626, 'Fundos'),
('Beatriz Souza', '345.678.901-23', '(08) 4321-0987', '09876-543', 2727, 'Sala 1'),
('Eduardo Lima', '456.789.012-34', '(19) 3210-9876', '76543-210', 2828, 'Andar 1'),
('Tatiane Costa', '567.890.123-45', '(20) 2109-8765', '54321-098', 2929, 'Bloco A'),
('Robson Santos', '678.901.234-56', '(31) 1098-7654', '21098-765', 3030, 'Apto 24');
