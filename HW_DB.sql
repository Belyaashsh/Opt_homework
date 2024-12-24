-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/

-- Хост: localhost
-- Время создания: Дек 24 2024 г., 19:27
-- Версия сервера: 10.4.28-MariaDB
-- Версия PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

CREATE DATABASE HW_DB;
CREATE USER 'belyaashsh'@'localhost' IDENTIFIED BY '12345678';
GRANT ALL PRIVILEGES ON HW_DB.* TO 'belyaashsh'@'localhost';
FLUSH PRIVILEGES;
--
-- База данных: `HW_DB`
--

-- --------------------------------------------------------

--
-- Структура таблицы `Grades`
--

CREATE TABLE `Grades` (
  `Student_id` int(11) NOT NULL,
  `Subject_id` int(11) NOT NULL,
  `Grade` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `Students`
--

CREATE TABLE `Students` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `group_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `Students`
--

INSERT INTO `Students` (`id`, `name`, `group_name`) VALUES
(1, 'Иванов Иван Иванович', 'БИВТ-21-1'),
(2, 'Петров Сергей Антонович', 'БИВТ-21-1'),
(3, 'Семенов Андрей Павлович', 'БИВТ-21-1'),
(4, 'Микла Евгений Эрнестович', 'БИВТ-21-1'),
(5, 'Семенов Андрей Павлович', 'БИВТ-21-1'),
(6, 'Ожегов Юрий Олегович', 'БИВТ-21-1');

-- --------------------------------------------------------

--
-- Структура таблицы `Subjects`
--

CREATE TABLE `Subjects` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subject_name` varchar(255) NOT NULL,
  `grading_system` varchar(255) NOT NULL,
  `hours_for_semesters` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Дамп данных таблицы `Subjects`
--

INSERT INTO `Subjects` (`id`, `subject_name`, `grading_system`, `hours_for_semesters`) VALUES
(1, 'Программирование и алгоритмизация', 'Экзамен', 240),
(2, 'Математика', 'Экзамен', 240),
(3, 'Физика', 'Экзамен', 240),
(4, 'Схемотехника', 'Экзамен', 240),
(5, 'Моделирование бизнес-процессов', 'Зачет', 176),
(6, 'Иностранный язык', 'Зачет с оценкой', 210),
(7, 'Физическая культура', 'Зачет', 120),
(8, 'Системный анализ ', 'Зачет с оценкой', 210),
(9, 'Информационная безопасность', 'Зачет с оценкой', 216),
(10, 'Сети и системы', 'Зачет с оценкой', 176);

-- --------------------------------------------------------

--
-- Индексы таблицы `Grades`
--

ALTER TABLE `Grades`
  ADD KEY `Student_id` (`Student_id`,`Subject_id`),
  ADD KEY `Subject_id` (`Subject_id`);

--
-- Ограничения внешнего ключа таблицы `Grades`
--
ALTER TABLE `Grades`
  ADD CONSTRAINT `grades_ibfk_1` FOREIGN KEY (`Subject_id`) REFERENCES `Subjects` (`id`),
  ADD CONSTRAINT `grades_ibfk_2` FOREIGN KEY (`Student_id`) REFERENCES `Students` (`id`);

COMMIT;

