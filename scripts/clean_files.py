import os
# from PIL import Image
# import PIL

prefix = "tf_files/"
directory = prefix + "conditions"
condition_directories = [
    prefix + "conditions/impetigo/",
    prefix + "conditions/allergic_dermatitis/",
    prefix + "conditions/ringworm/",
    prefix + "conditions/folliculitis/",
    prefix + "conditions/yeast_infection/",
]


def filename_replacer(filename):
    """
    Remove the extra dots from the file name
    """
    fname, fext = os.path.splitext(filename)
    new_filename = fname.replace(".", "_") + fext
    return clean_file_extensions(new_filename)


def clean_filenames(filename, directory):
    old_name = os.path.join(directory, filename)
    new_name = directory + filename_replacer(filename)
    if old_name != new_name:
        print(f"{old_name} -> {new_name}")
        os.rename(old_name, new_name)


def clean_file_extensions(filename):
    """
    For solving the error: Unknown image file format. One of JPEG, PNG, GIF, BMP required.
    """
    return filename
    # return filename.replace("jpg", "jpeg")

    # if '.webp' in filename:
    #     image = Image.open('new-format-image-from-png.webp')
    #     image = image.convert('RGB')
    #     image.save('converting-from-webp-to-png-format.png', 'png')



"""
Iterate over the directories to replace all the file names
"""
for directory in condition_directories:
    for filename in os.listdir(directory):
        clean_filenames(filename, directory)

