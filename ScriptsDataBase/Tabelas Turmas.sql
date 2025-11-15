CREATE TABLE turmas (
	cod_tur int unsigned auto_increment,
    id_grade int unsigned not null,
    cap_max int unsigned not null,
    dia_oco varchar(30),
    periodo varchar(30),
    prof_resp int unsigned,
    sit		enum('Ativado','Inativado'),
    constraint pk_cod_tur primary key (cod_tur),
    constraint fk_id_grade foreign key (id_grade) references grade(id_grade),
    constraint fk_prof_resp foreign key (prof_resp) references pessoas(reg_ins)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci