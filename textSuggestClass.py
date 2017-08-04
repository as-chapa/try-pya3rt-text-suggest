# -*- coding: utf-8 -*-
import pya3rt
APIKEY = "{Your APIKEY}"
previous_description = 'テスト'
style = 0 # 現代文
separation = 2 # センテンス

class textSuggestClass():
    def __init__(self):
        self.api = pya3rt.TextSuggestClient(APIKEY)

    def suggest(self,v_previous_description,v_style,v_separation):
        previous_description = v_previous_description
        style = v_style
        separation = v_separation
        return self.api.text_suggest(previous_description=previous_description,style=style,separation=separation)["suggestion"][0]

    def outText(self,v_previous_description,v_style,v_separation):
        return (v_previous_description + self.suggest(v_previous_description,v_style,v_separation))