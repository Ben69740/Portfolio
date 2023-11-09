
import streamlit as st
from streamlit_option_menu import option_menu

# Bar sur le coté

# Insérer du code HTML pour personnaliser le style de la sidebar
sidebar_custom_style = """
<style>
[data-testid="stSidebar"] {
    background-color: lightgrey;
}
.stOptionMenu {
    border-radius: 20px;
    padding: 20px;
    background-color: white;
}
.style{
    color: darkblue;
}
"""

# Afficher le style personnalisé dans la sidebar
st.markdown(sidebar_custom_style, unsafe_allow_html=True)

import pandas as pd

with st.sidebar:
    selected = option_menu(
        menu_title='Présentation',
        options=['Accueil','Projets','Compétences'])
    
if selected == 'Accueil':
    
    st.sidebar.write("--------------------------------------------------------------")
    st.sidebar.write("Restons en Contact:")
    col10, col11 = st.sidebar.columns([1,3])
    with col10 : 
        st.image("linkedin.png", width=50)
        st.image("kaggel.png", width=50)
        st.image("GitHub-Emblem.png", width=50)
    with col11 : 
        st.write("[Linkedin](https://www.linkedin.com/in/benjamin-chartier-data-analyst-python-machinelearning-powerbi)")
        st.write("[Kaggle](https://www.kaggle.com/benjaminchartier/code)")
        st.write("[GitHub](https://github.com/Ben69740?tab=repositories)")
    
    col1, col2, col3 = st.columns([1,10,1])
    with col1:st.write(" ")
    with col2:st.image('profile-pic (3).png')
    with col3:st.write(" ")
    
    st.markdown('<h3 style="color:darkblue;font-weight:bold;font-size:30px;text-align:center;">Benjamin CHARTIER</h3>', unsafe_allow_html=True)
    st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center;'>Bienvenue sur mon portfolio. Vous trouverez mes derniers projet détaillés et mes compétences.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center;'>N'hésitez pas à me contacter afin d'échanger sur de nouveaux challenges en data analyse ou business analyse.</h3>", unsafe_allow_html=True)
    st.write("----------------------------------------------------------------------------------------------")
    st.markdown("<h3 style='color:darkgreen;font-weight:bold;font-size:30px;'>Parcours</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>Après plus de dix années au sein de concessions automobiles premium : Audi, Volkswagen et BMW en tant que conseiller commercial, je décidé en 2022 d'entreprendre une reconversion professionnelle dans la DATA.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>C'est lors de ma première année d'alternance au sein de l'école de commerce INSEEC Business School que je découvre le monde de la DATA. Je suis alors, Business Intelligence Assistant au sein du groupe VOLVO TRUCK FRANCE.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>Mes missions sont diverses et variées :</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>-Key User: j'interviens auprès du réseau national de vente afin de leur proposer des KPIs pour améliorer leur vision commerciale</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>-Création de DashBoard : je suis en charge également de la création de dashboard d'aide à la décision auprès du CEO du groupe</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>-Business Analyst: je m'occupe de l'analyse des ventes mensuelles et Year to Date</h3>", unsafe_allow_html=True)
    
    st.write("----------------------------------------------------------------------------------------------")
    st.markdown("<h3 style='color:darkgreen;font-weight:bold;font-size:30px;'>Formation</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>Je suis titulaire d'un masters 2 en International Marketing auprès de l'INSEEC Business School.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>Ma reconversion professionnelle a commencé par plusieurs mois de formation auprès de Datascientest, organisme de formation reconnu. Leurs formations sont notamment certifiées par Les Mines Paris Tech. Je suis donc fier d'avoir réussi ce parcours de formation exigeant.</h3>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:grey;font-size:17px;'>Durant cette formation, j'ai réalisé un projet d'entreprise concret afin de mettre en pratique mes nouvelles compétences. Vous retrouverez ce projet dans la rubrique : Projets - Bank Marketing Prediction.</h3>", unsafe_allow_html=True)
