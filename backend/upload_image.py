# importing os module
import os

from flask import Flask, request, render_template, send_from_directory
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

# Function to rename multiple files
def main():
    i = 0

    # target = os.path.join(APP_ROOT, 'static/img/user_')
    # # target = os.path.join(APP_ROOT, 'static/')
    # print(target)
    # if not os.path.isdir(target):
    #     os.mkdir(target)
    # else:
    #     print("Couldn't create upload directory: {}".format(target))
    # print(request.files.getlist("file"))

    for filename in os.listdir("xyz"):
        dst = str(i) + ".jpg"
        src = 'xyz' + filename
        dst = 'xyz' + dst

        # rename() function will
        # rename all the files
        aa = os.rename(src, dst)
        print(aa)
        i += 1


# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()