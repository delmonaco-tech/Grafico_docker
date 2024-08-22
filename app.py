from flask import Flask
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/')
def home():
    # Cria um gráfico simples
    plt.figure(figsize=(10,5))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16])  # Exemplo de gráfico simples
    plt.title('Gráfico Simples')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Salva o gráfico em um buffer de memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    buffer.close()

    # Retorna o gráfico como uma imagem embutida na página web
    return f'<img src="data:image/png;base64,{img_base64}" />'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


