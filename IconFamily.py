import json


class IconFamily:
    def __init__(self, icon_family):
        with open('config.json', 'r', encoding='utf-8') as f:
            self.icons = json.load(f)
        self.icon_family = icon_family

    def get_container_icon(self):
        return self.icons['icon_families'][self.icon_family]['icon_container']

    def get_leaf_icon(self):
        return self.icons['icon_families'][self.icon_family]['icon_leaf']
