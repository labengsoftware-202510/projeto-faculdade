CREATE TABLE `disciplinas` (
  `cod_dis` int unsigned NOT NULL AUTO_INCREMENT,
  `nom_dis` varchar(30) NOT NULL,
  `dat_inc` date NOT NULL,
  `tipo` varchar(30) NOT NULL,
  `crg_hor_semanal` int DEFAULT NULL,
  `crg_hor_min_semestral` int DEFAULT NULL,
  `sit` enum('Ativo','Inativo') DEFAULT NULL,
  PRIMARY KEY (`cod_dis`),
  UNIQUE KEY `nom_dis` (`nom_dis`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci