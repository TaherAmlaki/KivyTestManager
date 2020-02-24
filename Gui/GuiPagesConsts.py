from enum import Enum


class PageNames(Enum):
    BACKGROUND = "background"
    HOME_PAGE = "HomePage"

    @property
    def name(self):
        return self.value
    