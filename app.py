from flask import Flask, render_template, request 
  
# import json to load JSON data to a python dictionary 
import json ,requests
  
# urllib.request to make a request to api 
import urllib.request 

  
  
app = Flask(__name__) 
  
@app.route('/', methods =['POST', 'GET']) 
def weather(): 
    if request.method == 'POST': 
        city = request.form['city'] 
    else: 
        # for default name mathura 
        city = 'Kolkata'
  
    # your API key will come here 
    api_key="54d8db7d2c9ee642e6da59f3888cddb9";
  
    # source contain json data from api 
    source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=54d8db7d2c9ee642e6da59f3888cddb9').read() 
    complete_url = 'http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=54d8db7d2c9ee642e6da59f3888cddb9'
    response = requests.get(complete_url) 
    x = response.json() 

    # converting JSON data to a dictionary
    if x["cod"] != "404":
     y = x["main"]
     z = x["weather"]
     p = x ["wind"]
     weather_description = z[0]["description"]
     wind = p["speed"] 
    list_of_data = json.loads(source) 
    data = { 
        "country_code": str(list_of_data['sys']['country']), 
        "coordinate": str(list_of_data['coord']['lon']) + ' , ' 
                    + str(list_of_data['coord']['lat']), 
        "temp": str(list_of_data['main']['temp'])+ ' K', 
        "pressure": str(list_of_data['main']['pressure']) +' mbar', 
        "humidity": str(list_of_data['main']['humidity'])+ ' %', 
        "des":str( weather_description) ,
        "wind":str( wind)
    } 
    
   
    # data for variable list_of_data 
   
    print(data) 
    return render_template('index.html', data = data) 
  
  
  
if __name__ == '__main__': 
    app.run(debug = True) 