#!/usr/bin/env python3
from dataclasses import asdict
import subprocess
import options as Options

class Gum:
    def __format_options(options):
        result = " ".join(['--{}={}'.format(key, value) for key, value in asdict(options).items() if value is not None])
        result = result.replace("_", "-")
        return result

    def __gum(gum_command, arguments = None, options = None, raw_result = False, stdin = None):
        command = ["gum", gum_command]

        if arguments is not None:
            if not isinstance(arguments, list):
                arguments = [arguments]
            
            command = command + arguments

        if options is not None:
            command = command + Gum.__format_options(options).split()

        result = subprocess.run(command, stdout=subprocess.PIPE, text=True, stdin=stdin)

        if raw_result:
            return result
        else:
            return result.stdout.strip()

    def choose(choices: list, options: Options.ChooseOptions = None):
        result = Gum.__gum("choose", arguments=choices, options=options)
        return result
    
    def confirm(options: Options.ConfirmOptions = None):
        result = Gum.__gum("confirm", options=options, raw_result=True)
        return result.returncode

    def file(path: str = None, options: Options.FileOptions = None):
        result = Gum.__gum("file", arguments=path, options=options)
        return result
    
    # def filter():
    #     pass
    
    # def format():
    #     pass
    
    def input(options: Options.InputOptions = None):
        result = Gum.__gum("input", options=options)
        return result
    
    # def join():
    #     pass
    
    # def pager():
    #     pass
    
    # def spin():
    #     pass
    
    # def style():
    #     pass
    
    # def table():
    #     pass
    
    # def write():
    #     pass

if __name__ == "__main__":
    print("This is not a script.")
