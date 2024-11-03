# /utils/logging_config.py

import logging

def setup_logging(log_file_path):
    """
    Setup logging configuration
    :param log_file_path: str
    """
    logging.basicConfig(
        filename=log_file_path, 
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
        )
    logging.info("Logging configured")