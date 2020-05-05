DROP DATABASE IF EXISTS sample_db;
CREATE DATABASE sample_db;
USE sample_db;
CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(30) NOT NULL,
  age INT,
  PRIMARY KEY (id)
);