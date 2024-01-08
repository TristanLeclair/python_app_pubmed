import logging
import argparse
from tkinter import Tk, font
import ttkbootstrap as ttk
from src.common.logging_utils import add_logging_args, setup_root_logger
from app.components.ArticleFetcher import ArticleFetcher


global logger


def parse_args():
    parser = argparse.ArgumentParser(description="A python app for my love")

    add_logging_args(parser, default_deep=True)

    args = parser.parse_args()

    return args.log_level, args.deep_logging


class App:
    def __init__(self, master: Tk) -> None:
        self.master = master
        self.links = []

        # self.defaultFont = font.nametofont("TkDefaultFont")
        #
        # self.defaultFont.configure(family="Segoe Script", size=19, weight=font.BOLD)

        self.article_fetcher = ArticleFetcher(self.master)

        self.article_fetcher.pack()


if __name__ == "__main__":
    log_level, deep_logging = parse_args()

    setup_root_logger(logging, log_level, deep_logging)
    logger = logging.getLogger(__name__)

    root = ttk.Window(themename="superhero")
    # Access the default font object
    default_font = font.nametofont("TkDefaultFont")

    # Configure the default font to change its size (and optionally, the font family)
    default_font.configure(size=30, family="Helvetica")

    root.title("Neuro app")
    root.geometry("400x400")

    app = App(root)

    root.mainloop()
