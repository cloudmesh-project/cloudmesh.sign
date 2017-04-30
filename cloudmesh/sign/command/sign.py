from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.sign.api import Sign

class SignCommand(PluginCommand):

    @command
    def do_sign(self, args, arguments):
        """
        ::

          Usage:
                sign hallo NAME
                sign detect IMAGE

          This command does some useful things.

          Arguments:
              NAME   name of the sign

          Options:
              -f      specify the file

        """
        print(arguments)

        if arguments.hallo:

            sign = Sign()
            sign.hello(arguments.NAME)

            return ""


        elif arguments.hallo:
            
            sign = Sign()
            output = sign.deploy(arguments.IMAGE)
            print (output)

            return ""

        return ""
