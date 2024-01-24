import os
import sys
import logging

##Logging file is created here, so that it can be directly accessed form src without going into any folders

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

##Build a Logging directory
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

##Configure your Loggings
logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        ##StreamHandler helps you print your log in the terminal
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")