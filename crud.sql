
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";

CREATE TABLE `propertylist` (
  `id` int NOT NULL PRIMARY KEY,
  `name` varchar(255) NOT NULL,
  `phone` varchar(255) NOT NULL,
  'propertyaddress' varchar(255),
  'propertytype' varchar(255),
  'numberofbedrooms' varchar(255),
  'price' float
) ENGINE=MyISAM DEFAULT CHARSET=latin1;


--
--

INSERT INTO `propertylist` (`id`, `name`, `phone`, 'propertyaddress', 'propertytype', 'number of bedrooms', 'price') VALUES
(null, 'zach', '9876543210', 'Tildenwood', 'condo''2', '3000'),
(4, 'Fitsum', '1234567890', 'tild', 'condo' '4', '3000'),




ALTER TABLE `propertylist`
  ADD PRIMARY KEY (`id`);

ALTER TABLE `propertylist`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

