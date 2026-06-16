from loguru import logger

logger.add("Logando.log")

logger.debug("Aviso debuggando")
logger.info("Info do processo")
logger.warning("Algo vai parar no futuro")
logger.error("Aconteceu uma falha")
logger.critical("Aconteceu uma falha que abortou a aplicacao")
