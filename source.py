import csv

ficheiro = 'perguntas.csv' # Nome do arquivo que contém as perguntas
ficheiro_final = 'perguntas_moodle.xml' # Nome do arquivo final no formato XML

# Função para converter uma linha do arquivo CSV para o formato XML Moodle
def converter_linha(linha):
    questão = linha[0] # Coluna 1 é a questão
    dificuldade = linha[1] # Coluna 2 é a dificuldade da questão
    resposta_correta = linha[2] # Coluna 3 é a resposta correta
    respostas_incorreta = linha[3:] # Restantes colunas são as respostas incorretas

    xml = f'<question type="multichoice">\n'
    xml += f'    <name>\n'
    xml += f'        <text>{dificuldade}</text>\n' # O nome da pergunta é o nível de dificuldade
    xml += f'    </name>\n'
    xml += f'    <questiontext format="moodle_auto_format">\n'
    xml += f'        <text><![CDATA[<p>{questão}</p>]]></text>\n'  # Texto da pergunta formatado como HTML
    xml += f'    </questiontext>\n'
    xml += f'    <single>true</single>\n' # Resposta de escolha única
    xml += f'    <shuffleanswers>true</shuffleanswers>\n' # Baralhar as respostas
    xml += f'    <answernumbering>ABCD</answernumbering>\n' # Numeração ABCD escolha múltipla

    for answer in [resposta_correta] + respostas_incorreta:
        xml += f'    <answer fraction="{100 if answer == resposta_correta else 0}">\n'
        xml += f'        <text>{answer}</text>\n'
        xml += f'        <feedback><text> {"Correto!" if answer == resposta_correta else "Incorreto."}</text></feedback>\n'
        xml += f'    </answer>\n'

    xml += f'</question>\n'
    return xml

with open(ficheiro, 'r') as f:
    r = csv.reader(f, delimiter=';')
    next(r)  #Salta o header
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<quiz>\n'
    
    for linha in r:
        xml += converter_linha(linha) # Converte cada linha do arquivo CSV em XML

    xml += '</quiz>'
    
# Escrever conteúdo XML no arquivo final
with open(ficheiro_final, 'w') as f:
    f.write(xml)
