--Importante se notar que deverá ser criado como desejar um schema e um database antes de rodar os códigos posteriores:

-- Criação da tabela de usuários
CREATE TABLE `users` (
	`user_id` INT NOT NULL AUTO_INCREMENT,
	`user_login` VARCHAR(50) NOT NULL COLLATE 'latin1_swedish_ci',
	`user_password` VARCHAR(50000) NOT NULL COLLATE 'latin1_swedish_ci',
	`user_email` VARCHAR(50) NOT NULL COLLATE 'latin1_swedish_ci',
	`user_name` VARCHAR(50) NULL DEFAULT '' COLLATE 'latin1_swedish_ci',
	PRIMARY KEY (`user_id`) USING BTREE
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0
;

CREATE TABLE `games` (
	`game_id` INT NOT NULL AUTO_INCREMENT,
	`game_user_id` INT NOT NULL,
	`game_number` INT NOT NULL,
	`game_seasson` INT NOT NULL,
	`game_points` INT NOT NULL,
	PRIMARY KEY (`game_id`) USING BTREE,
	INDEX `game_user_id` (`game_user_id`) USING BTREE,
	CONSTRAINT `FK_games_users` FOREIGN KEY (`game_user_id`) REFERENCES `basket`.`users` (`user_id`) ON UPDATE NO ACTION ON DELETE NO ACTION
)
COLLATE='latin1_swedish_ci'
ENGINE=InnoDB
AUTO_INCREMENT=0
;


