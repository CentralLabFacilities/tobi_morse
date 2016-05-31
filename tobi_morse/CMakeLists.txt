### Maintainer: flier[@techfak.uni-bielefeld.de] ###

cmake_minimum_required(VERSION 2.8)
PROJECT(tobi-morse)
SET(CMAKE_BUILD_TYPE distribution)

MESSAGE("-- You are building on: ${CMAKE_SYSTEM_NAME}")
MESSAGE("-- If you don't set -DCMAKE_INSTALL_PREFIX defaults are used.")

SET(PREFIX "/usr/local")
IF (CMAKE_INSTALL_PREFIX)
    SET(PREFIX ${CMAKE_INSTALL_PREFIX})
    MESSAGE("-- Found install PREFIX: " ${PREFIX})
ENDIF()

### Glob, then install the files ###
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/scripts/morse_cam_2_rsb.py" DESTINATION ${PREFIX}/bin/)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/models/human_rig.blend" DESTINATION ${PREFIX}/share/morse/data/robots)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/models/patrolbot.blend" DESTINATION ${PREFIX}/share/morse/data/robots)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/models/test.blend" DESTINATION ${PREFIX}/share/morse/data/environments)
INSTALL(PROGRAMS "${CMAKE_CURRENT_SOURCE_DIR}/default.py" DESTINATION ${PREFIX}/share/tobi_morse)
