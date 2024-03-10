<?php

$con= mysqli_connect('localhost','root','','crudoperation');
if($con){
    echo "connection successufully ";

}else{
    die(mysqli_error($con));
}
?>