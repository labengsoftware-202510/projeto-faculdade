CREATE TABLE `matriculas_turmas` (
  `reg_ins` int unsigned NOT NULL,
  `cod_tur` int unsigned NOT NULL,
  `estado` varchar(30) NOT NULL,
  `faltas` tinyint DEFAULT NULL,
  `nota1` decimal(4,2) DEFAULT NULL,
  `nota2` decimal(4,2) DEFAULT NULL,
  `nota3` decimal(4,2) DEFAULT NULL,
  `nota4` decimal(4,2) DEFAULT NULL,
  `media` decimal(4,2) DEFAULT NULL,
  `dat_ini` date NOT NULL,
  `dat_fin` date DEFAULT NULL,
  PRIMARY KEY (`reg_ins`,`cod_tur`,`dat_ini`),
  KEY `fk_cod_tur_mat_tur` (`cod_tur`),
  CONSTRAINT `fk_cod_tur_mat_tur` FOREIGN KEY (`cod_tur`) REFERENCES `turmas` (`cod_tur`),
  CONSTRAINT `fk_reg_ins_mat_tur` FOREIGN KEY (`reg_ins`) REFERENCES `pessoas` (`reg_ins`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci