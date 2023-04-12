from ._anvil_designer import NoteListPageTemplate
from anvil import *
import plotly.graph_objects as go
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

from ..Search import Search
from ..Create import Create

class NoteListPage(NoteListPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.repeating_panel_1.items = app_tables.notes.search(tables.order_by('created_date', ascending=False))
    # Any code you write here will run before the form opens.

  def SearchBT_click(self, **event_args):
    alert(
    content=Search(),
    title="Search Note",
    large=True,
    buttons=[],
    )
    pass

  def CreateBT_click(self, **event_args):
    alert(
    content=Create(),
    title="Create Note",
    large=True,
    buttons=[],
    )
    pass










