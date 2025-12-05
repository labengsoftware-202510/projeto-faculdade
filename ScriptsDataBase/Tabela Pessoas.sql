CREATE TABLE `pessoas` (
  `reg_ins` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `nom_com` varchar(150) NOT NULL,
  `cpf` bigint(11) unsigned zerofill NOT NULL,
  `dat_nas` date DEFAULT NULL,
  `cep` int unsigned NOT NULL,
  `num` int DEFAULT NULL,
  `comp` varchar(30) DEFAULT NULL,
  `sit` enum('Ativo','Inativo') DEFAULT NULL,
  `categoria` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`reg_ins`),
  KEY `pessoas_ibfk_1` (`cep`),
  CONSTRAINT `pessoas_ibfk_1` FOREIGN KEY (`cep`) REFERENCES `tab_cep` (`cep`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci