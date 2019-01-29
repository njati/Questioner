"""Entry point to the Application"""

from app.api import APP
import os

if __name__=="__main__":
    APP.run(host=os.getenv('IP', '0.0.0.0'), 
            port=int(os.getenv('PORT', 4444)), debug=True)
