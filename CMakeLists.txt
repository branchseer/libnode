cmake_minimum_required(VERSION 3.13)

project(libnode)

file(GLOB LIBNODE_ARCHIVES ${CMAKE_CURRENT_LIST_DIR}/lib/*)
set(LIBNODE_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/include/node)

add_library(libnode STATIC ${CMAKE_CURRENT_LIST_DIR}/dummy.c)

if(UNIX AND NOT APPLE)
    target_link_libraries(libnode INTERFACE "-Wl,--start-group" ${LIBNODE_ARCHIVES} "-Wl,--end-group" "-pthread" "-ldl" "-lrt" "-lm" "-rdynamic")
elseif(WIN32)
	target_link_libraries(libnode INTERFACE ${LIBNODE_ARCHIVES} ws2_32 dbghelp crypt32 winmm iphlpapi psapi userenv)
	if(CMAKE_SIZEOF_VOID_P EQUAL 4)
	# Nodejs is compiled with /SAFESEH:NO with when using MSVC targeting 32bit: https://github.com/nodejs/node/commit/2f477bd34de128683c8d183e759b8f098205b1c9
		target_link_options(libnode INTERFACE "-SAFESEH:NO")
	endif()
else()
	target_link_libraries(libnode INTERFACE ${LIBNODE_ARCHIVES})
	list(JOIN LIBNODE_ARCHIVES " " LIBNODE_PRELINK_FLAGS)
	set_target_properties(libnode PROPERTIES
		XCODE_ATTRIBUTE_OTHER_LIBTOOLFLAGS ${LIBNODE_PRELINK_FLAGS}
	)
endif()

target_include_directories(libnode INTERFACE ${LIBNODE_INCLUDE})
