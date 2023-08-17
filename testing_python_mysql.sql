-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 17, 2023 at 06:30 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.0.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `testing_python_mysql`
--

-- --------------------------------------------------------

--
-- Table structure for table `tb_data_pengguna`
--

CREATE TABLE `tb_data_pengguna` (
  `id` int(11) NOT NULL,
  `nama` varchar(60) NOT NULL,
  `umur` int(2) NOT NULL,
  `alamat` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `tb_data_pengguna`
--

INSERT INTO `tb_data_pengguna` (`id`, `nama`, `umur`, `alamat`) VALUES
(2, 'Budi Setiawan', 17, 'Sleman'),
(3, 'Eka Surya A', 17, 'Jogja'),
(4, 'Budi', 18, 'Jogja24jam'),
(5, 'Luqman Hakim', 17, 'Kidul STEMSA'),
(6, 'Miranti Mitayani', 16, 'Bantul'),
(7, '', 0, 'd');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `tb_data_pengguna`
--
ALTER TABLE `tb_data_pengguna`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `tb_data_pengguna`
--
ALTER TABLE `tb_data_pengguna`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
