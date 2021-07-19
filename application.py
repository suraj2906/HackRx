from flask import Flask
from flask_restful import Api,Resource
import spacy

app = Flask(__name__)
api = Api(app)

class Suggetions(Resource):
    def get(self, text):
        nlp = spacy.load("en_core_web_lg")
        doc = nlp(text)
        print(doc.text)
        print({(ent.text.strip(), ent.label_) for ent in doc.ents})
        return {}

    def post(self):
        return
api.add_resource(Suggetions, "/suggetions/<string:text>") 

if __name__ == '__main__':
    app.run(debug=True)


