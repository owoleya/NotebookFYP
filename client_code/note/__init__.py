from ._anvil_designer import noteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..uploadimg import uploadimg
from ..writetext import writetext

class note(noteTemplate):
  old = None
  table = None
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    
    self.init_components(**properties)
    self.old = self.item['label']
    self.title.text=self.item['label']
    
    self.table = app_tables.notes.get(label=self.item['label'])
    self.repeating_panel_1.items = self.table['imgs']
    # Any code you write here will run before the form opens.
  
  def save_click(self, **event_args):
    if (self.old!=self.item['label']) and (len(app_tables.notes.search(label=self.title.text))>0):
      self.error.text="Note already exists"
    elif (self.title.text == ""):
      self.error.text="Note must have proper title"
    else:
      updated = dict(self.item)
      anvil.server.call('update_note', self.old, updated)
      self.old = self.item['label']
      self.error.text=None
    pass

  def delete_click(self, **event_args):
    if confirm("Are you sure you want to delete this note?"):
      anvil.server.call('delete_note', self.old)
      open_form('main')
    pass


  def pen_click(self, **event_args):
    imageset={}
    
    cfm = alert(
    content=writetext(item=imageset),
    title="Write",
    large=True,
    buttons=[("Upload",True)],
    )
    if cfm:
      anvil.server.call('addImage',self.item['label'],imageset)

      self.repeating_panel_1.items.append([imageset])
      self.repeating_panel_1.items = self.table['imgs']
    pass

  def upload_click(self, **event_args):
    imageset={}
    
    cfm = alert(
    content=uploadimg(item=imageset),
    title="Upload",
    buttons=[("Upload",True)],
    )
    if cfm:
      anvil.server.call('addImage',self.item['label'],imageset)

      self.repeating_panel_1.items.append([imageset])
      self.repeating_panel_1.items = self.table['imgs']
    pass











