import os
import sys

from ayon_core.pipeline import install_host
from ayon_core.lib import Logger

log = Logger.get_logger(__name__)


def main(env):
    import ayon_resolve.api as bmdvr

    # activate resolve from ayon_core
    install_host(bmdvr)

    bmdvr.launch_pype_menu()


if __name__ == "__main__":
    result = main(os.environ)
    sys.exit(not bool(result))
