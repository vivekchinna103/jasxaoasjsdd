

import os
from pathlib import Path
from dotenv import load_dotenv
BASE_DIR= Path(__file__).resolve(strict=True).parent.parent
env_path=os.path.join(BASE_DIR,'env_var_folder/env')

load_dotenv(env_path)
SECRET_PHRASE=os.getenv('DB_USER')
print(SECRET_PHRASE)
