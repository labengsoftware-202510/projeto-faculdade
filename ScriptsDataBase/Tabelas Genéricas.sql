CREATE TABLE `tab_ger` (
  `dominio` varchar(20) NOT NULL,
  `valor` varchar(30) NOT NULL,
  `descricao` varchar(60) NOT NULL,
  `obs` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`dominio`,`valor`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci