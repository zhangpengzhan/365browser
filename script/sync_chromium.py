#!/usr/bin/env python
#
# Copyright (c) 2015 The mogoweb project. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import optparse
import os
import sys

import constants

sys.path.append(os.path.join(os.path.dirname(__file__), "dirsync-2.1"))
from dirsync import sync

def sync_java_files(options):
    app_java_dir = os.path.join(constants.DIR_APP_ROOT, "src", "main", "java")
    chrome_java_dir = os.path.join(options.chromium_root, "chrome", "android", "java", "src")
    sync(chrome_java_dir, app_java_dir, "sync")

def sync_jar_files(options):
    app_lib_dir = os.path.join(constants.DIR_APP_ROOT, "libs", "armeabi-v7a")
    chrome_so_lib_dir = os.path.join(options.chromium_root, "out", options.buildtype,
                                       "chrome_public_apk", "libs", "armeabi-v7a")
    args = {'only':['\\.so$']}
    sync(chrome_so_lib_dir, app_lib_dir, "sync", **args)

def sync_so_files(options):
    app_lib_dir = os.path.join(constants.DIR_APP_ROOT, "libs")
    chrome_java_lib_dir = os.path.join(options.chromium_root, "out", options.buildtype, "lib.java")
    args = {'only':['\w+_java\\.jar$', 'cacheinvalidation_javalib\\.jar$', 'jsr_305_javalib\\.jar$',
                'protobuf_nano_javalib\\.jar$']}
    sync(chrome_java_lib_dir, app_lib_dir, "sync", **args)

def sync_chromium_res_files(options):
    library_res_dir = os.path.join(constants.DIR_LIBRARIES_ROOT, "chrome_res", "src", "main", "res")
    chrome_res_dir = os.path.join(options.chromium_root, "chrome", "android", "java", "res")
    sync(chrome_res_dir, library_res_dir, "sync")

    chrome_res_dir = os.path.join(options.chromium_root, "chrome", "android", "java", "res_chromium")
    sync(chrome_res_dir, library_res_dir, "sync")

    # sync chrome generated string resources
    chrome_gen_res_dir = os.path.join(options.chromium_root, "out", options.buildtype,
                                      "gen", "chrome", "java", "res")
    sync(chrome_gen_res_dir, library_res_dir, "sync")

    # sync grd generated string resources
    chrome_grd_res_dir = os.path.join(options.chromium_root, "out", options.buildtype,
                                      "obj", "chrome", "chrome_strings_grd.gen", "chrome_strings_grd", "res_grit")
    library_grd_res_dir = os.path.join(constants.DIR_LIBRARIES_ROOT, "chrome_grd_res", "src", "main", "res")
    sync(chrome_grd_res_dir, library_grd_res_dir, "sync")

def sync_ui_res_files(options):
    library_res_dir = os.path.join(constants.DIR_LIBRARIES_ROOT, "ui_res", "src", "main", "res")
    ui_res_dir = os.path.join(options.chromium_root, "ui", "android", "java", "res")

    sync(ui_res_dir, library_res_dir, "sync")

    # sync grd generated string resources
    ui_grd_res_dir = os.path.join(options.chromium_root, "out", options.buildtype,
                                      "obj", "ui", "android", "ui_strings_grd.gen", "ui_strings_grd", "res_grit")
    args = {'exclude': ['values-\S+'], 'include': ['values-zh-rCN']}
    sync(ui_grd_res_dir, library_res_dir, "sync", **args)

def sync_content_res_files(options):
    library_res_dir = os.path.join(constants.DIR_LIBRARIES_ROOT, "content_res", "src", "main", "res")
    content_res_dir = os.path.join(options.chromium_root, "content", "public", "android", "java", "res")
    sync(content_res_dir, library_res_dir, "sync")

    # sync grd generated string resources
    content_grd_res_dir = os.path.join(options.chromium_root, "out", options.buildtype,
                                  "obj", "content", "content_strings_grd.gen", "content_strings_grd", "res_grit")
    args = {'exclude': ['values-\S+'], 'include': ['values-zh-rCN']}
    sync(content_grd_res_dir, library_res_dir, "sync", **args)

def sync_datausagechart_res_files(options):
    library_res_dir = os.path.join(constants.DIR_LIBRARIES_ROOT, "datausagechart_res", "src", "main", "res")
    datausagechart_res_dir = os.path.join(options.chromium_root, "third_party", "android_data_chart", "java", "res")
    sync(datausagechart_res_dir, library_res_dir, "sync")

def sync_androidmedia_res_files(options):
    library_res_dir = os.path.join(constants.DIR_LIBRARIES_ROOT, "androidmedia_res", "src", "main", "res")
    media_res_dir = os.path.join(options.chromium_root, "third_party", "android_media", "java", "res")
    sync(media_res_dir, library_res_dir, "sync")

def main(argv):
    parser = optparse.OptionParser(usage='Usage: %prog [options]', description=__doc__)
    parser.add_option('--chromium_root',
                      default="/work/chromium/master/chromium-android/src",
                      help="The root of chromium sources")
    parser.add_option('--buildtype',
                      default="Debug",
                      help="build type of chromium build(Debug or Release), default Debug")
    options, args = parser.parse_args(argv)

    if options.buildtype not in ["Debug", "Release"]:
        print("buildtype argument value must be Debug or Release")
        exit(0)

    sync_java_files(options)
    sync_jar_files(options)
    sync_chromium_res_files(options)
    sync_ui_res_files(options)
    sync_content_res_files(options)
    sync_datausagechart_res_files(options)
    sync_androidmedia_res_files(options)

if __name__ == '__main__':
    main(sys.argv)