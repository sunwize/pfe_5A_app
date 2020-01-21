from bson import ObjectId, json_util
from fonctions import load_data, prediction, entrainementQuiz, predictionQuiz, calculScoreBigFive
import pandas as pd
from flask import Flask, render_template, request, jsonify, json, g
from flask_cors import CORS, cross_origin
import ast
import pymongo
import json

##########################################################################################################################
###################################                 ROUTES POUR LES                 ######################################
###################################                   PREDICTIONS                   ######################################
##########################################################################################################################

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['CORS_HEADERS'] = 'Access-Control-Allow-Origin'

@app.route('/textPrediction', methods=['GET', 'POST'])
def donnerPersonnalite():
    print("test predict") 
    data = request.args.get('text')
    df = pd.read_csv("dataset/mbti_1.csv")
    load_data(df)
    #entrainement(output_dir="./model")
    #f = open("text.txt", "r") 
    js = prediction(model="./model", text=data)

    INTRO="E"
    INTUITION="S"
    JUGEMENT="P"
    REFLEXION="F"

    if js["INTROVERTED"] >= 0.5:
        INTRO="I"
    
    if js["INTUTIVE"] >= 0.5:
        INTUITION="N"
    
    if js["JUDGEMENTAL"] >= 0.5:
        JUGEMENT="J"
    
    if js["THINKING"] >= 0.5:
        REFLEXION="T"

    Personnalite=INTRO+INTUITION+REFLEXION+JUGEMENT
    print(Personnalite)
    js["PERSONNALITE"]=Personnalite
    return js

@app.route('/quizMbtiPrediction', methods=['GET', 'POST'])
def donnerPersonnaliteQuiz():
    data = request.args.get('liste')
    data='[['+data+']]'
    data=ast.literal_eval(data)
    input = pd.DataFrame(data)

    #Chargement dataset
    df = pd.read_csv('dataset/dataset_mbti_quiz.csv', names=['Personnalite', 'Reponses'])

    # Nombre de ligne par personnalité 
    #print(df.groupby('Personnalite').count())
    for i in range(len(df)):
          df['Reponses'][i] = ast.literal_eval(df['Reponses'][i])
    
    df[['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59']] = pd.DataFrame(df.Reponses.values.tolist(), index= df.index)

    y=df.Personnalite
    x=df.drop(['Reponses', 'Personnalite' ],axis=1)
    entrainementQuiz(x,y)
    Personnalite = predictionQuiz(model="model/models_quiz/model_quiz_mbti.sav", x=input)
    print(Personnalite)
    return Personnalite[0]


@app.route('/quizBig5Prediction', methods=['GET', 'POST'])
def donnerPersonnaliteQuizB5():
    data = request.args.get('liste')
    data = '['+data+']'
    data = ast.literal_eval(data)

    result = calculScoreBigFive(data)
    return result
   
#Gestion BDD
client = pymongo.MongoClient("mongodb+srv://teddy:GOULAGTV@cluster0-2heou.mongodb.net/Big5Mbti?retryWrites=true&w=majority")
db = client.Big5Mbti

@app.route('/insert', methods=['GET', 'POST'])
def insertBDD():
    my_json = request.get_data().decode('utf8').replace("'", '"')
    data = json.loads(my_json)
    comparaison = dict()
    comparaison['mbti'] = data['mbti']
    comparaison['big5'] = data['bf']
    print(my_json)
    print(comparaison)
    print(data)
    print('- ' * 20)
    personnalityBig5Mbti=db.personnalityBig5Mbti 
    personnalityBig5Mbti.insert_one(comparaison).inserted_id
    return "ok2"



@app.route('/get', methods=['GET', 'POST'])
def getBDD():
    personnalityBig5Mbti=db.personnalityBig5Mbti 
    result = personnalityBig5Mbti.find()
    result=str(list(result))
    
  
    # # create an empty DataFrame obj for storing Series objects
    # docs = pd.DataFrame(columns=[])
    # # iterate over the list of MongoDB dict documents
    # mongo_docs = list(result)
    # for num, doc in enumerate(mongo_docs):
    #     # convert ObjectId() to str
    #     doc["_id"] = str(doc["_id"])
    #     # get document _id from dict
    #     doc_id = doc["_id"]
    #     # create a Series obj from the MongoDB dict
    #     series_obj = pd.Series(doc, name=doc_id)

    #     # append the MongoDB Series obj to the DataFrame obj
    #     docs = docs.append(series_obj)


    return result
