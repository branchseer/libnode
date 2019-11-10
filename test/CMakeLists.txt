cmake_minimum_required(VERSION 3.12)

project(libnode_test)

set(LIBNODE_DIR ${PROJECT_SOURCE_DIR}/../release)
set(LIBNODE_INCLUDE ${LIBNODE_DIR}/include)
file(GLOB LIBNODE_LIBS ${LIBNODE_DIR}/lib/*)

add_executable(libnode_test main.cc)
target_link_libraries(libnode_test ${LIBNODE_LIBS})
target_include_directories(libnode_test PRIVATE ${LIBNODE_INCLUDE})
