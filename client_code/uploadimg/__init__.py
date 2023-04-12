from ._anvil_designer import uploadimgTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class uploadimg(uploadimgTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def file_loader_1_change(self, file, **event_args):
    parse=file
    readhand = ((anvil.server.call('text',parse)))
    self.text_box_1.text = self.text_box_1.text + readhand
    self.item['imglabel'] = self.text_box_1.text
    self.item['imgcontent'] = parse
    self.image_1.source=parse
    pass