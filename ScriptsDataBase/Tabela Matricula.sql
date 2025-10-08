CREATE TABLE `matricula` (
  `matricula` int unsigned NOT NULL AUTO_INCREMENT,
  `cod_tur` tinyint unsigned DEFAULT NULL,
  `reg_ins` int unsigned DEFAULT NULL,
  `sit` varchar(30) DEFAULT NULL,
  `faltas` tinyint unsigned DEFAULT NULL,
  `nota1` decimal(3,1) DEFAULT NULL,
  `nota2` decimal(3,1) DEFAULT NULL,
  `nota3` decimal(3,1) DEFAULT NULL,
  `nota4` decimal(3,1) DEFAULT NULL,
  `media` decimal(3,1) DEFAULT NULL,
  `dat_ini` date DEFAULT NULL,
  `dat_fin` date DEFAULT NULL,
  PRIMARY KEY (`matricula`),
  KEY `reg_ins` (`reg_ins`),
  KEY `cod_tur` (`cod_tur`),
  CONSTRAINT `matricula_ibfk_1` FOREIGN KEY (`reg_ins`) REFERENCES `pessoas` (`reg_ins`),
  CONSTRAINT `matricula_ibfk_2` FOREIGN KEY (`cod_tur`) REFERENCES `turmas` (`cod_tur`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci