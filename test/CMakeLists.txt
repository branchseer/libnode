cmake_minimum_required(VERSION 3.12)

project(libnode_test)

ADD_SUBDIRECTORY(${PROJECT_SOURCE_DIR}/../release libnode_out)

add_executable(libnode_test main.cc)
target_link_libraries(libnode_test libnode)
