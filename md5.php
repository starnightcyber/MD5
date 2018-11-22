<html>
<head>
	<meta http-equiv='Content-Type' content='text/html; charset=utf-8' /> 
	<title>MD5查询</title>
</head>
<body>
<br />
<br />
<br />
<br />
<br />
<br />
<br />
<h1 align="center">MD5查询</h1>
<br />
<form action="" method="post">
<div align="center">
<input type="text" id="hash" name="hash" style="width:600px;height:30px"/>
<input type="submit" value="查询">
</div>
</form>
<?php

   header("Content-type:text/html;charset=utf-8");  

   class SQLiteDB extends SQLite3
   {
      function __construct()
      {
         $this->open('md5.db');
      }
   }
   $db = new SQLiteDB();
   if(!$db){
      echo $db->lastErrorMsg();
   } else {
      # echo "Yes, Opened database successfully\n";
   }

   if(!empty($_POST)) {$hash = $_POST["hash"];}
   
   if(empty($hash))
   {
	   echo "<script>alert('please input md5');</script>"; 
	}
	$sql = 'SELECT PASSWD FROM MD5 where PASSWD_MD5="'.$hash.'"';
	#echo  "<h5 align='center'>".$sql."</h5>"."<br />";

    $results = $db->query($sql);
	
	echo "<h5 align='center'>".$hash."</h5>";

	while ($row = $results->fetchArray()) {
	    # echo "<h5 align='center'>".$hash.":".$row[0]."</h5>";
	    echo "<h5 align='center'>".$row[0]."</h5>";
	}

?>

</body>
</html>
