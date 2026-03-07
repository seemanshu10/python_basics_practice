from colorama import Fore, Style 

# file path input 
log_filePath = r"D:\PipelineTD\python_basics_practice\#_Sessions\M2_Python Scripting\02_Python Libraries\AP\5_module - colorama\17_Colorcoded Log File Viewer\log.txt"

# open and reading content 
with open(log_filePath, "r") as file_Errors:

    for line in file_Errors:
        line = line.strip()
        #print(line)

        # Split into two parts from : on first instance 
        line_split = line.split(": ", 1)[0]
        #print(line_split)
        # splitting in spaces and returns last item on list 
        if len(line_split) > 1:
            log_level = line_split.split()[-1]
        #print(log_level)
            if log_level == "DEBUG":
                print(Fore.BLUE + Style.BRIGHT + line ,end=" ")
                print(Style.RESET_ALL)

            elif log_level == "INFO":
                print(Fore.GREEN + Style.BRIGHT + line ,end=" ")
                print(Style.RESET_ALL)

            elif log_level == "WARNING":
                print(Fore.YELLOW + Style.BRIGHT + line ,end=" " )
                print(Style.RESET_ALL)

            elif log_level == "ERROR":
                print(Fore.RED + Style.BRIGHT + line ,end=" ")
                print(Style.RESET_ALL)

            elif log_level == "CRITICAL":
                print(Fore.MAGENTA + Style.BRIGHT + line ,end=" ")
                print(Style.RESET_ALL)


        