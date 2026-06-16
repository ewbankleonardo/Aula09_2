from loguru import logger
from sys import stderr #outputting error messages and logging 
import getpass

system_user = getpass.getuser()

#manipulando a forma que o log vai aparecer 
logger.add (
                sink=stderr, #joga o log pro terminal
                level="INFO",
                format = "{time} {level} {message} {file} " + system_user
            )
logger.add (
                "LogCrit.log",
                level="CRITICAL",
                format = "{time} {level} {message} {file} " + system_user
            )
logger.add (
                "LogCrit.log",
                level="ERROR",
                format = "{time} {level} {message} {file} " + system_user
            )

def somar(x:int,y:int) -> int:
    try:
        soma = x + y
        logger.info(f"Tudo certo {soma}")
        return soma
    except:
        logger.critical("Digite o valor correto")

somar(2,3)
somar(2,"a")