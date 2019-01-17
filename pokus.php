<?php
$image = '/var/www/html/Timak/some_image.jpg';

//# check whether CNN is not busy, because when it is not, the picture will be deleted
//if(file_exists($image)){
//    //echo "Busy";
//    exit("Busy");
//}

if(!empty($_POST["name"]) && !empty($_POST["image"])) {

    # save picture
    file_put_contents('/var/www/html/Timak/some_image.jpg', base64_decode($_POST["image"]));

    # let python do the talking
    $output = shell_exec("python3 /var/www/html/Timak/add_person.py " . $_POST["name"]. " 2>/dev/null");
    echo $output;
}


// ---- SQL -----
//include_once './config.php';
//// Create connection
//
//$myfile = fopen("info.txt", "w") or die("Unable to open file!");
//$conn = mysqli_connect($servername, $username, $password, $dbname);
//
//// Check connection
//if ($conn->connect_error) {
//	$txt="nepripojena databaza !!!";
//    fwrite($myfile, $txt);
//
//    die("Connection failed: " . $conn->connect_error);
//} else {
//	$txt="pripojena databaza !!!";
//    fwrite($myfile, $txt);
//}
//
//if(!empty($_POST["name"]) && !empty($_POST["image"])){
//	$name = $_POST["name"];
//	$image = $_POST["image"];
//	$arr = array("name" => $name);
//
//	//file_put_contents('img.jpg', base64_decode($image));
//
//	$sqlcount="SELECT * FROM users WHERE name='$name'";
//	$result = $conn->query($sqlcount);
//	//echo $result->num_rows;
//	if ($result->num_rows==0) {
//		echo "meno ".$name." nie je v databaze !!!";
//		$sql_name = "INSERT INTO users (name) VALUES ('$name')";
//		if ($conn->query($sql_name) === TRUE) {
//			echo "hodnota name bola vlozena !!!";
//			$txt="hodnota name bola vlozena !!!";
//    		fwrite($myfile, $txt);
//		}
//	}else{
//		echo "meno ".$name." uz je v databaze !!!";
//	}
//
//	$sql_img = "INSERT INTO faces (img)
//	VALUES ('$image')";
//	if ($conn->query($sql_img) === TRUE) {
//    	echo "New record created successfully";
//    	$txt="hodnota img bola vlozena !!!";
//    	fwrite($myfile, $txt);
//	} else {
//    	echo "Error: " . $sql_img . "<br>" . $conn->error;
//    	$txt="hodnota img nebola vlozena !!!";
//    	fwrite($myfile, $txt);
//	}
//
//	$sql_user_img = "INSERT INTO user_images (UserID, FaceID)
//	SELECT u.id, f.id
//	FROM users u,faces f
//	WHERE u.name = '$name'
//	AND f.img = '$image'";
//	if ($conn->query($sql_user_img) === TRUE) {
//    	echo "New record created successfully";
//    	$txt="hodnota id img bola vlozena !!!";
//    	fwrite($myfile, $txt);
//	} else {
//    	echo "Error: " . $sql_user_img . "<br>" . $conn->error;
//    	$txt="hodnota id img nebola vlozena !!!";
//    	fwrite($myfile, $txt);
//	}
//
//	//echo json_encode($arr,JSON_PRETTY_PRINT);
//	echo "Fotografia bolo uložená do databázy";
//}else if(!empty($_POST["start"])){
//	if($_POST["start"] == true){
//		$output = shell_exec("python3 /var/www/html/Timak/ttt.py");
//		echo $output;
//	}
//}
//fclose($myfile);
//$conn->close();