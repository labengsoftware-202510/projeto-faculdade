CREATE TABLE `materia` (
  `cod_mat` smallint unsigned NOT NULL,
  `nom_mat` varchar(30) DEFAULT NULL,
  `dat_inc` date DEFAULT NULL,
  `sit` enum('Ativo','Inativo') DEFAULT NULL,
  PRIMARY KEY (`cod_mat`),
  UNIQUE KEY `nom_mat` (`nom_mat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci