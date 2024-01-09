import logging
import webbrowser
from tkinter import Tk
from ttkbootstrap import Label, Button, Frame, Style

from scripts.fetch_neuro_articles import fetch_neuroscience_articles

logger = logging.getLogger(__name__)


class ArticleFetcher(Frame):
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.page_num = 1
        self.links = []
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
        )
        self.next_page_btn = Button(
            self.master,
            text="Next page",
            command=self.update_label,
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

    def next_page(self):

    pass