######################################################################################################
if selected == 'Projets':
        option_submenu = st.sidebar.radio('Mes Projets réalisés', ('Preface',
                                                                   'Bank-Marketing-Prediction',
                                                                   'API - Chess Player Analytics',
                                                                   'API-Cursus-Universitaire' ,
                                                                   'Série Temporelles : Températures Terrestres',
                                                                   'World Happyness Report',
                                                                   'StoryTelling - VideoGames - Sales',
                                                                   'StoryTelling - My Company - Sales'))
        st.sidebar.write('------------------------------------------------------')
######################################################################################################        
        if option_submenu == 'Preface':
            st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:35px;text-align:center'>Preface</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:grey;font-size:17px;text-align:center'>Vous retrouverez ici, toutes mes réalisations.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;text-align:center'>Veuillez choisir un projet dans le menu à gauche de la page.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;text-align:center'>Concernant certains projets et dans un souci de clarté, vous serez redirigez vers une application Streamlit indépendante.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
######################################################################################################
        elif option_submenu == 'Bank-Marketing-Prediction':
            st.markdown("<h3 style='color:darkgreen;font-size:30px;text-align:center'>Bank Marketing Prediction.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center'>Informations sur le projet</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:15px;text-align:center'>Je vous invite à cliquer sur le lien en bas de page afin d'avoir accès au code et à l'analyse.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;font-size:20px;text-align:center'>Ce projet a été réalisé dans le cadre de la formation que j'ai suivi auprès de Datascientest.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:grey;font-size:17px;'>Objectif de ce projet: Analyser et Prédire le comportement client d'une banque afin d'améliorer les campagnes marketing futures.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Contenu:</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Exploration et nettoyage des données.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Data visualisation en vue de faire des recommandations sur le comportement client.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Prédiction du comportement des futurs prospects sur un produit financier.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Création d'une application à disposition du client final.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            col201, col202, col203, col204 = st.columns([3.5,2,2,3])
            with col201:st.write(" ")
            with col202:
                st.image("streamlit.png")
            with col203:
                st.write("[Bank-Marketing-Prediction](https://bank-marketing-prediction.streamlit.app/)")
            with col204:st.write(" ")
            st.write("----------------------------------------------------------------------------------------------")
            path_to_pbix_file = "Bank-Marketing-Prediction.pbix"
            with open(path_to_pbix_file, "rb") as f:
                    pbix_data = f.read()
                    st.download_button(
                        label="Cliquez ici pour télécharger le fichier .pbix",
                        data=pbix_data,
                        key="file_download",
                        file_name="Bank-Marketing-Prediction.pbix")
######################################################################################################        
        elif option_submenu == 'API - Chess Player Analytics':
            st.markdown("<h3 style='color:darkgreen;font-size:30px;text-align:center'>API - Chess Player Analytics.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center'>Informations sur le projet</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:grey;font-size:17px;'>Objectif de ce projet: Analyser les résultats des joueurs d'échecs.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Contenu:</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Intégration des données.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Création de KPIs.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Analyse des résultats.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkred;text-align:center;font-size:17px;'>Le temps de chargement de la page peut prendre une ou deux minutes.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.write("----------------------------------------------------------------------------------------------")
            import requests
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                       }
            response = requests.get('https://api.chess.com/pub/titled/GM', headers=headers)
            if response.status_code == 200:
                grandmasters = response.json()
                grandmasters = grandmasters['players']
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Intégration des données</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Récupération des données d'un joueur</h3>", unsafe_allow_html=True)
            def extract_player_info(player_name):
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                           }
                endpoint = "https://api.chess.com/pub/player/{}".format(player_name)
                reponse_player = requests.get(endpoint, headers = headers).json()
                return reponse_player
            joueur_test = extract_player_info("fablibi")
            st.write(joueur_test)
            
            st.markdown("<h3 style='color:grey;font-size:17px;'>Nous avons désormais accès à de nombreuses informations sur le joueur choisi.</h3>", unsafe_allow_html=True) 
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Récupération des données des 100 premiers joueurs</h3>", unsafe_allow_html=True)
            import pandas as pd
            joueurs = []
            for joueur in grandmasters[0:100]:
                joueurs.append(extract_player_info(joueur))
            df_gms = pd.DataFrame(joueurs)
            df_gms = df_gms.drop(["url", "is_streamer", "avatar", "@id", "verified", "location", "status", "twitch_url"], axis=1)
            country_endpoints = df_gms['country'].unique()
            country_dict = {}
            for endpoint in country_endpoints:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                          }
                country_name = requests.get(endpoint, headers=headers).json()['name']
                country_dict[endpoint] = country_name
            df_gms['country'] = df_gms['country'].replace(country_dict)
            st.write(df_gms)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Nous avons maintenant, toutes les informations concernant les 100 premiers joueurs.</h3>", unsafe_allow_html=True) 
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Récupération des données statistiques d'un joueur</h3>", unsafe_allow_html=True)
            
            def get_player_stats(player_name):
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
                          }
                endpoint = "https://api.chess.com/pub/player/{}/stats".format(player_name)
                player_stats = requests.get(endpoint, headers=headers).json()
                return player_stats
            stats_erik = get_player_stats("erik")
            st.write(stats_erik)
            st.markdown("<h3 style='color:black;font-size:17px;'>Voici l'ensemble des statistiques de jeu du joueur 'erik'.</h3>", unsafe_allow_html=True) 
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Récupération des données statistiques des 100 premiers joueurs</h3>", unsafe_allow_html=True)
            stats_joueurs = []
            for joueur in grandmasters[0:100]:
                stats_joueurs.append(get_player_stats(joueur))
            df_gms_stats = pd.DataFrame(stats_joueurs)
            st.write(df_gms_stats)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Nous avons maintenant, toutes les statistiques concernant les 100 premiers joueurs.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Création de KPIs</h3>", unsafe_allow_html=True)
            stats_joueur = []
            for nom in df_gms['username']:    
                info_joueur = {}
                info_joueur['Nom Joueur'] = nom
                stats_player = get_player_stats(nom) 
                key = list(stats_player.keys())
                if 'chess_rapid' in key:
                    stats_rapid = stats_player['chess_rapid']    
                    total_joue = stats_rapid['record']['win'] + stats_rapid['record']['loss'] + stats_rapid['record']['draw']
                    info_joueur['Moyenne Rapid Victoire'] = stats_rapid['record']['win'] / total_joue
                    info_joueur['Moyenne Rapid Défaite'] = stats_rapid['record']['loss'] / total_joue
                    info_joueur['Moyenne Rapid Egalité'] = stats_rapid['record']['draw'] / total_joue
                    info_joueur['Dernier Note Rapid'] = stats_rapid['last']['rating']
        
                if 'chess_blitz' in key:
                    stats_blitz = stats_player['chess_blitz']
        
                    total_joue = stats_blitz['record']['win'] + stats_blitz['record']['loss'] + stats_blitz['record']['draw']
                    info_joueur['Moyenne Blitz Victoire'] = stats_blitz['record']['win'] / total_joue
                    info_joueur['Moyenne Blitz Défaite'] = stats_blitz['record']['loss'] / total_joue
                    info_joueur['Moyenne Blitz Egalité'] = stats_blitz['record']['draw'] / total_joue
                    info_joueur['Dernier Note Blitz'] = stats_blitz['last']['rating']
        
                stats_joueur.append(info_joueur)
            stats_final = pd.DataFrame(stats_joueur)
            stats_final = stats_final.dropna()
            st.write(stats_final)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Dans ce dataframe, nous avons créé les taux de victoires, défaites et de match nul pour deux systèmes de jeu. Nous avons également intégré la dernière note obtenu par le jeu pour chaque système de jeu.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Data Visualisation</h3>", unsafe_allow_html=True)
            
            import matplotlib.pyplot as plt
            import seaborn as sns
            fig, ax = plt.subplots(figsize=(20,10))
            sns.lineplot(data=stats_final, x='Nom Joueur', y='Moyenne Rapid Victoire', color='darkcyan')
            plt.title("Taux de Victoire pour le système de jeu 'Rapid'", fontsize=25, color='darkblue', weight='bold')
            plt.gca().set_xticks([])
            st.pyplot(fig)
            
            fig, ax = plt.subplots(figsize=(20,10))
            sns.lineplot(data=stats_final, x='Nom Joueur', y='Dernier Note Rapid', color='darkcyan')
            plt.title("Dernière Note obtenue dans le système de jeu 'Rapid'", fontsize=25, color='darkblue', weight='bold')
            plt.gca().set_xticks([])
            st.pyplot(fig)
            
            st.markdown("<h3 style='color:grey;font-size:17px;'>Nous remarquons que les taux de victoires sont hétérogènes. Certains joueurs ont un taux de victoire de 1 soit 100% de victoires quand un grand nombre de joueurs sont à environ 40% de taux de victoires.</h3>", unsafe_allow_html=True)
            
            fig, ax = plt.subplots(figsize=(20,10))
            sns.lineplot(data=stats_final, x='Nom Joueur', y='Moyenne Blitz Victoire', color='darkblue')
            plt.title("Taux de Victoire pour le système de jeu 'Blitz'", fontsize=25, color='darkblue', weight='bold')
            plt.gca().set_xticks([])
            st.pyplot(fig)
            
            fig, ax = plt.subplots(figsize=(20,10))
            sns.lineplot(data=stats_final, x='Nom Joueur', y='Dernier Note Blitz', color='darkblue')
            plt.title("Dernière Note obtenue dans le système de jeu 'Blitz", fontsize=25, color='darkblue', weight='bold')
            plt.gca().set_xticks([])
            st.pyplot(fig)
            
            st.markdown("<h3 style='color:grey;font-size:17px;'>Concernant le système de jeu 'Blitz', les taux de victoire sont beaucoup plus homogènes malgrè quelques joueurs qui se démarquent soit négativement ou positivement. Rappelons que le système de jeu 'Blitz' est un système où les joueurs ont 10 minutes pour jouer, il y a donc une donnée temps qui peut influencer les résultats.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Autres Data Visualisation</h3>", unsafe_allow_html=True)
            fig, ax = plt.subplots(figsize=(20,10))
            sns.countplot(data = df_gms, x='country')
            plt.title("Nombre de joueurs par pays", fontsize=25, color='darkblue', weight='bold')
            plt.xticks(rotation=90)
            st.pyplot(fig)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Les Etats-Unis sont le pays le plus représenté suivi par l'Inde et la Russie.</h3>", unsafe_allow_html=True)
            
            df_gms = df_gms.dropna()
            fig, ax = plt.subplots(figsize=(20,10))
            sns.countplot(data = df_gms, x='league')
            plt.title("Distribution des ligues", fontsize=25, color='darkblue', weight='bold')
            plt.xticks(rotation=90)
            st.pyplot(fig)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Toutes les ligues sont globalement distribuées de la même façon. Nous remarquons, en revanche, la ligue 'Crystal' qui se détache légèrement.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Merci de votre attention pour ce projet, si vous souhaitez parcourir la totalité du code, merci de cliquer sur l'icone kaggle en-dessous.</h3>", unsafe_allow_html=True)
            col201, col202, col203, col204 = st.columns([3.5,2,2,3])
            with col201:st.write(" ")
            with col202:
                st.image("kaggel.png")
            with col203:
                st.write("[API - Chess Player Analytics](https://www.kaggle.com/benjaminchartier/api-chess-players-statistics)")
            with col204:st.write(" ")
