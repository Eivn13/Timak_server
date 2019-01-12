<?php
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);

if (!empty($_POST["recognize"])) {
	$recognize = $_POST["recognize"];
	$output = shell_exec("python3 /var/www/html/Timak/testovaci.py ".$recognize);
	echo $output;
}else{
	echo "Chyba: obrazok nebol odoslany";
}
?>