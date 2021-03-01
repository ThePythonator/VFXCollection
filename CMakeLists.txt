# Basic parameters; check that these match your project / environment
cmake_minimum_required(VERSION 3.8)

project(VFXCollection)
set(PROJECT_SOURCE Point.cpp Point.hpp BezierCurve.cpp BezierCurve.hpp)
set(PROJECT_DISTRIBS LICENSE README.md)

# Build configuration; approach this with caution!
if(MSVC)
  add_compile_options("/W4" "/wd4244" "/wd4324")
else()
  add_compile_options("-Wall" "-Wextra" "-Wdouble-promotion")
endif()

# setup release packages
install (FILES ${PROJECT_DISTRIBS} DESTINATION .)
set (CPACK_INCLUDE_TOPLEVEL_DIRECTORY OFF)
set (CPACK_GENERATOR "ZIP" "TGZ")
include (CPack)
