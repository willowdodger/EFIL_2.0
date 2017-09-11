import os


# create directory
def create_project_dir(directory):  # funkcija sukurti nauja folderi
    if not os.path.exists(directory):  # tikrinama ar egzistuoja folderis
        print("Creating the directory '" + directory + "'")
        os.makedirs(directory)  # sukuriamas folderis


# directory = "test"
# create_project_dir("projectFolders/" + directory)



# creating files 'queue.txt' and 'crawled.txt'
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, "queue.txt")  # join project name ir file name, complete file path
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(queue):  # tikrina ar failas egzistuoja
        write_file(queue, base_url)  # irasom faila
    if not os.path.isfile(crawled):
        write_file(crawled, "")  # blank data, nes pradzioje nebus nieko tik base url - queue url


# write to file
def write_file(pathOfFile, dataToStoreToFile):
    with open(pathOfFile, "w") as f:  # atidaromas konkretus failas su 'write' as f
        f.write(dataToStoreToFile)  # irasoma info i faila


# adding to file
def append_to_file(pathOfFile, dataToStoreToFile):
    with open(pathOfFile, 'a') as f:
        f.write(dataToStoreToFile, '\n')  # write to file and create new line


# remowing from file content
def delete_file_contents(pathOfFile):
    open(pathOfFile, "w").close()  # deleting files content


# put data to set
def file_to_set(file_name):
    results = set()  # create results set
    with open(file_name, "rt") as f:  # open file
        for line in f:  # for each line
            results.add(line.replace("\n", ""))  # replace new line with blank space and write data
    return results


# copy back content to file
def set_to_file(links, file_name):
    with open(file_name, "w") as f:
        for line in sorted(links):  # sorted links
            f.write(line + "\n")
