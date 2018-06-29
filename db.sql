SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";

CREATE TABLE IF NOT EXISTS `home_devices` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `home_id` int(11) NOT NULL,
  `device_id` varchar(256) NOT NULL,
  `device_name` varchar(256) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `home_id` (`home_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `users` (
  `user_id` varchar(64) CHARACTER SET latin1 NOT NULL,
  `current_home_id` int(11) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `user_homes` (
  `home_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) NOT NULL,
  `remote_id` int(11) NOT NULL,
  `username` varchar(256) NOT NULL,
  `password` varchar(256) NOT NULL,
  `ZBW_SESSID` varchar(128) NOT NULL,
  `ZWAYSession` varchar(128) NOT NULL,
  `name` varchar(100) NOT NULL,
  `state` int(11) NOT NULL DEFAULT '0',
  `update_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `favorite` tinyint(1) NOT NULL,
  PRIMARY KEY (`home_id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `user_requests` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(64) CHARACTER SET latin1 NOT NULL,
  `user_request` varchar(1024) NOT NULL,
  `user_original_request` varchar(1024) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;

