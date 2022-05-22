from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy import Column , ForeignKey , create_engine
from sqlalchemy.types import Integer, Text, String , DateTime , Boolean ,ARRAY
from sqlalchemy.sql import func
from sqlalchemy.orm import sessionmaker
import datetime 
import os



BASE_DIR=os.path.dirname(os.path.realpath(__file__))
connection_string="sqlite:///"+os.path.join(BASE_DIR,'site.db')
Base=declarative_base()
engine=create_engine(connection_string,echo=False)
Session = sessionmaker(bind = engine)



class Employee(Base) :
	__tablename__ = "Employees"
	id = Column(Integer, primary_key=True, autoincrement="auto")
	Name = Column(String(300) , nullable=False)
	Birthday = Column(DateTime, nullable=False)
	HiredOn = Column(DateTime, nullable=False , default= datetime.datetime.utcnow() )
	Position = Column(String(300) , nullable=False)
	Email = Column(String(100) , nullable=False) 
	PhoneNumber = Column(String(100) , nullable=False) 
	# true = is Manager , false = not Manager 
	IsManager =  Column(Boolean , nullable=False) 
	# maxuimum teams diffrent type are 21 
	Team = Column(String(53) , nullable=False) 

	def __repr__(self) : 
		return f"""<Employee Name="{self.Name}",Birthday="{str(self.Birthday)}",HiredOn="{str(self.HiredOn)}",Position="{self.Position}",Email="{self.Email}",PhoneNumber="{self.PhoneNumber}",IsManager={self.IsManager},Team="{ self.Team }">"""

	def update(self, kwargs):
		status = True
		for key, value in kwargs.items():
			if hasattr(self, key):
				try : 
					if key == "Birthday" or key == "HiredOn" : 
						setattr(self, key, datetime.datetime(value["year"], value["month"],value["day"], 0, 0, 0, 0))
					elif key == "Team" : 
						if kwargs["IsManager"] == 1 or  kwargs["IsManager"] == True : 
							setattr(self, key,"-".join([value[i] for i in ["Dev_team" , "Design_team" , "DevOps_team" ]]))
					elif key == "IsManager" : 
						setattr(self, key,1 if value else 0 )
					else : 
						setattr(self, key,value ) 
				except Exception as e  : 
					print(e)
					return False 
			else : 
				return False 
		return True

	def as_dict_response(self) : 
		itm = {c.name: getattr(self, c.name) for c in self.__table__.columns}
		itm["HiredOn"] = {"year" : itm["HiredOn"].year  , "month" :  itm["HiredOn"].month , "day" : itm["HiredOn"].day}
		itm["Birthday"] = {"year" : itm["Birthday"].year  , "month" :  itm["Birthday"].month , "day" : itm["Birthday"].day}
		itm["Team"] = "-" + str(itm["Team"]) + "-"
		itm["Team"] = {"Dev_team" : "-1-" in itm["Team"] , "Design_team" : "-2-" in itm["Team"]  , "DevOps_team" : "-3-" in itm["Team"]  }
		return itm 

	def from_json_request(self,js) : 
		self.Name = js.get("Name")
		self.Birthday = datetime.datetime(js.get("Birthday").get("year"), js.get("Birthday").get("month"),js.get("Birthday").get("day"), 0, 0, 0, 0)
		self.HiredOn = datetime.datetime(js.get("HiredOn").get("year"), js.get("HiredOn").get("month"),js.get("HiredOn").get("day"), 0, 0, 0, 0)
		self.Position = js.get("Position")
		self.Email = js.get("Email")
		self.PhoneNumber = js.get("PhoneNumber")
		self.IsManager = js.get("IsManager")
		if self.IsManager : 
			self.Team = "-".join([ {'Dev_team': "1", 'Design_team': "2", 'DevOps_team': "3"}[k]  for k , v  in js["Team"].items() if v ])
		else : 
			self.Team = ""


if __name__ == '__main__':
	Base.metadata.create_all(engine)
	with Session() as session:
		false , true = False , True
		for i in range(20) : 
			v = {"Name": str(i) * 6 , "Birthday": {"year": 2015, "month": 4, "day": 18}, "HiredOn": {"year": 2015, "month": 4, "day": 18}, 
			"Position": "Position" + str(i), "Email":( str(i) * 5 )+ "@gmail.gmail", "PhoneNumber": "216" + str(i) * 5 , "IsManager": false,
			 "Team": {"Dev_team": true, "Design_team": true, "DevOps_team": false}}
			e = Employee()
			e.from_json_request(v)
			session.add(e)
			session.commit()





