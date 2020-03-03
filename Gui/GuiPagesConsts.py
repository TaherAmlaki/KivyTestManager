from enum import Enum


class PageNames(Enum):
    BACKGROUND = "background"
    HOME_PAGE = "HomePage"
    CONFIGURATION = "Configuration"

    @property
    def name(self):
        return self.value


class ButtonColor(Enum):
    NORMAL = [0, 0.5, 1.0, 1]
