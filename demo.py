from us_visa.logger import logging
from us_visa.exception import USVisaException
import sys

try:
    logging.info("Entering try block")
    result = 1/"0"
except Exception as e:
    logging.error(USVisaException(e,sys))


