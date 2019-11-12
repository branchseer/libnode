cmake_minimum_required(VERSION 3.13)
set(CMAKE_CXX_STANDARD 11)

project(libnode)

set(NODE_DIR ${PROJECT_SOURCE_DIR}/../node-$ENV{LIBNODE_NODE_VERSION})
include_directories(${NODE_DIR}/include/node)

add_library(node_stubs STATIC ${NODE_DIR}/src/node_code_cache_stub.cc  ${NODE_DIR}/src/node_snapshot_stub.cc)
target_compile_definitions(node_stubs PRIVATE NODE_WANT_INTERNALS=1)

add_library(node_start STATIC node_start.cc)

if(WIN32)
	target_compile_options(node_stubs PUBLIC "/MT")
	target_compile_options(node_start PUBLIC "/MT")
elseif(APPLE)
	target_compile_options(node_stubs PRIVATE -mmacosx-version-min=10.10)
	target_compile_options(node_start PRIVATE -mmacosx-version-min=10.10)
endif()
