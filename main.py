"""
    General Main Flow:
    1. Wait for user decision
    2. When yes start a program
    3. Ask about creating new DB or using already existed
    4. Depend on previous step do:
        4.1. If new - create choosed file format (here only Image or txt file)
        4.2. If upload - show the whole db and let user choose one
        4.3. If not new and not upload - Wait until user take decision
    5. When choose - First random computer step:
        5.1. If new - show process, take two random numbers and make the random decision point
        5.2. If upload - show uploading process, take two random numbers and make the random decision point
    6. Depends on random number:
        6.1. Black hole - ask user if he want additional iteration
        6.2. Go further - make some changes
    7. If 6.2. in the 6 point:

"""
# Import
import os
import numpy as np
import sys
from PIL import Image, ImageFilter
import PIL
import random

# System paths
database_path = './database'

# System lists - available over system.
database_list = [f for f in os.listdir(database_path)]
info = "You have to choose something ..."


def rand_numpy(x, y, unit="pixel") -> type(np.array):
    """
    Example of use:
    rand_numpy(1456, 3456) - return image with size 1456 pixels x 3456 pixels.
    rand_numpy(1456, 3456, unit="cm") - return image with size 1456 cm x 3456 cm.
    :param x: number of columns, number of vertical pixels.
    :param y: number of rows, number of horizontal pixels.
    :param unit: unit specifier: if contain c - recalculate centimeters for pixels.
    :return: random numpy array with declared size.
    TODO:
        1. Maybe change the defined param to the *args keywords list?
    """
    if "c" in unit:
        x = x * 115
        y = y * 115
        return np.np.random.rand(x, y)
    else:
        return np.random.rand(x, y)


def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    else:
        return a


def format__1(digits, num):
    if digits < len(str(num)):
        raise Exception("digits<len(str(num))")
    return ' ' * (digits - len(str(num))) + str(num)


def printmat(arr, row_labels=[], col_labels=[]):
    # print a 2d numpy array (maybe) or nested list
    # the maximum number of chars required to display any item in list
    arr = np.around(arr, decimals=2)
    flatten_list = lambda t: [item for sublist in t for item in sublist]
    max_chars = max([len(str(item)) for item in flatten_list(arr) + col_labels])
    if row_labels == [] and col_labels == []:
        for row in arr:
            print('[%s]' % (' '.join(format__1(max_chars, i) for i in row)))
    elif row_labels != [] and col_labels != []:
        rw = max([len(str(item)) for item in row_labels])  # max char width of row__labels
        print('%s %s' % (' ' * (rw + 1), ' '.join(format__1(max_chars, i) for i in col_labels)))
        for row_label, row in zip(row_labels, arr):
            print('%s [%s]' % (format__1(rw, row_label), ' '.join(format__1(max_chars, i) for i in row)))
    else:
        raise Exception(
            "This case is not implemented...either both row_labels and col_labels must be given or neither.")


def print_numpy(np_arr, *args):
    """

    :param np_arr:
    :param args:
    :return:
    TODO:
        Solve problems with printing. Right now the problem is connected with too many values in
        one row. Should be cut to the values defined by the user. Thing about it tomorrow
    """
    shape = np_arr.shape
    if not args:
        max_x = 7
        max_y = 10
    else:
        max_x = args[0]
        max_y = args[1]

    if len(shape) > 3:
        print("Image Size Error! I cannot have more than 3 dimensions")
    else:
        # Calculate the shape, depends on the size defined by the user.
        y, x = shape[0], shape[1]
        nwd_res = nwd(max(x, y), min(x, y))  # Find NWD of two size
        y, x = int(y / nwd_res), int(x / nwd_res)  # Find this int
        print(y, x)  # Optional - must be deleted
        # more options ...
        if y > max_y and x > max_x:
            x = max_y
            temp = y % max_x
            temp = y - temp
            y = (y - temp) / x + 1

        elif y > max_y and x <= max_x:
            y = 30

        elif y <= max_y and x > max_x:
            x = 30

        col_labels = list(range(1, x + 1))
        row_labels = list(range(1, y + 1))
        printmat(np_arr, row_labels=row_labels, col_labels=col_labels)


def description():
    print("To implement ...")
    pass


def db_print(db_list):
    """
    db_print(list) - database printing
    :param db_list: listed files from database directory
    :return:
    """
    print("Available database:")
    for i, elem in enumerate(db_list):
        print(f"{i + 1}: {os.path.basename(elem)}")


def db_len(**kwargs) -> int:
    if not kwargs:
        print("Which database? You didn't specified")
    else:
        for key, val in kwargs.items():
            if key == "path":
                db_list = [f for f in os.listdir(val)]
                return len(db_list)
            elif key == "list":
                return len(val)


