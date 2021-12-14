--------------------------------------------------------------------------------------------------------------------------------------------------
---------------------------------------------------- Data Integratioin ---------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------------------------------


			**************    Guide d'Installation   ***************

1.Installation Manuelle de la base de donnée "PrairieMusique":

    1.1 Exécutez le fichier "Desinstllation_prairiemusic.bat" # DAL\DataBase_install\Desinstllation_prairiemusic.bat
    1.2 Exécutez le fichier "Installation_prairiemusic.bat"  # DAL\DataBase_install\Installation_prairiemusic.bat


2.Installation de la base donnée "PrairieMusique" avec Données Actualisées:
 
   2.1 Lancez le script python "Actualiser_Data.py" # \DAL
   
PS: Le script "Actualiser_Data.py" sera lancé à chaque fois en cliquant sur le bouton "Actualise" de l'application web.


            ****************     Documentations      ************************

1. ParsXML.py:

    -1.1 Récupère tous les URLs qui se trouvent dans le fichiers source.xml.    
    -2.1 Traite les URLs récupérés en filtrant sur les TOP_50 et les Features_Songs ensuite les mettre dans deux listes(list_top_50, list_songs).

2. Integration_Donnees.py:

    -2.1 Exploite les URLs contenues dans les listes et extraire les données brutes sous format json.
    -2.2 Transforme les données brutes en listes de dictionnaires (chauqe liste correspond à une table de la base de donées).

3. Build_Sql_Data.py:

    -3.1 Transforme les listes de dictionnaire en fichier.sql  (nom_table.sql) en ajoutant des requêtes "INSERT".
