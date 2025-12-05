CREATE TABLE `matriculas_cursos` (
  `reg_ins` int unsigned NOT NULL,
  `cod_cur` smallint unsigned NOT NULL,
  `dat_inc` date NOT NULL,
  `dat_fin` date DEFAULT NULL,
  `dat_max` date DEFAULT NULL,
  `estado` varchar(30) DEFAULT NULL,
  `sit` enum('Ativo','Inativo') DEFAULT NULL,
  `dip_env` enum('S','N') DEFAULT NULL,
  PRIMARY KEY (`reg_ins`,`cod_cur`,`dat_inc`),
  KEY `fk_cod_cur` (`cod_cur`),
  CONSTRAINT `fk_cod_cur` FOREIGN KEY (`cod_cur`) REFERENCES `cursos` (`cod_cur`),
  CONSTRAINT `fk_reg_ins` FOREIGN KEY (`reg_ins`) REFERENCES `pessoas` (`reg_ins`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci