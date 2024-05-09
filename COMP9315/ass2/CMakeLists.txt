cmake_minimum_required(VERSION 3.28)
project(ass2 C)

set(CMAKE_C_STANDARD 99)

# Add each source file required for the 'ass2' executable
# Assuming 'main.c' is the entry point and includes the main function
# Add all other necessary source files (.c) and headers (.h)
# Note: Adjust the file list according to your project's structure
set(LIB_SOURCES
        query.c
        page.c
        reln.c
        tuple.c
        util.c
        chvec.c
        hash.c
        bits.c
        # Add other source files here
)

add_executable(create create.c ${LIB_SOURCES})
add_executable(dump dump.c ${LIB_SOURCES})
add_executable(insert insert.c ${LIB_SOURCES})
add_executable(select select.c ${LIB_SOURCES})
add_executable(stats stats.c ${LIB_SOURCES})
add_executable(gendata gendata.c ${LIB_SOURCES})

# If your project has specific include directories, you can specify them like this:
# include_directories(directory1 directory2 ...)

# If you link against external libraries, specify them here:
# target_link_libraries(ass2 library1 library2 ...)