# Makefile for python packages
#
# Author: deployr

PROJECT_NAME := $(shell python setup.py --name)
PROJECT_VERSION := $(shell python setup.py --version)

default:
        @echo "Usage:"
	@echo "make workstation-up inicia el entorno"
	@echo "make workstation-down apaga el entorno"

workstation-up:
	@echo 'Preparando entorno de trabajo'
	python3 docker/make-docker.py
	python3 docker/start-docker.py

workstation-down:
	@echo 'Apagando entorno de trabajo'
	sudo docker stop workstation-cont
	sudo docker rm workstation-cont
