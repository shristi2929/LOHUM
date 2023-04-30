from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
@app.route('/price')
def get_price():
    try:
        response = requests.get('https://www.metal.com/Lithium-ion-Battery/202303240001')
        soup = BeautifulSoup(response.content, 'html.parser')
        soup
        # Scrape price information
        price = soup.select_one('.strong__1JlBD.priceDown__2TbRQ').get_text()
        return jsonify({'price': price})
    except:
        return jsonify({'error': 'Error scraping price information'}), 500
if __name__ == '__main__':
    app.run(port=3000)
Serving Flask app '__main__'

