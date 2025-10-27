cmake_minimum_required(VERSION 3.16)
project(counter_cyclonedds C CXX)

set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 17)

find_path(CYCLONEDDS_INCLUDE_DIR dds/dds.h HINTS /usr/local/include /usr/include)
find_library(CYCLONEDDS_LIB NAMES ddsc HINTS /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu)
if (NOT CYCLONEDDS_INCLUDE_DIR OR NOT CYCLONEDDS_LIB)
  message(FATAL_ERROR "Cyclone DDS not found. Pass -DCYCLONEDDS_INCLUDE_DIR=/path -DCYCLONEDDS_LIB=/path/libddsc.so")
endif()

include_directories(${CYCLONEDDS_INCLUDE_DIR})
include_directories(${CMAKE_SOURCE_DIR}/gen_c)

file(GLOB GEN_C_SOURCES "${CMAKE_SOURCE_DIR}/gen_c/*.c")
set_source_files_properties(${GEN_C_SOURCES} PROPERTIES LANGUAGE C)

add_executable(counter_publisher counter_publisher.cpp ${GEN_C_SOURCES})
target_link_libraries(counter_publisher ${CYCLONEDDS_LIB})

add_executable(counter_subscriber counter_subscriber.cpp ${GEN_C_SOURCES})
target_link_libraries(counter_subscriber ${CYCLONEDDS_LIB})
