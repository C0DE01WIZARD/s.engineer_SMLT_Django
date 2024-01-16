create table test2 (
id BIGSERIAL NOT NULL PRIMARY KEY,
first_name VARCHAR(50) NOT NULL,
last_name VARCHAR(50) NOT NULL,
gender VARCHAR(50) NOT NULL,
email VARCHAR(50),
data_of_birth DATE NOT NULL,
country_of_birth VARCHAR(50) NOT NULL
);
INSERT INTO test2(first_name, last_name, gender, email, date_of_birth)VALUES('Jonh','Doe', 'MALE','Jd@mail.ru', '2000-01-01')
INSERT INTO test2(first_name, last_name, gender, email, date_of_birth)VALUES('Jon','Do', 'MAL','J@mail.ru', '2000-02-01')

