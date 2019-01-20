<?php

if(!empty($_POST["start"])){
    $output = shell_exec("python3 /var/www/html/Timak/train.py");
    echo $output;
}