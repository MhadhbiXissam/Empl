

def update_itm_response(itm) : 
	itm["HiredOn"] = itm["HiredOn"].split()[0]
	itm["Birthday"] = itm["HiredOn"].split()[0]
	itm["IsManager"] = True if itm["IsManager"] == "True" else False
	itm["Team"] = [ int(i) for i in itm["Team"].split("-")] 
	return itm 

if __name__ == '__main__':
	x = [{'id': '104', 'Name': 'sdfsdfsdf', 'Birthday': '2015-04-18 00:00:00', 'HiredOn': '2015-04-18 00:00:00', 'Position': 'Justice league', 'Email': 'darkside@gmail.gmail', 'PhoneNumber': '21625881317', 'IsManager': 'False',
	 'Team': ''}]
	map(update_itm_response,x)
	x = {'Dev_team': True, 'Design_team': True, 'DevOps_team': False}
	print([ {'Dev_team': True, 'Design_team': True, 'DevOps_team': False}[k]  for k , v  in x.items() if v ])