import logging
import webbrowser
from tkinter import Tk
from ttkbootstrap import Label, Button, Frame

from scripts.fetch_neuro_articles import fetch_neuroscience_articles

logger = logging.getLogger(__name__)


class ArticleFetcher(Frame):
    def __init__(self, master: Tk):
        super().__init__(master)
        self.master = master
        self.page_num = 1
        self.articles_per_page = 5
        self.links = []  # A list of Label objects
        self.displayed_links = []  # A list of article links (for pagination)
        self.articles = []  # A list of article links
        self.articles_frame = Frame(
            self.master,
        )
        self.articles_header = Label(
            self.master, text="Here are some articles for you to read"
        )
        self.fetch_btn = Button(
            self.master,
            text="Fetch articles",
            command=self.update_label,
        )
        self.new_articles_btn = Button(
            self.master,
            text="Get new articles",
            command=self.new_articles,
        )
        self.fetch_btn.pack()
        self.articles_frame.pack()
        self.new_articles_btn.pack()

    def update_label(self):
        logger.info("Fetch articles button pressed")
        if self.need_to_fetch_new_articles():
            articles = fetch_neuroscience_articles()
            if articles is None:
                self.articles_header.configure(text="No new articles found!")
                return
            self.page_num = 1
            # select first page of links
            self.articles = articles.copy()
            self.displayed_links = self.articles[: self.articles_per_page]
        else:
            self.displayed_links = self.articles[
                self.articles_per_page
                * (self.page_num - 1) : self.articles_per_page
                * (self.page_num)
            ]
            self.page_num += 1
        self.display_links()

    def display_links(self):
        if self.links:
            for link in self.links:
                link.destroy()
            self.links.clear()
        for url in self.displayed_links:
            link = Label(self.articles_frame, text=url)
            link.pack()
            link.bind("<Button-1>", lambda _: webbrowser.open_new(url))
            self.links.append(link)

    def need_to_fetch_new_articles(self):
        return (
            len(self.articles) == 0
            or len(self.articles) == self.articles_per_page * self.page_num
        )

    def new_articles(self):
        logger.info("New articles button pressed")

        pass
