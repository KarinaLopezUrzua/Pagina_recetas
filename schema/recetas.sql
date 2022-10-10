-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema recetas_schema
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `recetas_schema` ;

-- -----------------------------------------------------
-- Schema recetas_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `recetas_schema` DEFAULT CHARACTER SET utf8 ;
USE `recetas_schema` ;

-- -----------------------------------------------------
-- Table `recetas_schema`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recetas_schema`.`usuarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(145) NULL,
  `apellido` VARCHAR(145) NULL,
  `email` VARCHAR(245) NULL,
  `contraseña` VARCHAR(545) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `update_at` DATETIME NULL DEFAULT NOW(),
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `recetas_schema`.`recetas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `recetas_schema`.`recetas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(145) NULL,
  `descripcion` VARCHAR(245) NULL,
  `instrucciones` TEXT NULL,
  `fecha_creacion` DATE NULL,
  `tiempo_preparacion` VARCHAR(45) NULL,
  `created_at` DATETIME NULL DEFAULT NOW(),
  `update_at` DATETIME NULL DEFAULT NOW(),
  `usuario_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_recetas_usuarios_idx` (`usuario_id` ASC) VISIBLE,
  CONSTRAINT `fk_recetas_usuarios`
    FOREIGN KEY (`usuario_id`)
    REFERENCES `recetas_schema`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
