CREATE DATABASE ccbg;
USE ccbg;


CREATE TABLE `recruits` (
  `rec_id` int NOT NULL AUTO_INCREMENT,
  `firstname` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `email` varchar(50) DEFAULT NULL,
  `iracing_id` varchar(1) DEFAULT NULL,
  PRIMARY KEY (`rec_id`),
  UNIQUE KEY `rec_id` (`rec_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
SHOW TABLES;
SELECT * FROM recruits;