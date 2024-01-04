-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2024 at 05:38 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cinema_booking`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer_booking`
--

CREATE TABLE `customer_booking` (
  `Name` varchar(30) NOT NULL,
  `Phone_Number` int(20) NOT NULL,
  `Age` int(20) NOT NULL,
  `Movie` varchar(30) NOT NULL,
  `Packs` int(20) NOT NULL,
  `Total_Price` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `customer_booking`
--

INSERT INTO `customer_booking` (`Name`, `Phone_Number`, `Age`, `Movie`, `Packs`, `Total_Price`) VALUES
('Nursyuhaida', 1121505438, 23, 'WISH', 3, 48),
('MIRAGOJES', 2147483647, 17, 'NIGHT HAS COMES', 10, 250),
('aqib arfan', 1132687166, 22, 'WAR ON TERROR', 3, 51),
('Ainin maisara', 1754856394, 24, 'WISH', 1, 16),
('Siti noraziah', 1124506754, 43, 'WAR ON TERROR', 2, 34),
('Aiman Syafiq', 1154656754, 21, 'NIGHT HAS COMES', 3, 75),
('Dayana Batrisyia', 1823457652, 20, 'WISH', 5, 80),
('Seripul Azali', 1823455682, 33, 'WAR ON TERROR', 2, 34),
('Zikri Iqmal', 1121506394, 21, 'WAR ON TERROR', 2, 34),
('Alya Maisara', 1154625621, 26, 'WISH', 4, 64),
('Batrisyia Najwa', 1185236595, 21, 'MIGRATION', 1, 15);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
