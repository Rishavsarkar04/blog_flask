CREATE DATABASE  IF NOT EXISTS `codehunter` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `codehunter`;
-- MySQL dump 10.13  Distrib 8.0.25, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: codehunter
-- ------------------------------------------------------
-- Server version	8.0.25

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `serial_no` int NOT NULL AUTO_INCREMENT,
  `name` tinytext NOT NULL,
  `email` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `msg` tinytext NOT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`serial_no`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (2,'Rishav Sarkar','rishavsarkar04@gmail.com','8777475206','check that\r\n','2021-06-13 23:57:09'),(3,'Rishav Sarkar','susa@gmail.com','87774684','Sq','2021-06-14 00:04:27'),(4,'Rishav Sarkar','susa@gmail.com','87774684','adw','2021-06-14 00:20:30'),(5,'Rishav Sarkar','susa@gmail.com','87774684','Sq','2021-06-14 00:21:21'),(6,'Rishav Sarkar','rishavsarkar04@gmail.com','8777475206','check that\r\n','2021-06-14 00:21:48'),(9,'Bol Ami k','adadwd@gmail.com','2222','dadw','2021-06-14 00:22:58'),(10,'Rishav Sarkar','adadwd@gmail.com','8777','wda','2021-06-14 00:30:05');
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `posts`
--

DROP TABLE IF EXISTS `posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `posts` (
  `serial_no` int NOT NULL AUTO_INCREMENT,
  `tittle` tinytext,
  `tagline` tinytext,
  `slug` varchar(30) DEFAULT NULL,
  `content` text,
  `img_file` varchar(20) DEFAULT NULL,
  `date` datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`serial_no`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `posts`
--

LOCK TABLES `posts` WRITE;
/*!40000 ALTER TABLE `posts` DISABLE KEYS */;
INSERT INTO `posts` VALUES (1,'set new tittle for post 1','this is first ','first-post','Stock (also capital stock) is all of the shares into which ownership of a corporation is divided.[1] In American English, the shares are collectively known as \"stock\".[1] A single share of the stock represents fractional ownership of the corporation in proportion to the total number of shares. This typically entitles the stockholder to that fraction of the company\'s earnings, proceeds from liquidation of assets (after discharge of all senior claims such as secured and unsecured debt),[2] or voting power, often dividing these up in proportion to the amount of money each stockholder has invested. Not all stock is necessarily equal, as certain classes of stock may be issued for example without voting rights, with enhanced voting rights, or with a certain priority to receive profits or liquidation proceeds before or after other classes of shareholders..','kk.jpg','2021-06-13 19:57:40'),(2,'this is second post','coolest blog','second-post','Hi, I\'m trying to follow a lecture example for using SQLAlchemy in Python (from the Web Programming class). But I keep getting an error, and I don\'t know what I\'m doing wrong. Can someone please help?','about-bg.jpg','2021-06-07 20:04:16'),(3,'Database Queries','maast blog','third-post','Now that we’ve defined our models and used migrations to build our schema, we’re ready to start manipulating our data.',' ','2021-06-07 23:28:22'),(4,'Quick search','4th tagline','fouth-post','If you’re like me and love your SQL, you’ll understand how frustrating it can be to use a limited ORM. Luckily for us, we’re using one of the most powerful ORMs out there and it can do just about anything that raw SQL can do with its expressive query API.',' ','2021-06-07 23:28:22'),(5,'5 tittle','5 th tag line','fifth-post','Hrithik Roshan (English: /ˈrɪtɪk ˈrɒʃən/, born 10 January 1974) is an Indian actor who works in Hindi films. He has portrayed a variety of characters and is known for his dancing skills. One of the highest-paid actors in India, he has won many awards, including six Filmfares, four for Best Actor and one each for Best Debut and Best Actor (Critics). Starting in 2012, he appeared several times in Forbes India\'s Celebrity 100 based on his income and popularity.',' ','2021-06-07 23:28:22'),(6,'sixth post','6th tag line','sixth-post','Kaho Naa... Pyaar Hai (transl. Say It... You\'re In Love) is a 2000 Indian Hindi-language musical romantic action thriller film directed by Rakesh Roshan, marking the debuts of his son Hrithik Roshan and Ameesha Patel.',' ','2021-06-07 23:28:22'),(10,'lets learn about stock and many thing','this is first post','another-post','Stock (also capital stock) is all of the shares into which ownership of a corporation is divided.[1] In American English, the shares are collectively known as \"stock\".[1] A single share of the stock represents fractional ownership of the corporation in proportion to the total number of shares. This typically entitles the stockholder to that fraction of the company\'s earnings, proceeds from liquidation of assets (after discharge of all senior claims such as secured and unsecured debt),[2] or voting power, often dividing these up in proportion to the amount of money each stockholder has invested. Not all stock is necessarily equal, as certain classes of stock may be issued for example without voting rights, with enhanced voting rights, or with a certain priority to receive profits or liquidation proceeds before or after other classes of shareholders..',' ','2021-06-12 00:35:24'),(11,'tilak posts','pinakaa','1-post','my name is tilak','pod1.jpg','2021-06-12 01:58:45');
/*!40000 ALTER TABLE `posts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-06-16  1:41:05
