from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'AK':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)
                #Add the folder path & also create all the folders

extensions_folders = {
#No name
    'noname' : "C:/Users/HACKER47/Desktop/AK/Other/Uncategorized",
#Audio
    '.aif' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.cda' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.mid' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.midi' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.mp3' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.mpa' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.ogg' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.wav' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.wma' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.wpl' : "C:/Users/HACKER47/Desktop/AK/Audio",
    '.m3u' : "C:/Users/HACKER47/Desktop/AK/Audio",
#Text
    '.txt' : "C:/Users/HACKER47/Desktop/AK/Text/TextFiles",
    '.doc' : "C:/Users/HACKER47/Desktop/AK/Text/Microsoft/Word",
    '.docx' : "C:/Users/HACKER47/Desktop/AK/Text/Microsoft/Word",
    '.odt ' : "C:/Users/HACKER47/Desktop/AK/Text/TextFiles",
    '.pdf': "C:/Users/HACKER47/Desktop/AK/Text/PDF",
    '.rtf': "C:/Users/HACKER47/Desktop/AK/Text/TextFiles",
    '.tex': "C:/Users/HACKER47/Desktop/AK/Text/TextFiles",
    '.wks ': "C:/Users/HACKER47/Desktop/AK/Text/TextFiles",
    '.wps': "C:/Users/HACKER47/Desktop/AK/Text/TextFiles",
    '.wpd': "C:/Users/HACKER47/Desktop/AK/Text/TextFiles",
#Video
    '.3g2': "C:/Users/HACKER47/Desktop/AK/Video",
    '.3gp': "C:/Users/HACKER47/Desktop/AK/Video",
    '.avi': "C:/Users/HACKER47/Desktop/AK/Video",
    '.flv': "C:/Users/HACKER47/Desktop/AK/Video",
    '.h264': "C:/Users/HACKER47/Desktop/AK/Video",
    '.m4v': "C:/Users/HACKER47/Desktop/AK/Video",
    '.mkv': "C:/Users/HACKER47/Desktop/AK/Video",
    '.mov': "C:/Users/HACKER47/Desktop/AK/Video",
    '.mp4': "C:/Users/HACKER47/Desktop/AK/Video",
    '.mpg': "C:/Users/HACKER47/Desktop/AK/Video",
    '.mpeg': "C:/Users/HACKER47/Desktop/AK/Video",
    '.rm': "C:/Users/HACKER47/Desktop/AK/Video",
    '.swf': "C:/Users/HACKER47/Desktop/AK/Video",
    '.vob': "C:/Users/HACKER47/Desktop/AK/Video",
    '.wmv': "C:/Users/HACKER47/Desktop/AK/Video",
#Images
    '.ai': "C:/Users/HACKER47/Desktop/AK/Images",
    '.bmp': "C:/Users/HACKER47/Desktop/AK/Images",
    '.gif': "C:/Users/HACKER47/Desktop/AK/Images",
    '.ico': "C:/Users/HACKER47/Desktop/AK/Images",
    '.jpg': "C:/Users/HACKER47/Desktop/AK/Images",
    '.jpeg': "C:/Users/HACKER47/Desktop/AK/Images",
    '.png': "C:/Users/HACKER47/Desktop/AK/Images",
    '.ps': "C:/Users/HACKER47/Desktop/AK/Images",
    '.psd': "C:/Users/HACKER47/Desktop/AK/Images",
    '.svg': "C:/Users/HACKER47/Desktop/AK/Images",
    '.tif': "C:/Users/HACKER47/Desktop/AK/Images",
    '.tiff': "C:/Users/HACKER47/Desktop/AK/Images",
    '.CR2': "C:/Users/HACKER47/Desktop/AK/Images",
#Internet
    '.asp': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.aspx': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.cer': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.cfm': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.cgi': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.pl': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.css': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.htm': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.js': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.jsp': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.part': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.php': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.rss': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
    '.xhtml': "C:/Users/HACKER47/Desktop/AK/Other/Internet",
#Compressed
    '.7z': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
    '.arj': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
    '.deb': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
    '.pkg': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
    '.rar': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
    '.rpm': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
    '.tar.gz': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
    '.z': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
    '.zip': "C:/Users/HACKER47/Desktop/AK/Other/Compressed",
#Disc
    '.bin': "C:/Users/HACKER47/Desktop/AK/Other/Disc",
    '.dmg': "C:/Users/HACKER47/Desktop/AK/Other/Disc",
    '.iso': "C:/Users/HACKER47/Desktop/AK/Other/Disc",
    '.toast': "C:/Users/HACKER47/Desktop/AK/Other/Disc",
    '.vcd': "C:/Users/HACKER47/Desktop/AK/Other/Disc",
#Data
    '.csv': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.dat': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.db': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.dbf': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.log': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.mdb': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.sav': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.sql': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.tar': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.xml': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
    '.json': "C:/Users/HACKER47/Desktop/AK/Programming/Database",
#Executables
    '.apk': "C:/Users/HACKER47/Desktop/AK/Other/Executables",
    '.bat': "C:/Users/HACKER47/Desktop/AK/Other/Executables",
    '.com': "C:/Users/HACKER47/Desktop/AK/Other/Executables",
    '.exe': "C:/Users/HACKER47/Desktop/AK/Other/Executables",
    '.gadget': "C:/Users/HACKER47/Desktop/AK/Other/Executables",
    '.jar': "C:/Users/HACKER47/Desktop/AK/Other/Executables",
    '.wsf': "C:/Users/HACKER47/Desktop/AK/Other/Executables",
#Fonts
    '.fnt': "C:/Users/HACKER47/Desktop/AK/Other/Fonts",
    '.fon': "C:/Users/HACKER47/Desktop/AK/Other/Fonts",
    '.otf': "C:/Users/HACKER47/Desktop/AK/Other/Fonts",
    '.ttf': "C:/Users/HACKER47/Desktop/AK/Other/Fonts",
#Presentations
    '.key': "C:/Users/HACKER47/Desktop/AK/Text/Presentations",
    '.odp': "C:/Users/HACKER47/Desktop/AK/Text/Presentations",
    '.pps': "C:/Users/HACKER47/Desktop/AK/Text/Presentations",
    '.ppt': "C:/Users/HACKER47/Desktop/AK/Text/Presentations",
    '.pptx': "C:/Users/HACKER47/Desktop/AK/Text/Presentations",
#Programming
    '.c': "C:/Users/HACKER47/Desktop/AK/Programming/C&C++",
    '.class': "C:/Users/HACKER47/Desktop/AK/Programming/Java",
    '.dart': "C:/Users/HACKER47/Desktop/AK/Programming/Dart",
    '.py': "C:/Users/HACKER47/Desktop/AK/Programming/Python",
    '.sh': "C:/Users/HACKER47/Desktop/AK/Programming/Shell",
    '.swift': "C:/Users/HACKER47/Desktop/AK/Programming/Swift",
    '.html': "C:/Users/HACKER47/Desktop/AK/Programming/C&C++",
    '.h': "C:/Users/HACKER47/Desktop/AK/Programming/C&C++",
#Spreadsheets
    '.ods' : "C:/Users/HACKER47/Desktop/AK/Text/Microsoft/Excel",
    '.xlr' : "C:/Users/HACKER47/Desktop/AK/Text/Microsoft/Excel",
    '.xls' : "C:/Users/HACKER47/Desktop/AK/Text/Microsoft/Excel",
    '.xlsx' : "C:/Users/HACKER47/Desktop/AK/Text/Microsoft/Excel",
#System
    '.bak' : "C:/Users/HACKER47/Desktop/AK/System",
    '.cab' : "C:/Users/HACKER47/Desktop/AK/System",
    '.cfg' : "C:/Users/HACKER47/Desktop/AK/System",
    '.cpl' : "C:/Users/HACKER47/Desktop/AK/System",
    '.cur' : "C:/Users/HACKER47/Desktop/AK/System",
    '.dll' : "C:/Users/HACKER47/Desktop/AK/System",
    '.dmp' : "C:/Users/HACKER47/Desktop/AK/System",
    '.drv' : "C:/Users/HACKER47/Desktop/AK/System",
    '.icns' : "C:/Users/HACKER47/Desktop/AK/System",
    '.ico' : "C:/Users/HACKER47/Desktop/AK/System",
    '.ini' : "C:/Users/HACKER47/Desktop/AK/System",
    '.lnk' : "C:/Users/HACKER47/Desktop/AK/System",
    '.msi' : "C:/Users/HACKER47/Desktop/AK/System",
    '.sys' : "C:/Users/HACKER47/Desktop/AK/System",
    '.tmp' : "C:/Users/HACKER47/Desktop/AK/System",
}

folder_to_track = 'C:/Users/HACKER47/Desktop'
folder_destination = 'C:/Users/HACKER47/Desktop/AK'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
