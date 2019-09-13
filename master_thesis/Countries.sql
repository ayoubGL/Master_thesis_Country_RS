-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Aug 27, 2019 at 07:00 PM
-- Server version: 5.7.27-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `master_thesis_django`
--

-- --------------------------------------------------------

--
-- Table structure for table `Countries`
--

CREATE TABLE `Countries` (
  `id` int(11) NOT NULL,
  `country_name` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `Countries`
--

INSERT INTO "Countries" (id, country_name) VALUES
(343, 'Afghanistan'),
(344, 'Albania'),
(345, 'Algeria'),
(346, 'American Samoa'),
(347, 'Andorra'),
(348, 'Angola'),
(349, 'Argentina'),
(350, 'Armenia'),
(351, 'Australia'),
(352, 'Austria'),
(353, 'Azerbaijan'),
(354, 'Bahamas'),
(355, 'Bahrain'),
(356, 'Bangladesh'),
(357, 'Barbados'),
(358, 'Belarus'),
(359, 'Belgium'),
(360, 'Belize'),
(361, 'Bhutan'),
(362, 'Bolivia'),
(363, 'Botswana'),
(364, 'Brazil'),
(365, 'Brunei'),
(366, 'Bulgaria'),
(367, 'Burkina Faso'),
(368, 'Burundi'),
(369, 'Cambodia'),
(370, 'Cameroon'),
(371, 'Canada'),
(372, 'Cabo Verde'),
(373, 'Chad'),
(374, 'Chile'),
(375, 'China'),
(376, 'Colombia'),
(377, 'Comoros'),
(378, 'Congo'),
(379, 'Cook Islands'),
(380, 'Costa Rica'),
(381, 'Côte d&#;Ivoire'),
(382, 'Croatia'),
(383, 'Cuba'),
(384, 'Cyprus'),
(385, 'Czechia'),
(386, 'Denmark'),
(387, 'Djibouti'),
(388, 'Dominica'),
(389, 'Ecuador'),
(390, 'Egypt'),
(391, 'El Salvador'),
(392, 'Eritrea'),
(393, 'Estonia'),
(394, 'Ethiopia'),
(395, 'Fiji'),
(396, 'Finland'),
(397, 'France'),
(398, 'Gabon'),
(399, 'Gambia'),
(400, 'Georgia'),
(401, 'Germany'),
(402, 'Ghana'),
(403, 'Greece'),
(404, 'Grenada'),
(405, 'Guatemala'),
(406, 'Guinea'),
(407, 'Guinea-Bissau'),
(408, 'Guyana'),
(409, 'Haiti'),
(410, 'Honduras'),
(411, 'Hungary'),
(412, 'Iceland'),
(413, 'India'),
(414, 'Indonesia'),
(415, 'Iran'),
(416, 'Iraq'),
(417, 'Ireland'),
(418, 'Italy'),
(419, 'Jamaica'),
(420, 'Japan'),
(421, 'Jordan'),
(422, 'Kenya'),
(423, 'Kuwait'),
(424, 'Kazakhstan'),
(425, 'Latvia'),
(426, 'Lebanon'),
(427, 'Lesotho'),
(428, 'Liberia'),
(429, 'Libya'),
(430, 'Lithuania'),
(431, 'Luxembourg'),
(432, 'Madagascar'),
(433, 'Malawi'),
(434, 'Maldives'),
(435, 'Mali'),
(436, 'Malta'),
(437, 'Mauritius'),
(438, 'Mexico'),
(439, 'Moldova'),
(440, 'Mongolia'),
(441, 'Morocco'),
(442, 'Mozambique'),
(443, 'Myanmar'),
(444, 'Namibia'),
(445, 'Nauru'),
(446, 'Nepal'),
(447, 'Netherlands'),
(448, 'New Zealand'),
(449, 'Nicaragua'),
(450, 'Niger'),
(451, 'Nigeria'),
(452, 'Norway'),
(453, 'Oman'),
(454, 'Pakistan'),
(455, 'Palau'),
(456, 'Palestine'),
(457, 'Panama'),
(458, 'Paraguay'),
(459, 'Peru'),
(460, 'Philippines'),
(461, 'Portugal'),
(462, 'Qatar'),
(463, 'Romania'),
(464, 'Russia'),
(465, 'Saudi Arabia'),
(466, 'Senegal'),
(467, 'Serbia'),
(468, 'Sierra Leone'),
(469, 'Singapore'),
(470, 'Slovakia'),
(471, 'Slovenia'),
(472, 'Solomon Islands'),
(473, 'Somalia'),
(474, 'South Africa'),
(475, 'Spain'),
(476, 'Sri Lanka'),
(477, 'Sudan'),
(478, 'Suriname'),
(479, 'Sweden'),
(480, 'Switzerland'),
(481, 'Syria'),
(482, 'Tajikistan'),
(483, 'Thailand'),
(484, 'Togo'),
(485, 'Tokelau'),
(486, 'Tonga'),
(487, 'Tunisia'),
(488, 'Turkey'),
(489, 'Tuvalu'),
(490, 'Uganda'),
(491, 'Ukraine'),
(492, 'UAE'),
(493, 'UK'),
(494, 'USA'),
(495, 'Uruguay'),
(496, 'Uzbekistan'),
(497, 'Vanuatu'),
(498, 'Venezuela'),
(499, 'Vietnam'),
(500, 'Yemen'),
(501, 'Zambia'),
(502, 'Zimbabwe');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Countries`
--
ALTER TABLE `Countries`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Countries`
--
ALTER TABLE `Countries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=503;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
