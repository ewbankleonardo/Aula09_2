from loguru import logger
from sys import stderr #outputting error messages and logging 
import getpass
from utils_log import log_decorator

system_user = getpass.getuser()

@log_decorator
def somar(x:int,y:int) -> int:
  #  try:
    soma = x + y
  #      logger.info(f"Tudo certo {soma}")
    return soma
  #  except:
  #      logger.critical("Digite o valor correto")

somar(2,3)
somar(2,"a")