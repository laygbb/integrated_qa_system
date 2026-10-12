CREATE DATABASE edu_rag CHARACTER SET utf8 COLLATE utf8_general_ci;

use edu_rag;
 CREATE TABLE IF NOT EXISTS jpkb (
            id INT AUTO_INCREMENT PRIMARY KEY,
            subject_name VARCHAR(20),
            question VARCHAR(1000),
            answer VARCHAR(1000)
            );