CREATE TABLE `pessoas` (
  `reg_ins` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `nom_com` varchar(50) DEFAULT NULL,
  `cpf` int DEFAULT NULL,
  `dat_nas` date DEFAULT NULL,
  `cep` int unsigned DEFAULT NULL,
  `num` int DEFAULT NULL,
  `comp` varchar(30) DEFAULT NULL,
  `sit` enum('Ativo','Inativo') DEFAULT NULL,
  PRIMARY KEY (`reg_ins`),
  KEY `cep` (`cep`),
  CONSTRAINT `pessoas_ibfk_1` FOREIGN KEY (`cep`) REFERENCES `tab_cep` (`cep`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci