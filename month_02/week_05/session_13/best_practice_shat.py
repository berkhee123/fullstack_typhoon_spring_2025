# large file
with open('large_file.html', 'r') as file:
    chunk_size = 1024  # zovhon usegnii hemjee shuu 
    while True:
        chunk = file.read(chunk_size)
        print(chunk)
        if not chunk:
            break