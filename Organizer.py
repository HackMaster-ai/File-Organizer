import os
import shutil

directory = input("Enter the path of your folder : ")
# if directory.startswith('/') and directory.endswith('/'):
#     if not os.path.exists(directory):
#         raise ValueError("Please make sure the path exists")
# else:
#     raise ValueError("Please make sure the path is written correctly")

if not os.path.isdir(directory):
    raise ValueError("Please check that the directory exists")

fileExtensions = {
  "Documents": ["doc", "docx", "odt", "pdf", "ppt", "pptx", "xls", "xlsx", "txt"],
  "Images": ["ai", "bmp", "gif", "ico", "jpeg", "jpg", "png", "psd", "svg", "tiff"],
  "Audio": ["mp3", "wav", "wma", "flac", "aac"],
  "Video": ["avi", "mp4", "mkv", "wmv", "mov", "flv"],
  "Compressed Files": ["zip", "rar", "7z", "gz", "bzip2"],
  "Executable Files": ["exe", "dmg", "apk", "bat", "sh"],
  "Web Files": ["html", "css", "js"],
  "Data Files": ["csv", "json", "xml"],
  "Code Files": ["py", "java", "cpp", "js", "cs"]
}

contentDirectory = os.listdir(directory)
contentDirectoryCleaned = []

recognized = []
unrecognized = []

#cleaning from the parasit directories
for item in contentDirectory:
    if os.path.isfile(directory + f'{item}'):
        contentDirectoryCleaned.append(item)

#filtering the recognized files
for category, extensions in fileExtensions.items():
    for file in contentDirectoryCleaned:
        fileSplit = file.split('.')
        if fileSplit[1] in extensions:
            recognized.append(file)

for file in contentDirectoryCleaned:
    if file not in recognized:
        unrecognized.append(file)


#Creating the directories for the recognized file
for category, extensions in fileExtensions.items():
    for file in recognized:
        fileSplit = file.split('.')
        if fileSplit[1] in extensions:
            dir_path = directory + category
            src_path = directory + file
            dist_path = directory + category + '/' + file
            if not os.path.isdir(dir_path):
                os.makedirs(dir_path)
            shutil.move(src_path, dist_path)

#Creating the directories for the unrecognized file
for file in unrecognized:
    dir_path = directory + 'Others'
    src_path = directory + file
    dist_path = directory + 'Others/' + file 
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    shutil.move(src_path, dist_path)
    
# bug and problems in some files we don't know why try to debug tomorrow