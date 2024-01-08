import logging
import webbrowser
from tkinter import Tk
from tkinter.ttk import Label, Button, Frame, Style

from scripts.fetch_neuro_articles import fetch_neuroscience_articles

logger = logging.getLogger(__name__)


class ArticleFetcher(Frame):
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.links = []
        self.style = Style(self)
        button_style_name = "My.TButton"
        self.style.configure(button_style_name, background="red", foreground="white")
        self.articles_frame = Frame(
            self.master,
        )
        self.articles_header = Label(
            self.master, text="Here are some articles for you to read"
        )
        self.fetch_btn = Button(
            self.master,
            text="Press me now",
            command=self.update_label,
            style=button_style_name,
        )
        self.fetch_btn.pack()
        self.articles_frame.pack()

    def update_label(self):
        articles = fetch_neuroscience_articles()
        if articles is None:
            self.articles_header.configure(text="No new articles found!")
            return
        if self.links:
            for link in self.links:
                link.destroy()
            self.links.clear()
        for url in articles:
            link = Label(self.articles_frame, text=url)
            link.pack()
            link.bind("<Button-1>", lambda _: webbrowser.open_new(url))
            self.links.append(link)

    pass
