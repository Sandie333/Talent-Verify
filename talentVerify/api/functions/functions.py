
def handle_loaded_file(f):
    with open('api/static/fileupload'+f.name,'wb+') as destination:
        for chunk in f.chuncks():
            destination.write(chunk)