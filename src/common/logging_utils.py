from argparse import ArgumentParser


def add_logging_args(
    parser: ArgumentParser, default_level="INFO", default_deep=False
) -> ArgumentParser:
    """Add logging arguments to an ArgumentParser.
    Adds the following arguments:
        -l/--log: Set the logging level
        -d/--deep: Show which file is logging
    """

    # add logging level argument
    parser.add_argument(
        "-l",
        "--log",
        dest="log_level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        default=default_level,
        help="Set the logging level",
    )

    # add toggle for deep logging ("shows who is logging")
    parser.add_argument(
        "-d",
        "--deep",
        dest="deep_logging",
        action="store_true",
        help="Show which file is logging",
        default=default_deep,
    )

    return parser


def setup_root_logger(logging, log_level, deep_logging):
    format = f"%(asctime)s - { '%(name)s - ' if deep_logging else ''}%(levelname)s: %(message)s"
    logging.basicConfig(
        level=log_level,
        format=format,
        datefmt="%Y-%m-%d %H:%M:%S",
    )
