CREATE TABLE `cursos` (
  `cod_cur` smallint unsigned NOT NULL,
  `nom_cur` varchar(30) DEFAULT NULL,
  `dat_inc` date DEFAULT NULL,
  `sit` varchar(30) DEFAULT NULL,
  `estado` enum('Ativo','Inativo') DEFAULT NULL,
  PRIMARY KEY (`cod_cur`),
  UNIQUE KEY `nom_cur` (`nom_cur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci