-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 20 Nov 2023 pada 10.53
-- Versi server: 10.4.27-MariaDB
-- Versi PHP: 7.4.33

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `wisata`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `penilaian`
--

CREATE TABLE `penilaian` (
  `id` int(11) NOT NULL,
  `daya_tarik` int(11) NOT NULL,
  `aksesbilitas` int(11) NOT NULL,
  `fasilitas` int(11) NOT NULL,
  `pelayanan` int(11) NOT NULL,
  `kebersihan` int(11) NOT NULL,
  `promosi` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `penilaian`
--

INSERT INTO `penilaian` (`id`, `daya_tarik`, `aksesbilitas`, `fasilitas`, `pelayanan`, `kebersihan`, `promosi`) VALUES
(2, 5, 7, 4, 3, 5, 6),
(3, 5, 7, 4, 3, 5, 6),
(4, 7, 8, 6, 4, 3, 5),
(5, 4, 3, 5, 7, 8, 9),
(6, 7, 6, 5, 4, 3, 6),
(7, 4, 6, 7, 8, 9, 2),
(8, 3, 4, 5, 6, 5, 4),
(9, 5, 6, 7, 8, 4, 3),
(10, 5, 6, 5, 7, 6, 5),
(11, 4, 3, 5, 7, 8, 9),
(12, 4, 3, 2, 5, 6, 7);

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `penilaian`
--
ALTER TABLE `penilaian`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `penilaian`
--
ALTER TABLE `penilaian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
