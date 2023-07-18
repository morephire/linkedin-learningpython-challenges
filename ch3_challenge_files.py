import os

######### Functions ##############

## Calculate bytesize of files in the given path
## Counts only files and not dirs
def count_bytes(path) -> str:
    file_list = os.listdir(path)
    sum = 0
    for file in file_list:
        # byte_size = os.stat(file).st_size
        if os.path.isfile(file):    
            file_size = os.path.getsize(file)
            sum += file_size
    
    return "Total bytecount:" + str(sum)

## Lists all files in the given path
def list_files(path) -> str:
    file_list = os.listdir(path)
    files = ""
    for file in file_list:
        if os.path.isfile(file):
            files += file + "\n"       
    return files

########## MAIN ################
def main():
    cur_dir = os.getcwd()
    
    try:
        # Create folder
        os.makedirs("results")
    except :
        # If the folder exists it will throw and excpetion but will rewrite the textfile in the finally block
        print("Folder already exists")   
    finally:
        # constructing the path for the file    
        dirpath = os.path.realpath("results")
        filename = "textfile.txt"
        filepath = os.path.join(dirpath,filename)

        # opening and (over)write the file
        with open(filepath, "w") as file:
            file.write(count_bytes(cur_dir) + "\n")
            file.write("File list: \n")
            file.write("------------------- \n")
            file.write(list_files(cur_dir))
            file.close()
        
        
if __name__ == "__main__":
    main()