from flask import Flask, render_template

dicionario = {
  1: {
      "nome": "Harry Potter",
      "raça": "Humano",
      "casa": "Grifinória",
      "altura": "1.80",
      "nascimetno": "31/07/1980",
      "imagem": "https://p2.trrsf.com/image/fget/cf/1200/1600/middle/images.terra.com/2023/04/14/594335823-harry-potter.jpg"
  },
  2: {
      "nome": "Ron Weasley",
      "raça": "Humano",
      "casa": "Grifinória",
      "altura": "1.83",
      "nascimetno": "01/08/1980",
      "imagem": "https://upload.wikimedia.org/wikipedia/en/5/5e/Ron_Weasley_poster.jpg"
  },
  3: {
      "nome": "Hermione Granger",
      "raça": "Humano",
      "casa": "Grifinória",
      "altura": "1.60",
      "nascimetno": "10/09/1980",
      "imagem": "https://pm1.aminoapps.com/6293/299271e4398cb7e4dcd6c5e779c8602e482c02fe_hq.jpg"
  }
}

def retorna_personagem():
  for chave, valor in dicionario.items():
    print(f"{chave} - {valor}")

app = Flask(__name__)

@app.route("/")
def teste():
  return dicionario

@app.route("/personagem/<int:personagem_id>")
def mostra_personagem(personagem_id):
  return render_template('personagem.html', **dicionario[personagem_id])

@app.route("/personagem_boot/<int:personagem_id>")
def mostra_personagem_boot(personagem_id):
  return render_template('personagem_boot.html', **dicionario[personagem_id])

@app.route("/personagens")
def mostra_personagens():
  return render_template('personagens_bootlist.html', personagens=dicionario)


app.run(debug=True)