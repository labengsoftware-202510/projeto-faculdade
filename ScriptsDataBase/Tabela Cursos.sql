CREATE TABLE `cursos` (
  `cod_cur` smallint unsigned NOT NULL AUTO_INCREMENT,
  `nom_cur` varchar(150) NOT NULL,
  `dat_inc` date DEFAULT NULL,
  `estado` varchar(30) DEFAULT NULL,
  `sit` enum('Ativo','Inativo') DEFAULT NULL,
  PRIMARY KEY (`cod_cur`),
  UNIQUE KEY `nom_cur` (`nom_cur`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci