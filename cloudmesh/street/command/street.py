from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.street.api import Street

class StreetCommand(PluginCommand):

    @command
    def do_street(self, args, arguments):
        """
        ::

          Usage:
                street sign hallo NAME
                street sign detect IMAGE

          This command does some useful things.

          Arguments:
              NAME   name of the sign

          Options:
              -f      specify the file

        """
        print(arguments)

        if arguments.sign and arguments.hallo:

            street = Street()
            street.hello(arguments.NAME)

            return ""

                if arguments.sign and arguments.hallo:

        elif arguments.sign and arguments.hallo:
            
            street = Street()
            output = street.deploy(arguments.IMAGE)
            print (output)
