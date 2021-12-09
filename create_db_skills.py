# Create database and connection
from db import cursor
from db import db
# input to choose a option
message_input = """
what do you want to do ?
's' ==> Show skills
'a' ==> Add skill
'd' ==> Delete skill
'u' ==> Update skill
'q'==> Quit Skills App
choose option : 
"""

message_input_up = """
Would you update it : 
'y' For Yes , 
'n' for No
choose your option : 
"""


def commit_close():
    """Cmmit and close database"""
# commit changes
    db.commit()
    # Close connection
    db.close()


# User input
user_input = input(message_input).strip().lower()

# Define a functions


def show_skills():
    """Show all skills"""
    query = f"SELECT * FROM skills WHERE user_id == '{idu}'"
    cursor.execute(query)
    results = cursor.fetchall()
    print(f'You have {len(results)} skills ')
    if len(results) > 0:
        for row in results:
            print(f'skill : {row[0]} ==> {row[1]}')

    commit_close()


idu = 2


def add_skill():
    # User Input skill name and progress
    sk = input('What is the name of the skill : ').strip().capitalize()
    # Check if skill is exixsted
    query = f"SELECT name FROM skills WHERE name = '{sk}' AND user_id == '{idu}'"
    cursor.execute(query)
    result = cursor.fetchone()
    if result == None:
        prog = input(f'What is your {sk} progress : ').strip()
        # to change for risk sql injection
        # query = f"INSERT INTO skills (name,progress,user_id) VALUES ('{sk}','{prog}','{idu}')"
        # Protected sql injection
        query = f"INSERT INTO skills (?,?,?) VALUES ('{sk}','{prog}','{idu}')"
        commit_close()
        print('Skill is added !')
    else:
        print('The skill exists !')
        user_chosse = input(message_input_up).strip().lower()

        if user_chosse == 'y':
            update_skill()
        elif user_chosse == 'n':
            commit_close()
        else:
            print('Your choise is not valid ! ')


def delete_skill():
    sk = input('What is the skill to delete : ').strip().capitalize()
    query = f"DELETE FROM skills WHERE name == '{sk}'AND user_id == '{idu}' "
    cursor.execute(query)
    print('Skill is deleted !')


def update_skill():
    # User Input skill name and progress
    sk = input('What is the name of the skill : ').strip().capitalize()
    new_prog = input(f'What is new your {sk} progress : ').strip()
    # to change for risk sql injection
    query = f"UPDATE skills  SET progress = '{new_prog}'WHERE name='{sk}' AND user_id == '{idu}' "
    cursor.execute(query)
    commit_close()
    print('Skill is updated !')


# Check user input
options = ['s', 'a', 'd', 'u', 'q']
if user_input in options:
    if user_input == "s":
        show_skills()
    elif user_input == 'a':
        add_skill()
    elif user_input == 'd':
        delete_skill()
    elif user_input == 'u':
        update_skill()
    else:
        print('Skills App is closed !')


else:  # Input error
    print(f'Your choose \"{user_input}\" is not in options ')
