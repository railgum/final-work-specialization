-- 7. В подключенном MySQL репозитории создать базу данных “Друзья
-- человека”
CREATE DATABASE man_friends;
USE man_friends;
-- 8. Создать таблицы с иерархией из диаграммы в БД
CREATE TABLE animals(
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Type VARCHAR(50) NOT NULL
);
INSERT INTO animals (Type)
VALUES ('Home_Animals'),
    ('Pack_Animals');
CREATE TABLE home_animals (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    View_name VARCHAR (20),
    Type_id INT,
    FOREIGN KEY (Type_id) REFERENCES animals (ID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO home_animals (View_name, Type_id)
VALUES ('Cats', 1),
    ('Dogs', 1),
    ('Hamsters', 1);
CREATE TABLE pack_animals (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    View_name VARCHAR (20),
    Type_id INT,
    FOREIGN KEY (Type_id) REFERENCES animals (ID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO pack_animals (View_name, Type_id)
VALUES ('Horses', 2),
    ('Donkeys', 2),
    ('Camels', 2);
-- 9. Заполнить низкоуровневые таблицы именами(животных), командами
-- которые они выполняют и датами рождения
CREATE TABLE cats (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Animal_name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    View_id int,
    Foreign KEY (View_id) REFERENCES home_animals (ID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO cats (Animal_name, Birthday, Commands, View_id)
VALUES ('Васька', '2019-04-07', 'Брысь!', 1),
    ('Лиля', '2020-11-21', "Гулять!", 1),
    ('Кекс', '2017-09-14', "Голос!", 1);
CREATE TABLE dogs (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Animal_name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    View_id int,
    Foreign KEY (View_id) REFERENCES home_animals (ID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO dogs (Animal_name, Birthday, Commands, View_id)
VALUES ('Джек', '2022-01-04', 'Дай лапу!', 2),
    ('Байден', '2017-12-12', "Упал!", 2),
    ('Юля', '2020-05-10', "Лежать!", 2);
CREATE TABLE hamsters (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Animal_name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    View_id int,
    Foreign KEY (View_id) REFERENCES home_animals (ID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO hamsters (Animal_name, Birthday, Commands, View_id)
VALUES ('Жирный', '2022-11-02', 'Беги!', 3),
    ('Дрищ', '2021-03-12', "Жри!", 3),
    ('Марго', '2022-10-15', "Улыбочку!", 3);
CREATE TABLE horses (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Horses_name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    View_id int,
    Foreign KEY (View_id) REFERENCES pack_animals (ID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO horses (Animal_name, Birthday, Commands, View_id)
VALUES ('Быстрый', '2017-01-22', 'Пошёл!', 1),
    ('Макар', '2019-08-02', "Н-н-н-о!", 1),
    ('Рассвет', '2012-04-15', "Стоять!", 1);
CREATE TABLE camels (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Animal_name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    View_id int,
    Foreign KEY (View_id) REFERENCES pack_animals (ID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO camels (Animal_name, Birthday, Commands, View_id)
VALUES ('Джон', '2015-10-02', 'Плюнь!', 2),
    ('Бон', '2017-08-17', "Ляг!", 2),
    ('Джови', '2016-04-13', "Встань!", 2);
CREATE TABLE donkeys (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Animal_name VARCHAR(20),
    Birthday DATE,
    Commands VARCHAR(50),
    View_id int,
    Foreign KEY (View_id) REFERENCES pack_animals (ID) ON DELETE CASCADE ON UPDATE CASCADE
);
INSERT INTO donkeys (Animal_name, Birthday, Commands, View_id)
VALUES ('Иа', '2011-10-02', 'Вперёд!', 3),
    ('Джим', '2012-03-12', "Влево!", 3),
    ('Керри', '2013-04-05', "Вправо!", 3);
-- 10. Удалив из таблицы верблюдов, т.к. верблюдов решили перевезти в другой
-- питомник на зимовку. Объединить таблицы лошади, и ослы в одну таблицу.
DELETE FROM camels;
SELECT *
FROM horses
UNION ALL
SELECT *
FROM donkeys;
-- 11.Создать новую таблицу “молодые животные” в которую попадут все
-- животные старше 1 года, но младше 3 лет и в отдельном столбце с точностью
-- до месяца подсчитать возраст животных в новой таблице
CREATE VIEW all_animals AS
SELECT *
FROM horses
UNION ALL
SELECT *
FROM donkeys
UNION ALL
SELECT *
FROM dogs
UNION ALL
SELECT *
FROM cats
UNION ALL
SELECT *
FROM hamsters;
CREATE TABLE young_animals
SELECT Animal_name,
    Birthday,
    TIMESTAMPDIFF(MONTH, Birthday, CURDATE()) AS Age
FROM all_animals
WHERE TIMESTAMPDIFF(YEAR, Birthday, CURDATE()) BETWEEN 1 AND 3;
-- 12. Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
-- прошлую принадлежность к старым таблицам.
CREATE TABLE union_all_tables
SELECT h.Animal_name,
    h.Birthday,
    h.Commands,
    pa.View_name,
    ya.Age_months
FROM horses h
    LEFT JOIN young_animals ya ON ya.Animal_name = h.Animal_name
    LEFT JOIN pack_animals pa ON pa.ID = h.View_id
UNION
SELECT d.Animal_name,
    d.Birthday,
    d.Commands,
    pa.View_name,
    ya.Age_months
FROM donkeys d
    LEFT JOIN young_animals ya ON ya.Animal_name = d.Animal_name
    LEFT JOIN pack_animals pa ON pa.ID = d.View_id
UNION
SELECT c.Animal_name,
    c.Birthday,
    c.Commands,
    ha.View_name,
    ya.Age_months
FROM cats c
    LEFT JOIN young_animals ya ON ya.Animal_name = c.Animal_name
    LEFT JOIN home_animals ha ON ha.ID = c.View_id
UNION
SELECT d.Animal_name,
    d.Birthday,
    d.Commands,
    ha.View_name,
    ya.Age_months
FROM dogs d
    LEFT JOIN young_animals ya ON ya.Animal_name = d.Animal_name
    LEFT JOIN home_animals ha ON ha.ID = d.View_id
UNION
SELECT hm.Animal_name,
    hm.Birthday,
    hm.Commands,
    ha.View_name,
    ya.Age_months
FROM hamsters hm
    LEFT JOIN young_animals ya ON ya.Animal_name = hm.Animal_name
    LEFT JOIN home_animals ha ON ha.ID = hm.View_id;