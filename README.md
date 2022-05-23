# Empl
Employee Mangement App



# Getting all data   : GET http://127.0.0.1:8000/api/all"  

# update row data  : POST http://127.0.0.1:8000/api/update , data = {full employee data }  
## example with requests :  
	r = requests.post("http://127.0.0.1:8000/api/update" , data ={
    "id": 12,
    "Name": "Issam ",
    "Birthday": {
        "year": 2015,
        "month": 4,
        "day": 18
    },
    "HiredOn": {
        "year": 2015,
        "month": 4,
        "day": 18
    },
    "Position": "-----",
    "Email": "----@gmail.gmail",
    "PhoneNumber": "0000000000",
    "IsManager": false,
    "Team": {
        "Dev_team": true,
        "Design_team": true,
        "DevOps_team": false
    }
})
## example with curl :  	
	curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 259' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: python-requests/2.25.1' -d 'id=12&Name=Issam+99999999999999999999&Birthday=year&Birthday=month&Birthday=day&HiredOn=year&HiredOn=month&HiredOn=day&Position=Justice+league&Email=darkside%40gmail.gmail&PhoneNumber=21625881317&IsManager=False&Team=Dev_team&Team=Design_team&Team=DevOps_team' http://127.0.0.1:8000/api/update



# Delete partial employees list :  POST http://127.0.0.1:8000/api/delete , data = "all" | list of ids  : 
## example with requests :  
	r = requests.post("http://127.0.0.1:8000/api/delete" , data = {"ids" : [10,2,3]})

## example with curl : 
	curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 18' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: python-requests/2.25.1' -d 'ids=10&ids=2&ids=3' http://127.0.0.1:8000/api/delete  


#Add new row  : POST http://127.0.0.1:8000/api/add , data = { "data" : json.dumps(json_row_reprensentation)}  : 

## example with requests :  
	r = requests.post("http://127.0.0.1:8000/api/add", data={
		"data": "{\"Name\": \"xxxxxxxxxxx \", \"Birthday\": {\"year\": 2015, \"month\": 4, \"day\": 18}, \"HiredOn\": {\"year\": 2015, \"month\": 4, \"day\": 18}, \"Position\": \"uuuuu\", \"Email\": \"vvvvv@gmail.gmail\", \"PhoneNumber\": \"lllll\", \"IsManager\": true, \"Team\": {\"Dev_team\": true, \"Design_team\": true, \"DevOps_team\": false}}"
	} )

## example with curl : 
	curl -X POST -H 'Accept: */*' -H 'Accept-Encoding: gzip, deflate' -H 'Connection: keep-alive' -H 'Content-Length: 457' -H 'Content-Type: application/x-www-form-urlencoded' -H 'User-Agent: python-requests/2.25.1' -d data=%7B%22Name%22%3A+%22xxxxxxxxxxx+%22%2C+%22Birthday%22%3A+%7B%22year%22%3A+2015%2C+%22month%22%3A+4%2C+%22day%22%3A+18%7D%2C+%22HiredOn%22%3A+%7B%22year%22%3A+2015%2C+%22month%22%3A+4%2C+%22day%22%3A+18%7D%2C+%22Position%22%3A+%22uuuuu%22%2C+%22Email%22%3A+%22vvvvv%40gmail.gmail%22%2C+%22PhoneNumber%22%3A+%22lllll%22%2C+%22IsManager%22%3A+true%2C+%22Team%22%3A+%7B%22Dev_team%22%3A+true%2C+%22Design_team%22%3A+true%2C+%22DevOps_team%22%3A+false%7D%7D http://127.0.0.1:8000/api/add

# How to run the project :  
	* create virtual env from terminal and activate it then install the requirements .
	* cd to where the manage.py where the manage.py exist :
	* type in terminal the command line : python3 manage.py runserver 
	* open the browser on : http://127.0.0.1:8000/  
	* to test the api of the project use the curl commands provided here in README.md .
	
# Notes : 
	* the connection of functionnalities betewen fronyt-end and backend they are not all implemented ,  
	but the api functionnalities are are all implemented . 
