from traits.api import HasTraits, Str, Range, Enum
from traitsui.api import View, Item, CodeEditor


class Code(HasTraits):
    code = Str()

code = Code()

code_view = View(
    Item('code', editor=CodeEditor(),),
    buttons=['OK', 'Cancel'],
    resizable=True,
)

code.configure_traits(view=code_view)
