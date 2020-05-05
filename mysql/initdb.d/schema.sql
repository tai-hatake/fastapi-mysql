DROP DATABASE IF EXISTS sample_db;
CREATE DATABASE sample_db;
USE sample_db;
CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(30) NOT NULL,
  age INT,
  full_name VARCHAR(128),
  email VARCHAR(128),
  hashed_password VARCHAR(128),
  is_active boolean NOT NULL DEFAULT TRUE,
  is_superuser boolean NOT NULL DEFAULT FALSE,
  PRIMARY KEY (id)
);
