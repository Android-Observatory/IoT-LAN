import argparse
from utils import Nmap
from sys import exc_info
import datetime

NOTIMEOUT = 0
LOGPRETTY = 1
SUCCESS = 0


def sysexcinfo():
    """"Return the systems's exception."""
    return f"{exc_info()[0].__name__}:{exc_info()[1]}"


def setstatus(passed=True, reason=None):
    """Set the Test result status.

    :param passed: True or False
    :param reason: Reason for failure if any
    :return:
    """
    passed = passed
    reason = reason

def exception():
    """Set passed to False and reason to the exception message.

    Returns:
        Nothing
    """
    passed = False
    reason = "Exception caught: [{}]".format(sysexcinfo())


if __name__ == "__main__":
    argparser = argparse.ArgumentParser()
    argparser.add_argument(
            "-a",
            "--args",
            required=True,
            help="Nmap command line arguments",
        )
    argparser.add_argument(
            "-t",
            "--timeout",
            type=int,
            default=NOTIMEOUT,
            help=f"Timeout for nmap command. Default is {NOTIMEOUT} secs, "
                 f"which means no timeout",)

    args = argparser.parse_args()

    nmp = Nmap()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"nmap_scan_{args.args.replace(' ', '_')}_{timestamp}.csv"

    out, err = nmp.run_xmltodict_output(
        args.args,
        timeout=args.timeout or None,
        csv_file=filename
    )
    # print(out)
    print('ERROR: '.format(err))
    
    # try:
    #     nmp = Nmap()
    #     out, err = nmp.run_xmltodict_output(
    #         args,
    #         timeout=None
    #     )
    #     print(out)
    #     print(err)
    #     if err:
    #         setstatus(passed=False, reason=err)
    #     else:
    #         print(**out)
    #         # self.output_handler(**out)
    # except:  # noqa: E722
    #     exception()

