CREATE TABLE matriculas_turmas (
  reg_ins	int unsigned,
  cod_tur	int unsigned,
  estado	varchar(30) not null,
  faltas	tinyint,
  nota1		decimal(4,2),
  nota2		decimal(4,2),
  nota3		decimal(4,2),
  nota4		decimal(4,2),
  media		decimal(4,2),
  dat_ini	date,
  dat_fin	date,
  constraint pk_mat_tur primary key (reg_ins, cod_tur, dat_ini),
  constraint fk_reg_ins_mat_tur foreign key (reg_ins) references pessoas (reg_ins),
  constraint fk_cod_tur_mat_tur foreign key (cod_tur) references turmas (cod_tur)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci