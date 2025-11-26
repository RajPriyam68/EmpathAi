from loguru import logger as _logger
_logger.remove()
_logger.add(lambda msg: print(msg, end='\n'))
def log_event(name, data=None):
    _logger.info({'event': name, 'data': data})
