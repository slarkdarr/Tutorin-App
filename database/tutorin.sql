-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 21 Apr 2021 pada 18.13
-- Versi server: 10.4.14-MariaDB
-- Versi PHP: 7.3.22

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tutorin`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `bidang`
--

CREATE TABLE `bidang` (
  `username` varchar(255) NOT NULL,
  `bidang` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struktur dari tabel `detailcourse`
--

CREATE TABLE `detailcourse` (
  `namaMapel` varchar(255) NOT NULL,
  `jenjang` varchar(255) NOT NULL,
  `tingkat` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `detailcourse`
--

INSERT INTO `detailcourse` (`namaMapel`, `jenjang`, `tingkat`) VALUES
('Biologi', 'SMA', 1),
('Biologi', 'SMP', 2),
('Biologi', 'SMP', 3),
('Matematika', 'SMA', 1),
('Matematika', 'SMA', 2),
('Matematika', 'SMA', 3),
('Matematika', 'SMP', 1),
('Matematika', 'SMP', 2),
('Matematika', 'SMP', 3),
('Fisika', 'SMA', 1),
('Fisika', 'SMA', 2),
('Fisika', 'SMA', 3),
('Fisika', 'SMP', 1),
('Fisika', 'SMP', 2),
('Fisika', 'SMP', 3),
('Kimia', 'SMA', 1),
('Kimia', 'SMA', 2),
('Kimia', 'SMA', 3),
('Kimia', 'SMP', 1),
('Kimia', 'SMP', 2),
('Kimia', 'SMP', 3),
('Ekonomi', 'SMA', 1),
('Ekonomi', 'SMA', 2),
('Ekonomi', 'SMA', 3),
('Ekonomi', 'SMP', 1),
('Ekonomi', 'SMP', 2),
('Ekonomi', 'SMP', 3),
('Sosiologi', 'SMA', 1),
('Sosiologi', 'SMA', 2),
('Sosiologi', 'SMA', 3),
('Sosiologi', 'SMP', 1),
('Sosiologi', 'SMP', 2),
('Sosiologi', 'SMP', 3),
('Geografi', 'SMA', 1),
('Geografi', 'SMA', 2),
('Geografi', 'SMA', 3),
('Geografi', 'SMP', 1),
('Geografi', 'SMP', 2),
('Geografi', 'SMP', 3),
('Bahasa Inggris', 'SMA', 1),
('Bahasa Inggris', 'SMA', 2),
('Bahasa Inggris', 'SMA', 3),
('Bahasa Inggris', 'SMP', 1),
('Bahasa Inggris', 'SMP', 2),
('Bahasa Inggris', 'SMP', 3),
('Bahasa Indonesia', 'SMA', 1),
('Bahasa Indonesia', 'SMA', 2),
('Bahasa Indonesia', 'SMA', 3),
('Bahasa Indonesia', 'SMP', 1),
('Bahasa Indonesia', 'SMP', 2),
('Bahasa Indonesia', 'SMP', 3),
('Sejarah', 'SMA', 1),
('Sejarah', 'SMA', 2),
('Sejarah', 'SMA', 3),
('Sejarah', 'SMP', 1),
('Sejarah', 'SMP', 2),
('Sejarah', 'SMP', 3);

-- --------------------------------------------------------

--
-- Struktur dari tabel `jadwaltutor`
--

CREATE TABLE `jadwaltutor` (
  `tutorID` int(11) NOT NULL,
  `courseID` int(11) NOT NULL,
  `hari` varchar(255) NOT NULL,
  `jamMulai` int(11) NOT NULL,
  `durasi` int(11) NOT NULL,
  `deskripsi` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `jadwaltutor`
--

INSERT INTO `jadwaltutor` (`tutorID`, `courseID`, `hari`, `jamMulai`, `durasi`, `deskripsi`) VALUES
(1, 0, 'Selasa', 9, 2, 'ajasnd'),
(1, 0, 'Kamis', 10, 2, 'ajnsjds'),
(1, 0, 'Senin', 9, 2, 'anjay');

-- --------------------------------------------------------

--
-- Struktur dari tabel `tutor`
--

CREATE TABLE `tutor` (
  `username` varchar(255) NOT NULL,
  `jenjang` varchar(255) NOT NULL,
  `tarif` int(11) NOT NULL,
  `noKTP` varchar(255) NOT NULL,
  `pengalaman` varchar(255) NOT NULL,
  `pendidikan` varchar(255) NOT NULL,
  `headline` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `tutor`
--

INSERT INTO `tutor` (`username`, `jenjang`, `tarif`, `noKTP`, `pengalaman`, `pendidikan`, `headline`) VALUES
('dwi', 'SD', 1000, '123455666', 'sjndjnfjdnfjfnjdfnj', 'S1', 'SDSKDNKDSNFKNFK');

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `idUser` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `kontak` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `balance` int(11) NOT NULL DEFAULT 0,
  `flag` int(11) NOT NULL DEFAULT 0,
  `rating` float NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`idUser`, `username`, `password`, `nama`, `kontak`, `alamat`, `balance`, `flag`, `rating`) VALUES
(1, 'dwi', '123', 'dwi bagus', '0821', 'jlan', 0, 0, 0),
(2, 'abc', 'djdjd', 'jdjdjd', 'ddjjdjd', 'ddjjdjd', 0, 0, 0),
(3, 'dwi', '123', 'dwi bagus', '0821', 'jlan', 0, 0, 0),
(4, 'dwinbaa', '1234', 'dwi', '1244', 'jalan', 0, 0, 0);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`idUser`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `idUser` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
