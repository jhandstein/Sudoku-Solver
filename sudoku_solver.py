def main():
    sudoku = [
    [7,4,5,0,0,0,2,0,8],
    [2,0,0,6,8,0,0,0,0],
    [9,0,8,0,0,0,4,3,1],
    [0,0,4,5,0,0,7,8,6],
    [0,3,0,0,0,1,0,0,0],
    [0,0,0,0,2,8,0,1,0],
    [5,7,2,0,0,0,0,0,3],
    [0,0,0,9,0,5,0,0,0],
    [0,9,0,0,0,0,1,0,4]
    ]

    # replaces all zeros with empty dictonaries
    sudoku = zero_to_dict(sudoku)
    counter = 0
    # actual solving of sudoku
    while (True):
        # update dicts for every row
        for line in sudoku:
            for x in line:
                update_dict(line)

        # update dicts for every column
        for i in range(9):
            column = list()
            for idx, _ in enumerate(sudoku):
                column.append(sudoku[idx][i])

            for x in column:
                update_dict(column)

            for idx, _ in enumerate(sudoku):
                sudoku[idx][i] = column[idx]

        # update dicts for every square and map them back
        squares = check_squares(sudoku)
        sudoku = squares_back(squares)

        # full dictionaries (len > 7) are replaced by correct numbers
        sudoku = new_entries(sudoku)
        counter +=1

        # first interruption of the loop if the sudoku is solved
        if get_real_true(sudoku) == False:
            break

        # preventing endless loop if sudoku can't be solved
        if counter >= 1000:
            break

    print(f'Algorithm finished after {counter} iterations.')

    check_sudoku(sudoku)

def zero_to_dict(sudoku):
    for idx, line in enumerate(sudoku):
        for jdx, number in enumerate(sudoku):
            if sudoku[idx][jdx] == 0:
                sudoku[idx][jdx] = {}
    return sudoku

def update_dict(instancelist):
    for instance in instancelist:
        # skip over all value which are set already
        if not isinstance(instance, dict):
            pass

        else:
            for entry in instancelist:
                if isinstance(entry, int):
                    # dict gets all entries, which are already solved in the array
                    instance[entry] = instance.get(entry, False)

def check_squares(sudoku):
    squarelist = list()
    # iterate over the single squares
    for box_x in range(3):
        for box_y in range(3):
            squarex = list()

            # iterate over the actual rows and columns within the square
            for actualrow in range(box_x*3, (box_x+1)*3):
                for value in sudoku[actualrow][box_y*3 : (box_y+1)*3]:
                    squarex.append(value)

            update_dict(squarex)
            squarelist.append(squarex)

    return squarelist

def squares_back(squarelist):
    rows_l = list()

    for box_x in range(3):
        for box_y in range(3):
            truerow = list()

            for placeholder_var in range(box_x*3, (box_x+1)*3):
                for value in squarelist[placeholder_var][box_y*3 : (box_y+1)*3]:
                    truerow.append(value)

            rows_l.append(truerow)
    return rows_l

def new_entries(sudoku):
    for rows in sudoku:
        for eid, entry in enumerate(rows):
            if isinstance(entry, int):
                continue

            if len(entry) == 8:

                for number in range(1,10):
                    entry[number] = entry.get(number, True)

                for key in entry.keys():
                    if entry[key] == True:
                        rows[eid] = key

    return sudoku

def check_sudoku(sudoku):
    print("''"*30)
    for idx, line in enumerate(sudoku):
        print(f'*{idx + 1}*: {line}')
    print("''"*30)

def compare_two(s1, s2):
    for i in range(9):
        for j in range(9):
            if s1[i][j] == s2[i][j]:
                print(f"Row {i+1}/ Column {j+1}: True")

def get_real_true(sudoku):
    still_dicts = False

    # check whether there is a dict with 8 entries
    for lid, line in enumerate(sudoku):
        for nid, number in enumerate(line):
            if isinstance(number, dict) and len(number) > 7:
                print(f'In row {lid+1}/column{nid+1}: {number}')
            elif isinstance(number, dict):
                still_dicts = True

    return still_dicts

if __name__ == '__main__':
    main()
