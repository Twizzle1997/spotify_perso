""" Ce fichier permet de simplifier l'écriture des fichiers d'insertion .sql
"""

def __write_query(file, query):
    file.write(query + '\n')

def __build_query_insert(table, columns, values):
    return "INSERT INTO %s (%s) VALUES (%s);" %(table, columns, values)

def BuildSQLFile(table_name, list):
    """ Create a .sql file with given args

    Args:
        table_name (string): name of the table and generated file.sql
        list (list of dictionaries): data to insert in the .sql file

    Example:
        The list must be like this:
        [
            {
                'id': 'xxxx',
                'name': 'yyyy'
            }
        ]
    """

    #referme automatiquement le fichier à la sortie du "with"
    with open("./DAL/DataBase_install/%s.sql" %(table_name), "w", encoding='utf-8') as file:
        for dictionary in list:
            columns = ', '.join("'" + str(key).replace("'", '_') + "'" for key in dictionary.keys())
            values = ', '.join("'" + str(val).replace("'", '_') + "'" for val in dictionary.values())

            __write_query(file, __build_query_insert(
                table_name,
                columns,
                values
            ))

    ls = []
    with open("./DAL/DataBase_install/%s.sql" %(table_name), 'r', encoding='utf-8') as file:
        for line in file:
            if line not in ls:
                ls.append(line)
    with open("./DAL/DataBase_install/%s.sql" %(table_name), 'w', encoding='utf-8') as file:
        for line in ls:
            file.write(line)
