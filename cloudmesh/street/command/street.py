from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand


class StreetCommand(PluginCommand):

    @command
    def do_street(self, args, arguments):
        """
        ::

          Usage:
                street -f FILE
                street FILE
                street list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """
        print(arguments)



