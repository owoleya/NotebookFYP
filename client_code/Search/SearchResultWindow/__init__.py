from ._anvil_designer import SearchResultWindowTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ...note import note

class SearchResultWindow(SearchResultWindowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    # Any code you write here will run before the form opens.

  def notename_click(self, **event_args):
    main=get_open_form()
    stuffs=anvil.server.call('open_note', self.item['label'])
    main.content.clear()
    main.content.add_component(note(item=stuffs))
    self.raise_event("x-close-alert")
    pass




