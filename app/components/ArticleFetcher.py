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
        self.links = []
        self.style = Style()
        self.style.configure(
            "primary.TButton", font=("Arial", 10, "bold"), background="blue"
        )
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
            style="primary.TButton",
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
