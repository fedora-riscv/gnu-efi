# Makefile for source rpm: gnu-efi
# $Id$
NAME := gnu-efi
SPECFILE = $(firstword $(wildcard *.spec))

include ../common/Makefile.common
