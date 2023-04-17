"""Module software_renderer"""

import sdl2
import sdl2.ext

class SoftwareRenderer(sdl2.ext.SoftwareSpriteRenderSystem):
  """Class SoftwareRenderer"""

  def __init__(self, window):
    super(SoftwareRenderer, self).__init__(window)

  def render(self, components):
    sdl2.ext.fill(self.surface, sdl2.ext.Color(0, 0, 0))
    sdl2.ext.draw.line(self.surface, sdl2.ext.Color(255, 255, 255), (398, 0, 398, 600), width=4)
    super(SoftwareRenderer, self).render(components)
