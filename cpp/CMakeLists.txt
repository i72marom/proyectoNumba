cmake_minimum_required(VERSION 2.6)  # CMake version check
project(practica1)               # Create project

# Add main.cpp file of project root directory as source file
set(SOURCE_FILES 
	src/main.cc 
	src/classTime/classTime.cc
	src/funciones/funciones.cc
	src/determinanteIterativo/determinanteIterativo.cc
	src/determinanteRecursivo/determinanteRecursivo.cc
	src/exponenciacion/exponenciacion.cc
)

# Add executable target with source files listed in SOURCE_FILES variable
add_executable(test ${SOURCE_FILES})
