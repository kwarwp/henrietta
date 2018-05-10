XXXX - executa_acao if error else lambda self.error - XXXXXXXX - executa_acao if error else lambda self.error - XXXXTraceback (most recent call last):
  module _core.main line 204
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 132
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 286
    return self._first_response(dialog, lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 261
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 278
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 167
    Puzzle()
  module <module> line 159
    self.puzzle = Bloco(oce, 4, 4, style=dict(left=10, top=100))
  module <module> line 116
    self.inicia_de_novo()
  module <module> line 119
    INVENTARIO.score(casa=self.img, carta=self.dim[0]*100+self.dim[1],
NameError: name 'INVENTARIO' is not defined
XXXX - executa_acao if error else lambda self.error - XXXXTraceback (most recent call last):
  module _core.main line 204
    dialog.action(lambda *_: self.start()
  module _core.supygirls_factory line 132
    self.act(self, lambda *_: self.hide() or extra()) if self.act else None
  module _core.supygirls_factory line 286
    return self._first_response(dialog, lambda: self._executa_acao(), self.extra, self.error)
  module _core.supygirls_factory line 261
    traceback.print_exc(file=sys.stderr)
  module _core.supygirls_factory line 278
    exec(self.code, glob)  # dict(__name__="__main__"))
  module <module> line 167
    Puzzle()
  module <module> line 159
    self.puzzle = Bloco(oce, 4, 4, style=dict(left=10, top=100))
  module <module> line 116
    self.inicia_de_novo()
  module <module> line 119
    INVENTARIO.score(casa=self.img, carta=self.dim[0]*100+self.dim[1],
  module _spy.vitollino.main line 369
    SUPERPYTHON.scorer(data) if SUPYGIRLS else None
NameError: name 'SUPYGIRLS' is not defined
XXXX - executa_acao if error else lambda self.error - XXXX
 module <string> line 120
  move="BLOCO", ponto=self.repete, valor=0)
                                          ^
SyntaxError: invalid syntax
XXXX - executa_acao if error else lambda self.error - XXXX