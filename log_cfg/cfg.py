import sys
from log_cfg.log_filter import DebugWarningLogFilter, CriticalLogFilter, ErrorLogFilter, InfoFilter
sstart='Бот запущен'

logging_config = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 'default': {
            'format': '#%(levelname)-8s %(name)s:%(funcName)s - %(message)s'
        },
        'formatter_start': {
             'format': f'[%(asctime)s]-<BOT STARTING WORK> ::%(name)s: %(funcName)s - %(message)s'
            # 'format': '[%(asctime)s] #%(levelname)-8s %(filename)s:'
            #           '%(lineno)d - %(name)s:%(funcName)s - {BOT_START_WORK} - %(message)s'
        },
        'formatter_bd':{
            'format': f'[%(asctime)s -<OPEN SQL base> ::%(name)s]'
        }

    },

    'filters': {
        'critical_filter': {
            '()': CriticalLogFilter,
        },
        'error_filter': {
            '()': ErrorLogFilter,
        },
        'debug_warning_filter': {
            '()': DebugWarningLogFilter,
        },
        'info_filter': {
            '()': InfoFilter
        }
    },
    'handlers': {
        'info_h': {
            'class': 'logging.FileHandler',
            'filename': 'files_log/info.log',
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'formatter_start',
            'filters': ['info_filter']
        },
        # 'critical_file': {
        #     'class': 'logging.FileHandler',
        #     'filename': 'files_log/critical.log',
        #     'mode': 'a',
        #     'formatter': 'formatter_start',
        #     'filters': ['critical_filter']
        # },
        'info_bas': {
            'class': 'logging.FileHandler',
            'filename': 'files_log/info.log',
            'mode': 'a',
            'level': 'DEBUG',
            'formatter': 'formatter_bd',
            'filters': ['info_filter']
        }
    },

    'loggers': {
        'log_cfg.log_def': {
            'level': 'INFO',
            'handlers': ['info_h']

        },
    },
    'root': {
        'formatters': 'formatter_start',
        'handlers': ['info_h']
    }
}