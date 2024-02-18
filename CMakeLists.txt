# Set the minimum required CMake version
cmake_minimum_required(VERSION 3.10)

# Project name
project(HelloC)

# Add the executable target from source files in the "src" directory
add_executable(hello src/hello.c)

enable_testing()

find_package(Python COMPONENTS Interpreter REQUIRED)

add_test(NAME HelloPythonTests COMMAND ${Python_EXECUTABLE} -m pytest ${CMAKE_CURRENT_SOURCE_DIR} )

# Set environment variables for the test
set_tests_properties(HelloPythonTests PROPERTIES ENVIRONMENT "APP_PATH=$<TARGET_FILE:hello>")
