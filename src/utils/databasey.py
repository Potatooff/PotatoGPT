import sqlite3
from src.utils.values import raw_database_path



def _Cleaner_database(foo: list) -> list:
    """Clean the results from the database.
    foo: list cleaner"""
    
    bar: list = []
    for i in foo:
        for j in i:
            if j == i[0]:
                pass
            else:
                j = j[2:]
            bar.append(j)
    return bar


def _patterns_parser(tag) -> list:
    """Parse patterns from the database.
    tag: string with tag name to find in the database."""

    holder: list = []

    conn = sqlite3.connect(raw_database_path) # Connect to the database
    cursor = conn.cursor()

    cursor.execute('SELECT patterns FROM intents WHERE tags = ?', (tag,)) # Check database!
    result = cursor.fetchone() # Get results
    conn.close()

    if result:
        patterns: list = result
    
        for i in patterns:
            if i != patterns[0]:
                i = i[2:]
            patterns_list: list = i.split('#@!') # Remove code from strings
            patterns_list.remove('') # Remove weird empty string
            holder.append(patterns_list)

        holder: list = _Cleaner_database(holder)

    else:
        print(f'Tag: "{tag}" not found in the database.')

    return holder 



def _responses_parser(tag) -> list:
    """Parse responses from the database.
    tag: string with tag name to find in the database."""

    holder: list = []
    conn = sqlite3.connect(raw_database_path) # Connect to the database
    cursor = conn.cursor()

    cursor.execute('SELECT responses FROM intents WHERE tags = ?', (tag,)) # Check database!
    result = cursor.fetchone() # Get results
    conn.close()

    if result:
        responses: list = result

        for i in responses:
            if i != responses[0]:
                i = i[2:]
            responses_list: list = i.split('#@!')
            responses_list.remove('') # Remove weird empty string
            holder.append(responses_list)

        holder: list = _Cleaner_database(holder)
    
    else:
        print(f'Tag: "{tag}" not found in the database.')

    return holder


def _tags_parser() -> list:

    """Parse all tags from the database."""

    conn = sqlite3.connect(raw_database_path) # Connect to the database
    cursor = conn.cursor()

    cursor.execute('SELECT tags FROM intents') # Check database!
    result = cursor.fetchall() # Get results
    conn.close()

    tags_list: list = []
    for i in result:
        for j in i:
            tags_list.append(j)

    return tags_list
