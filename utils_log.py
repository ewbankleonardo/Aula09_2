from loguru import logger
from sys import stderr #outputting error messages and logging 
import getpass
from functools import wraps


system_user = getpass.getuser()
#logger.add("Logando.log")

logger.add (
                #sink=stderr, #joga o log pro terminal
                "LogInfo.log",
                level="INFO",
                format = "{time} {level} {message} {file} " + system_user
            )



def log_decorator (func):
    @wraps(func) #garante que a func recebida não perca as caracteristicas dela
    def wrapper(*args, **kwargs): #recebe todos os 
        #argumentos e args reservados que a func ta recebendo (todos os parametros que o user passa)
        logger.info(f"Chamando func'{func.__name__}' com args {args} e kwargs {kwargs}") #jogando a info de log desejada
        try:
            result = func(*args,**kwargs) #pega o resultado da funcao com os parametros passados
            logger.info(f"Função '{func.__name__}' retornou {result}")
            return result
        except Exception as e: #se der problema no result, taca essa exceçao 
            logger.exception(f"Exceção capturada em '{func.__name__}': {e} ")
            raise #relança a excecao pra não alterar o funcionamento da func
    return wrapper

