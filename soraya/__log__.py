
{'date': 'Fri May 11 2018 08:59:21.60 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''
 module <string> line 152
  INVENTARIO.score(
                                                                                                        ^
SyntaxError: invalid syntax
'''},
{'date': 'Fri May 11 2018 08:59:32.878 GMt-0300 (-03) -X- SuPyGirls -X-',
'error': '''Traceback (most recent call last):
  module _core.main line 125
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 132
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 285
    return self._first_response(dialog, lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 261
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 278
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 174
    Puzzle()
  module <module> line 166
    self.puzzle = Bloco(oce, 4, 4, style=dict(left=10, top=100))
  module <module> line 118
    self.inicia_de_novo()
  module <module> line 121
    INVENTARIO.score(
TypeError: score() got an unexpected keyword argument '_level'
'''},