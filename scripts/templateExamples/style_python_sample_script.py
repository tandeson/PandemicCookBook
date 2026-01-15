#!/usr/bin/env python
#*****************************************************************************
#
"""
    What does this do?
"""
#
#*****************************************************************************
#   Use of the software source code and warranty disclaimers are
#   identified in the Software Agreement associated herewith.
#*****************************************************************************

#*  Imports ******************************************************************

import os
import subprocess
import time
import sys
import errno

#*  Constants ****************************************************************

# Exit codes - "no error" must be 0
EXIT_OK, EXIT_ERR, EXIT_CTRL_C = range(3)

#=============================================================================
def main(argv=None):
    """
    Parse arguments, report start & stop time, and run the test.
    """
    
    # Handle command line arguments
    if argv is None:
        argv = sys.argv

    args = parseCommandLine( argv[1:] )

    try:
        print "Start date & time is " + time.strftime("%c")

        # Do the work
        mainControl(args)

    except KeyboardInterrupt:
        # Assume Control-C is intentional, and just exit w/o alerts
        return EXIT_CTRL_C

    print "End date & time is " + time.strftime("%c")
    return EXIT_OK


#=============================================================================
def parseCommandLine(args = sys.argv[1:]):
    """
    Parse command-line options. Returns arguments.

    """

    ## Documentation: https://docs.python.org/2/howto/argparse.html
    import argparse

    ## Parse Input Options.
    parser = argparse.ArgumentParser(description='Sample program')
    
    ## -- Common Options
    parser.add_argument(
        '-f','--file',
        action='store', default="foo.txt",
        help = "Any file.")

    parser.add_argument(
        '-v','--verbose',
        action='store_true',
        help = "Verbose progress messages. Progress messages are "
                "not displayed by default except for system error messages.")
    
    ## Parse the options
    args = parser.parse_args()

    return (args)

#=============================================================================
def mainControl(args):
    """
    Main routine for script.

    <<<Description of the work done.>>>
    """

    # Sample of getting an environment variable including setting a
    # default.
    foo_dir = os.getenv("FOO", "default_FOO_directory")

    # Sample of handling errors.
    if not os.path.isdir(foo_dir):
        sys.stderr.write("Directory '%s' does not exist.\n" % foo_dir)
        sys.exit(1)

    # Sample of using arguments.
    if args.verbose:
        print args.file

    # Sample of invoking an os command.
    command = "ls %s" % os.path.join(foo_dir, args.file)
    if not execCommand(command):
        return False

    return True


#=============================================================================
def execCommand(command):
    """
    Executes a command. Returns True if successful, False otherwise.

    (Part of the code borrowed from Bradey's build daemon code.)
    """

    # Run command
    process = subprocess.Popen(
        command,
        shell = True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        close_fds=True
        )

    # Get output
    commandLog = process.stdout.read()
    process.stdout.close()
    process.stdin.close()

    # Can print debug output if needed.

    # Get exit code
    exitstatus = process.wait()
    if 0 == exitstatus:
        return True
    else:
        sys.stderr.write(
            "Failure: '%s' exited with status: %d\n" % (command, exitstatus))
        return False


#*  Main Code Path ***********************************************************

if __name__ == "__main__":
    # Exit code is main() return value
    # (see http://www.artima.com/weblogs/viewpost.jsp?thread=4829)
    sys.exit(main())


#*****************************************************************************
#*****************************************************************************
