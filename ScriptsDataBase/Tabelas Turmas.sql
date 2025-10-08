CREATE TABLE `turmas` (
  `cod_tur` tinyint(3) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `cod_cur` smallint unsigned DEFAULT NULL,
  `cod_mat` smallint unsigned DEFAULT NULL,
  `periodo` varchar(30) DEFAULT NULL,
  `max_cap` tinyint unsigned DEFAULT NULL,
  `sem_ind` tinyint unsigned DEFAULT NULL,
  `prf_res` int unsigned DEFAULT NULL,
  `sit` enum('Ativo','Inativo') DEFAULT NULL,
  PRIMARY KEY (`cod_tur`),
  KEY `cod_cur` (`cod_cur`),
  KEY `cod_mat` (`cod_mat`),
  KEY `prf_res` (`prf_res`),
  CONSTRAINT `turmas_ibfk_1` FOREIGN KEY (`cod_cur`) REFERENCES `cursos` (`cod_cur`),
  CONSTRAINT `turmas_ibfk_2` FOREIGN KEY (`cod_mat`) REFERENCES `materia` (`cod_mat`),
  CONSTRAINT `turmas_ibfk_3` FOREIGN KEY (`prf_res`) REFERENCES `pessoas` (`reg_ins`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci