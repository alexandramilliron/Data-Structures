"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    houses = set()


    openfile = open(filename)
    for line in openfile:
        splitline = line.split("|")

        if splitline[2] == "":
          continue 
        else:
          houses.add(splitline[2])       

    return houses



def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    students = []

    the_file = open(filename)
    for line in the_file:
      line = line.rstrip()
      line = line.split("|")
      full_name = " ".join(line[0:2])

      if line[4] == "G" or line[4] == "I":
        continue
      elif line[4] == cohort:
        students.append(full_name)
      elif cohort == "All":
        students.append(full_name)
        
    return sorted(students)



def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """

    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []
    roster = []

    the_file = open(filename)
    for line in the_file:
        line = line.rstrip()
        line = line.split("|")
        full_name = " ".join(line[0:2])

        if "Dumbledore's Army" in line:
            dumbledores_army.append(full_name)

        if "Gryffindor" in line:
            gryffindor.append(full_name)

        if "Hufflepuff" in line:
            hufflepuff.append(full_name)
        
        if "Ravenclaw" in line:
            ravenclaw.append(full_name)
      
        if "Slytherin" in line:
            slytherin.append(full_name)

        if "G" in line:
            ghosts.append(full_name)

        if "I" in line:
            instructors.append(full_name)         
    
    return [sorted(dumbledores_army),
            sorted(gryffindor),
            sorted(hufflepuff),
            sorted(ravenclaw),
            sorted(slytherin),
            sorted(ghosts),
            sorted(instructors)]



def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """

    all_data = []

    the_file = open(filename)
    for line in the_file:
        line = line.rstrip().split("|")
        full_name = " ".join(line[0:2])
        house = line[2]
        advisor = line[3]
        cohort = line[4]

        tup = (full_name, house, advisor, cohort) 

        all_data.append(tup)


    return all_data 


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """

    the_file = open(filename)
    for line in the_file:
        line = line.rstrip().split("|")
        name_in_line = " ".join(line[0:2])
        cohort = line[4]

        if name == name_in_line:
            return cohort 

    return None



def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """
    
    last_names = []
    dupe_names = set()

    the_file = open(filename)
    for line in the_file:
        line = line.rstrip().split("|")
        last_name = line[1]

        if last_name in last_names:
            dupe_names.add(last_name)

        last_names.append(last_name)
    
    return dupe_names


def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """

    housemates = set() 
    house = ""
    cohort = ""

    the_file = open(filename)
    for line in the_file:
        line = line.rstrip().split("|")
        name_in_line = " ".join(line[0:2])

        if name == name_in_line:
            house = line[2]
            cohort = line[4]

    the_file = open(filename)
    for line in the_file:
        line = line.rstrip().split("|")
        name_in_line = " ".join(line[0:2])
      
        if line[2] == house and line[4] == cohort and name_in_line != name:
            housemates.add(name_in_line)
    
    return housemates
        


##############################################################################
# END OF MAIN EXERCISE. Yay! You did it! You rock!


if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
