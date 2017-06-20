import requests

#r = requests.get('http://echo.jsontest.com/events/mesboules/Tristal/LeCristal')
#print(r.text)

r = requests.get('http://79.137.38.211/api/public/index.php/hello/maxime')


print(r.text)
