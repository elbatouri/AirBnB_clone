# AirBnB_clone
my version
This is the first step of making a clone of Airbnb

-for to start you should analyse the AirBnb website app : 
- the user should be able to create an account
	- what are the field we need : 
		- unique identifier
		- name
		- email
		- creation date
		- update Date
	- the Review part : 
		- unique identifier
		- update date
		- creation date
	- The place: 
		- unique identifier
		- update date
		- creation date
	- the amenities : "confort plus":
		- fields : quantity,
		- classes (attributes and methods to structure a way how an amenity instance of the class will be created)
		- CRUD :
			- C : CREAT
			- R: READ
			- U: UPDATE
			- D: DELETE
		- for to do that we need to work on methods for to can crate, read, update or delete from and to our database.
		- since theres is a cummon attributes and methodes between all classes we lle be :
			- creating a BaseModel() in witch we ll : 
					# define all commun attributes
					#define all commun methods:
			- Create User(BaseModel):
					#inherits the base classes attributes
					#inherits all the base class Methods
					#declare the unique attributes
					#declare the unique methods
			- Create Amenities(BaseModel)
					#Create attributes.
		After creation all the classes with the attributes and methods you ll have to : 
		
			- because everything in python is an object you ll have to prepare the data for the storage : 
				- we   to convert the object into a JSON string format ( serialization )
				- and also the conversion from JSON back to object ( deserialization )
			- to do that we have to create :
				- FileStorage() class with : 
						# attributes related to file
						# methods of  serialization and deserialization
						
				

-implementation phase :
- Fronend
	- Console ( cmd module).
- Backend:
	- OOP : 
		- building classes.
		- creating méthodes
		- calling methods
		- class attributes.
	- DATABASE: 
		- FILE STORAGE :   
		- JSON Model
-testing phase :
	- Unitest Model
	
