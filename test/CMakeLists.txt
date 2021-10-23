cmake_minimum_required(VERSION 3.13)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_MSVC_RUNTIME_LIBRARY "MultiThreaded$<$<CONFIG:Debug>:Debug>")


project(libnode_test)

add_subdirectory(${PROJECT_SOURCE_DIR}/../libnode libnode_out)

add_executable(simple simple.cc)
target_link_libraries(simple libnode)

add_executable(process_argv process_argv.cc)
target_link_libraries(process_argv libnode)
