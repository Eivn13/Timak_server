<?php
// ini_set('display_errors', 1);
// ini_set('display_startup_errors', 1);
// error_reporting(E_ALL);

if (!empty($_POST["recognize"])) {
	$recognize = $_POST["recognize"];
	$output = shell_exec("python3 /var/www/html/Timak/testovaci.py '".$recognize."'");
	//$out_separe = explode(" ",$output);
	//echo $out_separe[1];
        echo $output;
	//echo "TU BY SI MAL DOSTAT MENO";
	//print_r($output);
        //echo $recognize;
}else{
	echo "Chyba: obrazok nebol odoslany";
}
?>
