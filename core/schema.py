schema="""
CREATE TABLE IF NOT EXISTS `user` (
    `id`                    INT(11) NOT NULL AUTO_INCREMENT,
    `name`                  VARCHAR(50) UNIQUE,
    `email`                 VARCHAR(50),
    `user_type`             INT(3) DEFAULT 2,
    `login_counting`        INT(5) DEFAULT 0,
    `create_datetime`       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `update_datetime`       TIMESTAMP,
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `recipe` (
    `id`                    INT(11) NOT NULL AUTO_INCREMENT,
    `name_kr`               VARCHAR(200),
    `name_en`               VARCHAR(200),
    `desc_kr`               VARCHAR(1000),
    `desc_en`               VARCHAR(1000),
    `image_urls`            VARCHAR(1000),
    `products_urls`         VARCHAR(1000),
    `taken_time`            INT(3),
    `food_type`             INT(3),
    `create_datetime`       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `update_datetime`       TIMESTAMP,
    PRIMARY KEY(`id`)
);

CREATE TABLE IF NOT EXISTS `comment` (
    `id`                    INT(11) NOT NULL AUTO_INCREMENT,
    `user_id`               INT(11),
    `text`                  VARCHAR(1000),
    `create_datetime`       TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    `update_datetime`       TIMESTAMP,
    PRIMARY KEY(`id`),
    CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `cpg`.`user` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `user_recipe` (
    `user_id`               INT(11) NOT NULL,
    `recipe_id`             INT(11) NOT NULL,
    CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `cpg`.`user` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (`recipe_id`) REFERENCES `cpg`.`recipe` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `user_follower` (
    `user_id`               INT(11) NOT NULL,
    `follower_id`           INT(11) NOT NULL,
    CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `cpg`.`user` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT FOREIGN KEY (`follower_id`) REFERENCES `cpg`.`user` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `session` (
    `id`                    INT(11) NOT NULL AUTO_INCREMENT,
    `user_id`               INT(11) NOT NULL,
    `token`                 VARCHAR(100) NOT NULL,
    `last_call_datetime`    TIMESTAMP,
    PRIMARY KEY(`id`,`user_id`,`token`),
    CONSTRAINT FOREIGN KEY (`user_id`) REFERENCES `cpg`.`user` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);
"""