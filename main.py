from flask import Flask, render_template,url_for, Markup
from elasticsearch import Elasticsearch
from data import *
app = Flask(__name__)

es = Elasticsearch(host='localhost', port=9200)
hotel1 = {
        'hImage': 'https://q-xx.bstatic.com/xdata/images/hotel/max300/157674722.jpg?k=bab6297144d0e071750f7c475116b051ee97b547a0c37805d66099999f4b3901&o=',
        'hCost': '13530',
        'hName': 'Universal\'s Aventura Hotel',
        'hType': 'Resort',
        'hReview': '1092',
        'hGuests': '500',
        'hBedRooms': '600',
        'hFeatures': ["Air Conditioner", "Breakfast", "Internet", "Laundry", "Parking", "Pool", "Smoking"],
        'hDescription': ' Universal\'s Aventura Hotel offers early park admission to The Wizarding World of Harry Potter™ and Universal\'s Volcano Bay water theme park 1 hour before park opening (Valid theme park admission required; attractions).<span id="dots">...</span><span id="more"><br><br>All rooms include a 43-inch flat-screen TV. A small refrigerator and coffee maker are also available. Complimentary toiletries and a hairdryer are included, as well. Certain rooms feature a seating area.<br><br>A resort-style pool with a hot tub and kids\' splash area is available for guests to enjoy. Complimentary WiFi and a free transfer to all Universal Orlando theme parks and Universal CityWalk are provided.<br><br>Restaurants come together inside a food hall offering multiple cuisines for breakfast, lunch, and dinner. The rooftop bar, lobby bar, and pool bar offer a wide range of cocktails. The Aventura also includes an onsite Starbucks®.</span>'
    }

es.index(index='database', doc_type='_doc', id=1, body=hotel1)    

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/hotel/<int:id>')
def hotel(id):
    receiveId = id
    # get index by document(id)
    res = es.get(index='database', id=receiveId)
    hotelDataById = res['_source']
    #searching by hotel id
    
    #res = es.search(index="database",
                   # body={"query": {"match": {id: receiveId}}})
    # searchingResult
    #hits = res['hits']['hits']

    return render_template('hotel.html', allHotelImages=allHotelImages, hotelDataById=hotelDataById)



if __name__ == '__main__':
    app.run(debug=True)