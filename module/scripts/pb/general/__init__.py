import sys
import logging

logger = logging.getLogger(__file__)


def reload_pb_tools():
    """Remove all mop modules from the Python session.

    Use this command to reload the `mop` package after
    a change was made.
    """
    search = ["pb"]

    mop_modules = []
    for module in sys.modules:
        for term in search:
            if term in module:
                mop_modules.append(module)
                break

    for module in mop_modules:
        del (sys.modules[module])

    logger.info("Reloaded Project Borealis tools.")
