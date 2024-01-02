import logging
import webbrowser
import argparse
from tkinter import Frame, Tk, font
from tkinter.ttk import Button, Label
from src.common.logging_utils import add_logging_args, setup_root_logger

from scripts.fetch_neuro_articles import fetch_neuroscience_articles

global logger


def parse_args():
    parser = argparse.ArgumentParser(description="A python app for my love")

    add_logging_args(parser, default_deep=True)

    args = parser.parse_args()

    return args.log_level, args.deep_logging


def update_label(app):
    articles = fetch_neuroscience_articles()

    if articles is None:
        app.articles_header.configure(text="No new articles found!")
        return

    if app.links:
        for link in app.links:
            link.destroy()
        app.links.clear()

    for url in articles:
        link = Label(app.articles_frame, text=url)
        link.pack()
        link.bind("<Button-1>", lambda e: webbrowser.open_new(url))
        app.links.append(link)


class App:
    def __init__(self, master: Tk) -> None:
        self.master = master
        self.links = []

        self.defaultFont = font.nametofont("TkDefaultFont")

        self.defaultFont.configure(family="Segoe Script", size=19, weight=font.BOLD)

        self.articles_frame = Frame(self.master)

        self.articles_header = Label(
            self.master, text="Here are some articles for you to read"
        )

        self.fetch_btn = Button(
            self.master,
            text="Press me",
            command=lambda: update_label(self),
        )
        self.fetch_btn.pack()
        self.articles_frame.pack()


if __name__ == "__main__":
    log_level, deep_logging = parse_args()

    setup_root_logger(logging, log_level, deep_logging)
    logger = logging.getLogger(__name__)

    root = Tk()

    root.title("Neuro app")
    root.geometry("400x400")

    app = App(root)

    root.mainloop()
