import re
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import os
from datetime import datetime, timedelta 
import subprocess
import sys

def install_package(package):
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])

try:
    import win32com.client
    print("win32com is already installed.")
except ImportError:
    print("win32com is not installed. Installing...")
    install_package('pywin32')
    print("win32com has been installed.")


class OutlookWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

    def ask_directory(self):
        selected_directory = filedialog.askdirectory()
        return selected_directory

    def mainloop(self):
        self.root.mainloop()

class Outlook_mange_api:
    def __init__(self) -> None:
        pass
class Outlook:
    def __init__(self, output_directory, api, days_received=1, not_allowed=False):
        self.dir = output_directory
        self.api = api
        self.day_receive = days_received
        self.not_allowed = not_allowed

    def check_variables(self, filename=None):
        if filename is None:
            if self.api != "Mapi":
                self.api = "Mapi"

            self.day_receive = int(input("Please enter the number of how many days: "))
            directory_pattern = r'^[A-Za-z0-9_\-./]+$'

            if re.match(directory_pattern, self.dir):
                outlook_window = OutlookWindow()
                selected_directory = outlook_window.ask_directory()
                self.dir = selected_directory

            if self.not_allowed:
                self.not_allowed = [".png", ".jpg", ".gif", ".ARTask"]

            attributes = {
                'dir': [self.dir],
                'api': [self.api],
                'day_receive': [self.day_receive],
                'not_allowed': [self.not_allowed]
            }

            df = pd.DataFrame.from_dict(attributes)
            return df
        else:
            attributes = pd.read_csv(filename + r".csv", index_col=None)
            return attributes

    def save_attributes(self, filename):
        attributes = vars(self)  # Get the instance's attributes as a dictionary
        df = pd.DataFrame.from_dict(attributes)
        df.to_csv(filename + r".csv", index=False)
    
    


    def download_attachments(Sef,dataframe):
        
        not_allowed_extensions=dataframe.iloc[0,3]
        state=1
        def specificy_extentions(notallowedlist):
            only_download_specific_extensions = input("Please enter the extensions you want to download. If multiple, separate them with commas. Leave empty to exclude the following extensions {}: ".format(notallowedlist))

            if only_download_specific_extensions == '':
      #Default setting
                allowed_extensions= None 
            else:
                allowed_extensions = only_download_specific_extensions.split(",")
            return allowed_extensions
        
        allowed_extentions=specificy_extentions(not_allowed_extensions)
        
        api=dataframe.iloc[0,1]
        output_dir=dataframe.iloc[0,0]
        day_recived=dataframe.iloc[0,2]

        Outlook =win32com.client.Dispatch("Outlook.Application").GetNamespace(api)
        inbox = Outlook.GetDefaultFolder(6)
        received_dt = datetime.now() -timedelta(days=int(day_recived)) 
        received_dt = received_dt.strftime('%d/%m/%Y %H:%M %p')
        messages = inbox.Items
        messages = messages.Restrict("[ReceivedTime] >= '" + received_dt + "'")
        # add in the furture to let the user add file strings to restrict
        try:
            for message in list(messages):
                try:
                    s= message.sender
                    for attachment in message.Attachments:
                            if not allowed_extentions == None:
                                if (any(attachment.FileName.lower().endswith(ext) for ext in allowed_extentions)):
                                    attachment.SaveASFile(os.path.join(output_dir,attachment.FileName))
                                    print(f"attachment {attachment.FileName} from {s} saved")
                            if not (any(attachment.FileName.lower().endswith(ext) for ext in not_allowed_extensions)):
                                attachment.SaveASFile(os.path.join(output_dir,attachment.FileName))

                                print(f"attachment {attachment.FileName} from {s} saved")
                            
                except Exception as e: print("error when saving the attachment:" + str(e)) 
        except Exception as e: print("error when processing emails messages:" + str(e))


    
# Example usage


obj = Outlook("output", "API key", 1, True)
file_path = "attributes.csv"
if not os.path.isfile(file_path):
    file_path= None
data =obj.check_variables()
obj.save_attributes(r"attributes")
obj.download_attachments(data)

