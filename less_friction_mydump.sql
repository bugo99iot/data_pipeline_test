-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: less_friction_mydatabase
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer1_data`
--

DROP TABLE IF EXISTS `customer1_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer1_data` (
  `Region` text,
  `Kontakter` bigint(20) DEFAULT NULL,
  `Varav nya kontakter` bigint(20) DEFAULT NULL,
  `Varav kontakter storkund` bigint(20) DEFAULT NULL,
  `Varav kontakter prio` bigint(20) DEFAULT NULL,
  `Besok` bigint(20) DEFAULT NULL,
  `Telemoten` bigint(20) DEFAULT NULL,
  `Webmoten` bigint(20) DEFAULT NULL,
  `Bokn besok` bigint(20) DEFAULT NULL,
  `Bokn telemoten` bigint(20) DEFAULT NULL,
  `Bokn webmoten` bigint(20) DEFAULT NULL,
  `Offerter` bigint(20) DEFAULT NULL,
  `Inringda avtal` bigint(20) DEFAULT NULL,
  `Seminarieavtal` bigint(20) DEFAULT NULL,
  `Eget avtal` bigint(20) DEFAULT NULL,
  `Mailat avtal` bigint(20) DEFAULT NULL,
  `Partneravtal` bigint(20) DEFAULT NULL,
  `Premier` bigint(20) DEFAULT NULL,
  `Date` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer1_data`
--

LOCK TABLES `customer1_data` WRITE;
/*!40000 ALTER TABLE `customer1_data` DISABLE KEYS */;
INSERT INTO `customer1_data` VALUES ('STORKUND      ',57,4,32,40,4,0,0,5,0,0,1,0,0,0,0,0,0,'2017-09-11'),('AFT           ',186,29,11,59,13,3,0,7,1,0,6,0,0,0,0,0,0,'2017-09-11'),('INKASSO       ',253,163,18,99,0,1,0,0,0,0,2,0,0,0,0,0,0,'2017-09-11'),('LEASING       ',39,11,7,27,3,0,0,9,0,0,0,0,0,0,0,0,0,'2017-09-11'),('BILLING       ',0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'2017-09-11'),('SALJFINANS    ',101,50,8,55,42,0,0,25,0,0,1,4,0,3,0,0,1995,'2017-09-11'),('WEBPAY        ',100,42,13,48,2,3,6,7,2,2,21,0,0,5,0,0,3890,'2017-09-11'),('INNESALJ STORK',42,2,32,38,0,0,0,2,2,0,0,0,0,0,0,0,0,'2017-09-11'),('INNESALJ      ',174,44,18,72,0,0,0,1,2,6,1,0,0,0,0,0,0,'2017-09-11');
/*!40000 ALTER TABLE `customer1_data` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-10-11  9:24:58
