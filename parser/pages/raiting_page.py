import os

from parser.pages.base_page import BasePage


class RatingPage(BasePage):
    """
    Класс для страницы рейтинга фильмов
    """
    def __init__(self, driver):
        super(RatingPage, self).__init__(driver)
        self._FILM_TITLE = "//div[@class='styles_root__ti07r']/div[2]/div/div/a/div[" \
                           "@class='base-movie-main-info_mainInfo__ZL_u3']/span"

    def get_top_five(self):
        titles = [title.text for title in self.find_elements(self._FILM_TITLE)[:5]]
        print(titles)
        return titles
