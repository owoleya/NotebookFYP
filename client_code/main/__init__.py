from ._anvil_designer import mainTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..note import note
from ..NoteListPage import NoteListPage

class main(mainTemplate):
  
  def __init__(self, **properties):
    
    self.init_components(**properties)
    
    self.content.add_component(NoteListPage())
    self.repeating_panel_1.items = app_tables.notes.search(tables.order_by('created_date', ascending=False))[:3]
    #app_tables.stufftest.add_row(label='name', content='lame')

  def searchbox_pressed_enter(self, **event_args):
    if (len(app_tables.notes.search(label=self.searchbox.text))!=0):
      self.repeating_panel_2.items = app_tables.notes.search(label=self.searchbox.text)
    else:
      notfound = [{"label":"Note cannot be found"}]
      self.repeating_panel_2.items = notfound
    pass

  def addnote_click(self, **event_args):
    index=1
    while True:
      name=f"Note {index}"
      if (len(app_tables.notes.search(label=str(name)))>0):
          index+=1
      else:
          break

    main=get_open_form()
    newnote=anvil.server.call('add_note', str(name))
    main.content.clear()
    main.content.add_component(note(item=newnote))
    pass

  def home_click(self, **event_args):
    open_form('main')
    pass

























