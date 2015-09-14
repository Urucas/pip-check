#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import pip
import os
import sys

def err(msg):
    print "\033[31m✗ \033[0m%s" % msg

def ok(msg):
    print "\033[32m✓ \033[0m%s" % msg

def main():
    cwd = os.getcwd()
    json_file = os.path.join(cwd, 'dependencies.json')
    if os.path.isfile(json_file) == False:
        err("dependencies.json not found in current folder")
        sys.exit(1)

    with open(json_file) as data_file:
        data = json.load(data_file)

    dependencies = data["dependencies"]
    for lib in dependencies:
        command = pip.commands.install.InstallCommand()
        opts, args = command.parser.parse_args()
        requirements_set = command.run(opts, [lib])
        requirements_set.install(opts)

    ok("Successfuly installed mising dependencies")

if __name__ == "__main__":
    main()
