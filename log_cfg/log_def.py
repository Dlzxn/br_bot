import logging
import logging.config


logger=logging.getLogger(__name__)
def start_log():
    logger.info('log INFO')



def user_new(user, id):
    us_id_sp=[user, id]
    logger.info(us_id_sp)