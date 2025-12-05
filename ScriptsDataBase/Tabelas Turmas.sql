CREATE TABLE `turmas` (
  `cod_tur` int unsigned NOT NULL AUTO_INCREMENT,
  `id_grade` int unsigned NOT NULL,
  `cap_max` int unsigned NOT NULL,
  `dia_oco` varchar(30) DEFAULT NULL,
  `periodo` varchar(30) DEFAULT NULL,
  `prof_resp` int unsigned DEFAULT NULL,
  `sit` enum('Ativo','Inativo') DEFAULT NULL,
  PRIMARY KEY (`cod_tur`),
  KEY `fk_id_grade` (`id_grade`),
  KEY `fk_prof_resp` (`prof_resp`),
  CONSTRAINT `fk_id_grade` FOREIGN KEY (`id_grade`) REFERENCES `grade` (`id_grade`),
  CONSTRAINT `fk_prof_resp` FOREIGN KEY (`prof_resp`) REFERENCES `pessoas` (`reg_ins`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci