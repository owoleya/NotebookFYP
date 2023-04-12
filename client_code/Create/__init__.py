from ._anvil_designer import CreateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..note import note

class Create(CreateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def createbox_pressed_enter(self, **event_args):
    if (len(app_tables.notes.search(label=self.createbox.text))>0):
      self.error.text="Note already exists"
    else:
      main=get_open_form()
      data=anvil.server.call('add_note', self.createbox.text)
      main.content.clear()
      main.content.add_component(note(item=data))
      self.raise_event("x-close-alert")
    pass
