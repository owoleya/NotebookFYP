from ._anvil_designer import SearchTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Search(SearchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def text_box_1_pressed_enter(self, **event_args):
    if (len(app_tables.notes.search(label=self.text_box_1.text))!=0):
      results = len(app_tables.notes.search(label=self.text_box_1.text))
      self.result.text = f"Found {results} notes"
      self.repeating_panel_2.items = app_tables.notes.search(label=self.text_box_1.text)
    else:
      self.result.text = "No notes found"
    pass