######################################################################################################

        elif option_submenu == 'Série Temporelles : Températures Terrestres':
            st.markdown("<h3 style='color:darkgreen;font-size:30px;text-align:center'>Températures Terrestres.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:15px;text-align:center'>Je vous invite à cliquer sur le lien en bas de page afin d'avoir accès au code et à l'analyse.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center'>Informations sur le projet</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:grey;font-size:17px;'>Objectif de ce projet: Analyser et prédire les températures terrestres  .</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Contenu:</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Data visualisation : Analyse des données.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Prédiction des températures terretres avec SARIMAX.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Analyse des données Européennes.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Analyse des données des Etats-Unis.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Analyse des données de la France.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkred;text-align:center;font-size:17px;'>Le temps de chargement de la page peut prendre une ou deux minutes.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.write("----------------------------------------------------------------------------------------------")
            
            import seaborn as sns
            import matplotlib.pyplot as plt
            palette_color = ['darkcyan', 'tomato'] # Couleur ppour les graphiques
            sns.set(rc={'axes.facecolor':'lightgray'}) # Couleur du fond et de la grille
            data = pd.read_csv("GlobalTemperatures.csv")
            fig, ax = plt.subplots(figsize=(20,10))
            data['LandAverageTemperature'].plot(label='Températures')
            plt.title('Températures Terrestes par Mois',fontsize=25, color='darkblue', weight='bold')
            plt.xlabel('Date')
            plt.ylabel('Températures')
            plt.legend()
            st.pyplot(fig)
            
            st.write("----------------------------------------------------------------------------------------------")
            col201, col202, col203, col204 = st.columns([3.5,2,2,3])
            with col201:st.write(" ")
            with col202:
                st.image("kaggel.png")
            with col203:
                st.write("[Température-Terretres](https://www.kaggle.com/code/benjaminchartier/forecast-temp-with-sarima-et-prophet-dataviz)")
            with col204:st.write(" ")
            
#####################################################################################################
        
###################################################################################################
        elif option_submenu == 'API-Cursus-Universitaire':
            st.markdown("<h3 style='color:darkgreen;font-size:30px;text-align:center'>API - Cursus Universitaires.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center'>Informations sur le projet</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:grey;font-size:17px;'>Objectif de ce projet: Récupérer et créer des KPIs pertinents afin d'analyser les cursus d'une université.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Contenus:</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Récupération des données.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Créaton des KPIs.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Regroupement des données.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Data Visualisation des données.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkred;text-align:center;font-size:17px;'>Le temps de chargement de la page peut prendre une ou deux minutes.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;text-align:center;font-size:17px;'>Récupération des données:</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Dans cet exemple de création de KPI via des données récupérées avec une API, nous allons analyser les cursus d'une école. La capacité de chaque cours, le cursus majoritaire et préféré, la moyenne de chaque cursus ou encore la présence dans les cours obligatoires. Merci à tous pour votre attention.</h3>", unsafe_allow_html=True)
            
            st.write("en cours d'ajout")
#####################################################################################################

        elif option_submenu == 'World Happyness Report':
            st.markdown("<h3 style='color:darkgreen;font-size:30px;text-align:center'>World Happyness Report.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:15px;text-align:center'>Je vous invite à cliquer sur le lien en bas de page afin d'avoir accès au code et à l'analyse.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center'>Informations sur le projet</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:grey;font-size:17px;'>Objectif de ce projet: Analyser le Bonheur au niveau mondial.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Contenu:</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Vision d'ensemble des données</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Preprocessing des Données.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Analyse des corrélations.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Analyse des Valeurs.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>- Analyse Géographiques.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkred;text-align:center;font-size:17px;'>Le temps de chargement de la page peut prendre une ou deux minutes.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;font-size:20px;text-align:center'>World Happyness Report - Illustration du Score du Bonheur.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;text-align:center'>Graphique interactif vous pouvez sélectionner un pays ou une région afin de créer votre propre filtre.</h3>", unsafe_allow_html=True)
            import plotly.express as px
            happy_report = pd.read_csv('haooy_report_données_netoyes')
            fig = px.sunburst(data_frame=happy_report,
                              path=['region', 'sub-region', 'Country name'],
                              values='Ladder score',
                              color='Ladder score',
                              color_continuous_scale='rdylgn',
                              title="Vue d'ensemble du Score du Bonheur",
                              width=1000,
                              height=1000)
            st.plotly_chart(fig)
            
            
            st.write("----------------------------------------------------------------------------------------------")
            col201, col202, col203, col204 = st.columns([3.5,2,2,3])
            with col201:st.write(" ")
            with col202:
                st.image("kaggel.png")
            with col203:
                st.write("[2021 World Happyness Report](https://www.kaggle.com/code/benjaminchartier/2021-world-happyness-report-2)")
            with col204:st.write(" ")
            
#############################################################################################################            
        elif option_submenu == 'StoryTelling - VideoGames - Sales':
            st.markdown("<h3 style='color:darkgreen;font-size:30px;text-align:center'>StoryTelling - Video Games Sales.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:15px;text-align:center'>Je vous invite à cliquer sur le lien en bas de page afin d'avoir accès au code et à l'analyse.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center'>Informations sur le projet</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:grey;font-size:17px;'>Objectif de ce projet: Analyser les ventes de jeux vidéos sous différents angles.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:17px;'>Nous allons analyser les ventes de jeux vidéos en fonction, du pays d'origine, du genre du jeu, de l'éditeur, de la console de jeu etc ...</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkred;text-align:center;font-size:17px;'>Le temps de chargement de la page peut prendre une ou deux minutes.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;font-size:20px;text-align:center'>Illustrations des Ventes de jeux vidéos par Années.</h3>", unsafe_allow_html=True)
            
            import pandas as pd
            import matplotlib.pyplot as plt
            data = pd.read_csv("vgsales.csv")
            data = data.rename(columns={'Rank':'Index',
                                        'Name':'Game-Name',
                                        'Platform':'Console',
                                        'Publisher':'Editeur',
                                        'NA_Sales':'America-Sales',
                                        'EU_Sales':'Europe-Sales',
                                        'JP_Sales':'Japan-Sales'})
            ventes_full = data.groupby('Year')['Global_Sales'].sum()
            fig, ax = plt.subplots(figsize=(20,10))
            ventes_full.plot(color='darkcyan', linewidth=2.5, marker='o')
            plt.title("Evolution des Ventes Gloables", fontsize=20, weight='bold', color='darkblue')
            plt.xlabel('Année', fontsize=15, weight='bold', color='darkgreen')
            plt.ylabel('Nombre de Ventes', fontsize=15, weight='bold', color='darkgreen')
            plt.xticks(rotation=90);
            st.pyplot(fig)
            st.write("----------------------------------------------------------------------------------------------")
            col201, col202, col203, col204 = st.columns([3.5,2,2,3])
            with col201:st.write(" ")
            with col202:
                st.image("kaggel.png")
            with col203:
                st.write("[StoryTelling - Video Games Sales](https://www.kaggle.com/code/benjaminchartier/video-games-sales-analyse)")
            with col204:st.write(" ")
##############################################################################################################
        elif option_submenu == 'StoryTelling - My Company - Sales':
            st.markdown("<h3 style='color:darkgreen;font-size:30px;text-align:center'>StoryTelling - My Company - Sales.</h3>", unsafe_allow_html=True)
            st.markdown("<h3 style='color:grey;font-size:15px;text-align:center'>Je vous invite à cliquer sur le lien en bas de page afin d'avoir accès au code et à l'analyse.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkcyan;font-weight:bold;font-size:25px;text-align:center'>Informations sur le projet</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:grey;font-size:17px;'>Objectif de ce projet:Création de KPI pertinents afin d'analyser les ventes d'un entreprise sous différents angles.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkred;text-align:center;font-size:17px;'>Le temps de chargement de la page peut prendre une ou deux minutes.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            st.write("----------------------------------------------------------------------------------------------")
            st.markdown("<h3 style='color:darkgreen;font-size:20px;text-align:center'>Nos données sont présentes dans plusieurs datasets différents.</h3>", unsafe_allow_html=True)
            st.write("----------------------------------------------------------------------------------------------")
            col201, col202, col203, col204 = st.columns([3.5,2,2,3])
            with col201:st.write(" ")
            with col202:
                st.image("kaggel.png")
            with col203:
                st.write("[StoryTelling - My Company Sales](https://www.kaggle.com/code/benjaminchartier/storytelling-my-campany-sales)")
            with col204:st.write(" ")

######################################################################################################

if selected == 'Compétences':
    st.sidebar.write("--------------------------------------------------------------")
    st.sidebar.write("Restons en Contact:")
    col10, col11 = st.sidebar.columns([1,3])
    with col10 : 
        st.image("linkedin.png", width=50)
        st.image("kaggel.png", width=50)
        st.image("GitHub-Emblem.png", width=50)
    with col11 : 
        st.write("[Linkedin](https://www.linkedin.com/in/benjamin-chartier-data-analyst-python-machinelearning-powerbi)")
        st.write("[Kaggle](https://www.kaggle.com/benjaminchartier/code)")
        st.write("[GitHub](https://github.com/Ben69740?tab=repositories)")
    st.sidebar.write("--------------------------------------------------------------")
    st.sidebar.image("profile-pic (3).png")
    
    #Corps de la Page
    st.markdown('<h3 style="color:darkcyan;font-weight:bold;font-size:45px;text-align:center;">Compétences Acquises</h3>', unsafe_allow_html=True)
    st.write("----------------------------------------------------------------------------------------------")
    st.markdown("<h3 style='color:darkgreen;font-weight:bold;font-size:30px;text-align:center'>Compétences Data</h3>", unsafe_allow_html=True)
    col101, col102, col103, col104 = st.columns([3.5,2,2,3])
    with col101:st.write(" ")
    with col102:
        st.write("Python")
        st.write("Pandas")
        st.write("Data Quality")
        st.write("Matplotlib")
        st.write("Plotly")
        st.write("Machine Learning")
        st.write("Sklearn")
        st.write("Clustering")
        st.write("Reduction de Dimensions")
        st.write("Power BI")
        st.write("SQL")
        st.write("Text Mining")
        st.write("ETL")
    with col103:
        st.write("StoryTelling")
        st.write("Statistiques Exploratoiores")
        st.write("Numpy")
        st.write("Seaborn")
        st.write("Bokeh")
        st.write("Advanced Sklearn")
        st.write("PySpark")
        st.write("Analyse de Données")
        st.write("Series Temporelles")
        st.write("Selenium")
        st.write("Beautifoul Soup")
    with col104:st.write(" ")
    st.write("----------------------------------------------------------------------------------------------")
    st.markdown("<h3 style='color:darkgreen;font-weight:bold;font-size:30px;text-align:center'>Autres Compétences</h3>", unsafe_allow_html=True)
    col105, col106, col107, col108 = st.columns([3.5,2,2,3])
    with col105:st.write(" ")
    with col106:
        st.write("Vente")
        st.write("Négociation")
        st.write("Fidélisation Client")
        st.write("Ecoute Client")
        st.write("Anglais : Courant")
    with col107:
        st.write("Travail en Equipe")
        st.write("Gestion du Stress")
        st.write("Gestion de la Pression")
        st.write("SalesForce")
    with col108:st.write(" ")