from tornado import ioloop, httpserver
from tornado.web import Application, OutputTransform

from controller.produto_controller import Index,Novo,Atualiza,Deleta

class RunApp(Application):
    def __init__(self) -> None:
        handlers = [ #rotas
            ('/',Index),
            ('/produto/novo', Novo),
            (r'/produto/update/(\d+)/status/(\d+)',Atualiza),
            (r'/produto/delete/(\d+)',Deleta)
        ]
        settings = dict(
            debug = True,
            template_path = 'views',
            static_path = 'static',
        )
        Application.__init__(self,handlers,**settings) # type: ignore
        
if __name__ == '__main__':
    httpserver = httpserver.HTTPServer(RunApp())
    httpserver.listen(5000)
    ioloop.IOLoop.instance().start()