import os



def list_files_in_directory(directory_path):
    try:
        # Get a list of all filenames in the directory
        filenames = os.listdir(directory_path)
        return filenames
    except OSError:
        print(f"Error: Unable to list files in {directory_path}")
        return []


    


# Replace 'directory_path' with the path to the directory you want to list files from
directory_path = ''
file_names = list_files_in_directory(directory_path)

# print("List of filenames:")
# for name in file_names:
#     print(name)
rawlist = []
for name in file_names:
    rawlist.append(int(name[:3]))
#print(rawlist)
#print(len(rawlist))
counter = 0
n = 1
i = 0
while i < len(rawlist):
    if rawlist[i] == n:
        n += 1
        i += 1
    else:
        print(n)
        counter += 1
        n += 1
print(f"Number of holes is {counter}")