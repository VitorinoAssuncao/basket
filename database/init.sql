CREATE DATABASE 'chega_mais' /*!40100 COLLATE 'utf8mb4_general_ci' */;
USE 'chega_mais';


CREATE TABLE 'users' (
	'id' INT NOT NULL AUTO_INCREMENT,
	'login' VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	'password' VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	'name' VARCHAR(100) NULL DEFAULT NULL COLLATE 'utf8mb4_general_ci',
	'birth_date' DATE NULL DEFAULT NULL,
	PRIMARY KEY ('id')
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB
;
