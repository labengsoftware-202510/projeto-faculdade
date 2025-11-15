CREATE TABLE matriculas_cursos (
  reg_ins	int unsigned,
  cod_cur	smallint unsigned,
  dat_inc	date,
  dat_fin	date,
  dat_max	date,
  estado	varchar(30),
  sit		enum('Ativo','Inativo'),
  dip_env	enum('S','N'),
  primary key (reg_ins, cod_cur, dat_inc),
  constraint fk_reg_ins foreign key (reg_ins) references pessoas(reg_ins),
  constraint fk_cod_cur foreign key (cod_cur) references cursos(cod_cur)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

