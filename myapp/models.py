from django.db import models
from django.contrib import admin

# Create your models here.

class Listes(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=255)
    prénom=models.CharField(max_length=255)
    email=models.EmailField(blank=True)
    telephone=models.IntegerField()
    ETUDIANT='Etudiant' 
    ENSEIGNANT='Enseignant' 
    statut = [
        (ETUDIANT, 'Etudiant'),
        (ENSEIGNANT, 'Enseignant')
    ]   
    statut=models.CharField( 
        max_length=255, 
        choices=statut,
        default=ETUDIANT
        )

    LICENCE1='L1'
    LICENCE2='L2'
    LICENCE3='L3'
    MASTER1='M1'
    MASTER2='M2'
    
    niveau  = [
        (LICENCE1, 'Licence 1'),
        (LICENCE2, 'Licence 2'),
        (LICENCE3, 'Licence 3'),
        (MASTER1, 'Master 1'),
        (MASTER1, 'Master 2'),
       
    ]   
    niveau=models.CharField( 
        max_length=2, 
        choices=niveau,
        default=LICENCE1
        )

    
    SEGMI='Sciences Economiques, Gestion, Mathématiques, Informatique (SEGMI)'
    LCE='Langues et Cultures Etrangères (LCE)'
    PHILLIA='Philosophie, Information-Communication, Langage, Littérature, Arts du spectacle (PHILLIA)'
    DSP='Droit et Science Politique (DSP)'
    SPSE="Sciences Psychologiques et Sciences de l'Education (SPSE)"
    SSA='Sciences Sociales et Administration (SSA)'
    STAPS='Sciences et Techniques des Activités Physiques et Sportives (STAPS)'
    SITEC='Systèmes Industriels et Techniques de Communication (SITEC)'
    SITEC="IUT Ville d'Avray/St Cloud/Nanterre"
    UFR  = [
        (SEGMI, 'Sciences Economiques, Gestion, Mathématiques, Informatique (SEGMI)'),
        (LCE, 'Langues et Cultures Etrangères (LCE)'),
        (PHILLIA,'Philosophie, Information-Communication, Langage, Littérature, Arts du spectacle (PHILLIA)'),
        (DSP, 'Droit et Science Politique (DSP)'),
        (SPSE, "Sciences Psychologiques et Sciences de l'Education (SPSE)"),
        (SSA, 'Sciences Sociales et Administration (SSA)'),
        (STAPS, 'Sciences et Techniques des Activités Physiques et Sportives (STAPS)'),
        (SITEC, 'Systèmes Industriels et Techniques de Communication (SITEC)'),
        (SITEC,"IUT Ville d'Avray/St Cloud/Nanterre"),
       
    ]   
    UFR=models.CharField( 
        max_length=255, 
        choices=UFR,
        default=(SEGMI)
        )        
    
    
    MIASHS ='MIASHS'
    Economie_et_Gestion ='Economie et Gestion'
    Espagnol = 'Espagnol'
    Etudes_anglo_américaines = 'Etudes anglo américaines'
    Etudes_germaniques = 'Etudes germaniques'
    Italien = 'Italien '
    Langues_étrangères_appliquées = ' Langues étrangères appliquées (LEA)'
    Portugais = 'Portugais'
    Russe = 'Russe'
    Centre_de_ressources_Langues = 'CRL - Centre de ressources Langues'
    Arts_du_spectacle = 'Arts du spectacle'
    Sciences_de_l_information_et_de_la_communication = "Sciences de l'information et de la communication"
    Langues_et_littératures_grecques_et_latines = 'Langues et littératures grecques et latines '
    Lettres_modernes = 'Lettres modernes '
    Philosophie = 'hilosophie'
    Sciences_du_langage = 'Sciences du langage'
    Science_Politique = 'Science Politique '
    Psychologie = ' Psychologie'
    Sciences_de_l_éducation = " Sciences de l'éducation"
    Administration_économique_et_sociale = 'Administration économique et sociale'
    Anthropologie = 'Anthropologie'
    Histoire = 'Histoire'
    Histoire_de_l_art_et_de_l_archéologie = "Histoire de l'art et de l'archéologie"
    Géographie_et_aménagement = 'Géographie et aménagement'
    Sociologie = 'Sociologie'
    Métiers_du_livre_et_de_l_audiovisuel = "Métiers du livre et de l'audiovisuel"
    Sciences_de_l_ingénieur = "Sciences de l'ingénieur"
    Génie_Électrique_et_Informatique_Industrielle = 'Génie Électrique & Informatique Industrielle (GEII)'
    Génie_Mécanique_Productique = 'Génie Mécanique & Productique (GMP)'
    Génie_Thermique_et_Énergie = 'Génie Thermique & Énergie (GTE)'
    Gestion_des_Entreprises_et_des_Administrations = 'Gestion des Entreprises & des Administrations'
    Carrières_Sociales = 'Carrières Sociales'
    Métiers_du_livre_et_de_l_audiovisuel = "Métiers du livre et de l'audiovisuel"

    département = [
        (MIASHS, 'MIASHS'),
        (Economie_et_Gestion, 'Economie et Gestion'),
        (Espagnol, 'Espagnol'),
        (Etudes_anglo_américaines, 'Etudes anglo américaines'),
        (Etudes_germaniques, 'Etudes germaniques'),
        (Italien, 'Italien '),
        (Langues_étrangères_appliquées, ' Langues étrangères appliquées (LEA)'),
        (Portugais, 'Portugais'),
        (Russe, 'Russe'),
        (Centre_de_ressources_Langues, 'CRL - Centre de ressources Langues'),
        (Arts_du_spectacle, 'Arts du spectacle'),
        (Sciences_de_l_information_et_de_la_communication, "Sciences de l'information et de la communication"),
        (Langues_et_littératures_grecques_et_latines, 'Langues et littératures grecques et latines'),
        (Lettres_modernes, 'Lettres modernes'),
        (Philosophie, 'hilosophie'),
        (Sciences_du_langage, 'Sciences du langage'),
        (Science_Politique, 'Science Politique'),
        (Psychologie, ' Psychologie'),
        (Sciences_de_l_éducation, " Sciences de l'éducation"),
        (Administration_économique_et_sociale, 'Administration économique et sociale'),
        (Anthropologie, 'Anthropologie'),
        (Histoire, 'Histoire'),
        (Histoire_de_l_art_et_de_l_archéologie, "Histoire de l'art et de l'archéologie"),
        (Géographie_et_aménagement, 'Géographie et aménagement'),
        (Sociologie, 'Sociologie'),
        (Métiers_du_livre_et_de_l_audiovisuel, "Métiers du livre et de l'audiovisuel"),
        (Sciences_de_l_ingénieur, "Sciences de l'ingénieur"),
        (Génie_Électrique_et_Informatique_Industrielle, 'Génie Électrique & Informatique Industrielle (GEII)'),
        (Génie_Mécanique_Productique, 'Génie Mécanique & Productique (GMP)'),
        (Génie_Thermique_et_Énergie, 'Génie Thermique & Énergie (GTE)'),
        (Gestion_des_Entreprises_et_des_Administrations, 'Gestion des Entreprises & des Administrations'),
        (Carrières_Sociales, 'Carrières Sociales'),
        (Métiers_du_livre_et_de_l_audiovisuel, "Métiers du livre et de l'audiovisuel"),
    ]   
    département=models.CharField( 
        max_length=255, 
        choices=département,
        default=MIASHS
        )

    MIAGE='MIAGE'
    MATHS='MATHS'
    ECONOMIE='ECONOMIE' 
    GESTION='GESTION'
    DOUBLE_LICENCE='DOUBLE LICENCE'
    AUTRES = 'AUTRES PARCOURS'
    parcours = [
        (MIAGE, 'MIAGE'),
        (MATHS, 'MATHS'),
        (ECONOMIE, 'ECONOMIE'),
        (GESTION, 'GESTION'),
        (DOUBLE_LICENCE, 'DOUBLE LICENCE'),
        (AUTRES, 'AUTRES PARCOURS'),
    ]   
    parcours=models.CharField( 
        max_length=255, 
        choices=parcours,
        default=MIAGE
        )

    
    TD1='TD1'
    TD2='TD2'
    TD3='TD3'
    
    groupe_de_TD = [
        (TD1, 'TD1'),
        (TD2, 'TD2'),
        (TD3, 'TD3')
        
    ]   
    groupe_de_TD=models.CharField( 
        max_length=255, 
        choices=groupe_de_TD,
        default=TD1
        )        
        
        
    date_de_declaration=models.DateTimeField(auto_now_add=True)
    testPCR=models.FileField(upload_to='pdf')
    
    POSITIF='Positif'
    CAS_CONTACT='Cas contact' 
    SYMPTOMATIQUE='Syptomatique'
    AUTRES='Autres' 
    sujet = [
        (POSITIF, 'Positif'),
        (CAS_CONTACT, 'Cas contact'),
        (SYMPTOMATIQUE, 'Symptomatique'),
        (AUTRES, 'Autres')
    
    ]   
    sujet=models.CharField( 
        max_length=255, 
        choices=sujet,
        default=POSITIF
        )

    message=models.TextField()
    

class ListesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom', 'prénom', 'email', 'telephone','niveau', 'UFR','département', 'parcours', 'groupe_de_TD', 'statut', 'date_de_declaration', 'testPCR', 'sujet', 'message')
    list_filter = ('date_de_declaration',)
    search_fields = ['nom', 'telephone']