from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.sign.api import Sign
from cloudmesh.common.default import Default
from cloudmesh.common.console import Console

class SignCommand(PluginCommand):

    @command
    def do_sign(self, args, arguments):
        """::

        Usage:
        sign deploy [--cloud=CLOUD] N
        sign cp IMAGE SERVER
        sign run IMAGE SERVER
        sign hallo NAME
        sign detect IMAGE
        sign spread IMAGESDIR
        sign status
        sign terminate
        sign benchmark PARAMETERS...

        This command does some useful things.

        Arguments:
        NAME   name of the sign
        CLOUD  the anme of the cloud 
        IMAGE  the name of the image
        SERVER  the name of the server to copy the image to

        Options:
        -f      specify the file

        Description:
        sign deploy [--cloud=CLOUD] N
                   
            Deploys on the cloud N servers to run the analysis. The
            cloudmesh cluster command is used tofr that.
                   
        sign run IMAGE SERVER

            Runs the detection on the given image on that server.  We assume
            the image is already on the server, otherwise we get an error

        sign spread IMAGESDIR

            The IMAGESDIR contains all images on your local
            computer.  The spread command will equally distribute
            the images onto the remote servers.  The cluster must
            be deployed befor this command can be
            executed. Server names are automatically determined
            from cloudmesh cluster command.

        Please provide descriptions for the other commands
        for the benchmark command see cloudmesh.cubernetes for easy parser I wrote

        """
        print(arguments)

        if arguments.deploy:

            d = Default()
            cloud = d["global", "cloud"]
            d.close()
            
            cloud = arguments["--cloud"]  or cloud
            if cloud is None or cloud is "None":
                Console.error("no cloud specified. please use cms default cloud=CLOUDNAME")
                return ""

            Console.ok("Deploy {} servers on cloud {}".format(arguments.N, cloud))
            Console.error("Not yet implemented")
            
        elif arguments.hallo:

            sign = Sign()
            sign.hello(arguments.NAME)

            return ""

        elif arguments.cp:
            
            sign = Sign()
            output = sign.cp(arguments.IMAGE, arguments.SERVER)
            print (output)

            return ""

        return ""
