from translate.filters.pofilter import cmdlineparser
from translate.filters.checks import StandardChecker

from translate.filters.checks import CheckerConfig

nousconfig = CheckerConfig(
    canchangetags = [("a", "title", None),
                     ("img", "alt", None)]
    )

class NousChecker(StandardChecker):

    def __init__(self, **kwargs):
        checkerconfig = kwargs.get("checkerconfig", None)
        if checkerconfig is None:
            checkerconfig = CheckerConfig()
            kwargs["checkerconfig"] = checkerconfig
        checkerconfig.update(nousconfig)
        StandardChecker.__init__(self, **kwargs)


def main():
    parser = cmdlineparser()
    parser.add_option("", "--nous", dest="filterclass",
        action="store_const", default=None, const=NousChecker,
        help="use the standard checks for Nous translations")

    parser.run()
