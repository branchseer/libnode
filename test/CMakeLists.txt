cmake_minimum_required(VERSION 3.13)

project(libnode_test)

add_subdirectory(${PROJECT_SOURCE_DIR}/../libnode libnode_out)

add_executable(libnode_test main.cc)
target_link_libraries(libnode_test libnode)

if(WIN32)
	target_compile_options(libnode_test PRIVATE "/MT")
endif()
