# MD5
small md5 rainbow

## Preface

| scripts | description| 
| ------ | ------ |
| main.py | a simple python web script for MD5 search |
| md5.py | a script to create a small MD5 rainbow|
| md5.php | a simple php page for MD5 search |

| files | description| 
| ------ | ------ |
| dict | password dictionary |
| templates | html for python web |
| md5.db | sqlite3 database to store MD5 hash |

## Sample
### main.py

a simple python web script for MD5 search

	$ python3 main.py
	Calculating MD5...
	945783
	 * Serving Flask app "main" (lazy loading)
	 * Environment: production
	   WARNING: Do not use the development server in a production environment.
	   Use a production WSGI server instead.
	 * Debug mode: on
	 * Running on http://127.0.0.1:5050/ (Press CTRL+C to quit)
	 * Restarting with stat
	Calculating MD5...
	945783
	 * Debugger is active!
	 * Debugger PIN: 907-104-971

Now, you can access http://127.0.0.1:5050/ with your browser, try to search MD5 hash. Change the port you like in this script.

Note that, there are 945783 lines in two dict files. If you want to get more, just add your dictionary file in dict/ and add a line in main.py. 

	read_file('dict/your-dict.txt')
	
Do not worry about you may get the same password line, the script has already handle this. Just add a dictionary file.

### md5.py

a script to create a small MD5 rainbow and store MD5 hashes in md5.db

	$ python3 md5.py

md5.php : a simple php page for MD5 search, it will try to find where your input MD5 hash in md5.db . 

You need a web server, like apache to show it up. It's a bit annoying, that's why i write a python web script main.py .

md5.db : to create this md5.db

	$ sqlite3 md5.db

	CREATE TABLE MD5(
	   ID INT PRIMARY KEY     NOT NULL,
	   PASSWD           TEXT    NOT NULL,
	   PASSWD_MD5        CHAR(32)  NOT NULL
	);

Because 50M limits with Github, given md5.db just contains the lines with the first dictionary. 

	$ sqlite3 md5.db
	SQLite version 3.19.3 2017-06-08 14:26:16
	Enter ".help" for usage hints.
	sqlite> select count(*) from MD5;
	19957

Anyway, add your dictionary with read_file function.

	read_file('dict/your-dict.txt')
	
Have fun.
