from ._anvil_designer import StickyNotesTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class StickyNotes(StickyNotesTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run before the form opens.
  
  def button_1_click(self, **event_args):
    if confirm("Are you sure you want to delete this note?"):   
      main = self.parent.parent.parent.item['label']
      anvil.server.call('delImage',main,self.item)
      self.item.delete()
      self.remove_from_parent()
    pass