def print_database(**kwargs) -> bool:
    """
    print_database(path=<path>, list=<list>)
    :param kwargs: path and list, determine from where database should read. From path or from listed directory.
    :return: print database
    """
    if not kwargs:
        print("Database has not been specified ...")
        return False
    else:
        for key, val in kwargs.items():
            if key == "path":
                db_list = [f for f in os.listdir(val)]  # probably don't need
                db_print(db_list)
                del db_list
            elif key == "list":
                db_print(val)
            else:
                print("Key Error! I think that I don't understand. I don't know this key")

        return True


def switch_case(choose, db_list) -> str:
    for i in range(1, len(db_list)):
        if i == choose:
            return db_list[i - 1]


def get_image_size():
    print("Please specify the image size in format:\ncolumns, rows (if pixels)\nwidth, height (if centimeters)\n")
    size = str(input("Size: ")).split(',')
    size = [int(i) for i in size]
    return size


if __name__ == "__main__":
    # Print description of program ...
    description()
    while True:
        # Main loop of the program, provide working infinitely
        end_cmd = 'close'
        init = str("")
        print("Would you like to start?\n1-yes\n2-no")
        while init != "1":
            end_cmd
            # Wait until the user decide to start
            init = str(input("Your decision ... "))
            if init.casefold() == "1":
                print("Let's start ...")
            elif init.casefold() == end_cmd:
                sys.exit()
            else:
                print("I am still waiting")
        del init

        print("What want to do?\n1-New File\n2-Upload File?")
        # Using already created file or generate new one?
        decision = str("")
        is_done = False
        while not is_done:
            # Loop - the decision must be taken
            decision = str(input("So? ..."))
            if decision.casefold() == "1":
                # Decision: Create new file
                is_done_inside = False
                while not is_done_inside:
                    # Loop - the inside decision about file must be taken
                    print("What format you expect?\n1-Image\n2-text")
                    file_format = str(input())
                    if file_format.casefold() == "1":
                        # If image - create the new image file, generate random numpy array
                        # converted later to the image.
                        # TODO:
                        #   1. Make program save. Right now user can give more than three size.
                        x, y = get_image_size()
                        raw_img = rand_numpy(x, y)
                        print_numpy(raw_img)
                        is_done_inside = True
                        del file_format
                        break
                    elif file_format.casefold() == "2":
                        # If test - create the new text file, generate random string
                        # saving then as txt file in the database.
                        raw_text = "fdfdggg"  # to implement - generating random string
                        is_done_inside = True
                        del file_format
                        break
                    else:
                        print(info)
                del is_done_inside
                print("File created ...")
                is_done = True
            elif decision.casefold() == "2":
                is_done_inside = False
                print_database(path=database_path)
                db_list = [f for f in os.listdir(database_path)]  # Temporary - must be changed
                while not is_done_inside:
                    # Choose file from database ...
                    f_number = int(input("Give the number of file: "))
                    choose = switch_case(f_number, db_list)
                    print("chosen", choose)
                    im_orgin = Image.open(database_path + "/" + choose)
                    im_copy = im_orgin.copy()

                    print("Image size: " + str(im_orgin.size[0]))


                    def random_tile():
                        # columns = 10
                        # rows = 8

                        columns = random.randint(3, 20)
                        rows = random.randint(3, 20)

                        tile_w = int(im_orgin.size[0] / columns)
                        tile_h = int(im_orgin.size[1] / rows)

                        start_x = random.randint(0, columns-1)
                        start_y = random.randint(0, rows-1)
                        paste_x = random.randint(0, columns-1)
                        paste_y = random.randint(0, rows-1)
                        region = im_orgin.crop((start_x * tile_w, start_y * tile_h, (start_x + 1) * tile_w, (start_y + 1) * tile_h))
                        print("Columns: " + str(columns) + ", Rows: " + str(rows))
                        print("crop size: " + str(start_x * tile_w) + " " + str(start_y * tile_h) + " " + str((start_x + 1) * tile_w) + " " + str((start_y + 1) * tile_h))
                        im_copy.paste(region, (paste_x * tile_w, paste_y * tile_h, (paste_x + 1) * tile_w, (paste_y + 1) * tile_h))
                        return im_copy

                    # left, upper, right, lower

                    # cycle_number = 50
                    cycle_number = random.randint(5, 50)
                    print("REPEAT COPYING: " + str(cycle_number) + " times")

                    for i in range(0, cycle_number):
                        im_copy = random_tile()

                    im_copy = im_copy.save(database_path + "/results/" + choose)

                    is_done = True
            else:
                print(info)
                is_done = False

        del decision

        print("Temporary end")  # Temporary part of code, determining that we finished properly
