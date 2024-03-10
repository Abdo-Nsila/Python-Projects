<?php
        if(isset($_POST['sub'])){
            $first_name=$_POST['first_name'];
            $last_name=$_POST['last_name'];
            $login=$_POST['login'];
            $password=$_POST['password'];
            $cpassword=$_POST['cpassword'];

            if (empty($first_name)){
                $error_msg['first_name']="name empty";
            }
            else if (empty($last_name)){
                $error_msg['last_name']="prenom empty";
            }
            else if (empty($login)){
                $error_msg['login']="login empty";
            }   
            else if (empty($password)){
                $error_msg['password']="password empty";
            }
            else if (empty($cpassword)){
                $error_msg['cpassword']="CONFIRME LE MOT DE PASS";
            }
            if($password!=$cpassword){
                $error_msg['pass']="PASSWORD DON'T MATCH";
            }

            include 'connect.php';
        }

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- <link rel="stylesheet" href="sign_in.css"> -->
    <link rel="stylesheet" href="bootstrap.min.css">
    <title>SIGN IN</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark text-white d-flex justify-content-between">
        <h1 class="navbar-brand">SIGN IN</h1>
        <a href="login1.php" class="navbar-brand bg-light text-dark rounded" >LOGIN</a>
    </nav>
    <div class="error_msg text-danger d-flex justify-content-center border">
            <?php
                if(isset($error_msg['first_name'])){
                    echo $error_msg['first_name'].'<br>';
                }
                if(isset($error_msg['last_name'])){
                    echo $error_msg['last_name'].'<br>';
                }
                if(isset($error_msg['login'])){
                    echo $error_msg['login'].'<br>';
                }
                if(isset($error_msg['password'])){
                    echo $error_msg['password'];
                }
                if(isset($error_msg['cpassword'])){
                    echo $error_msg['cpassword'].'<br>';
                }
                if(isset($error_msg['pass'])){
                    echo $error_msg['pass'].'<br>';
                }
            ?>
        </div>

    <div class="d-flex justify-content-center ">

    <form action="" method="post" enctype="multipart/form-data" class="form-group w-25 p-3 m-5 d-flex flex-column ">

        <label for="first_name">NOM</label>
        <input type="text" id="first_name" name="first_name" class="form-control">

        <label for="last_name">PRENOM</label>
        <input type="text" id="last_name" name="last_name" class="form-control">

        <label for="login">LOGIN</label>
        <input type="email" id="login" name="login" class="form-control">

        <label for="password">MOT DE PASS</label>
        <input type="password" id="password" name="password" class="form-control">

        <label for="cpassword">CONFIRME LE MOT DE PASS</label>
        <input type="password" id="cpassword" name="cpassword" class="form-control">
        <br>
        <input type="submit" name="sub" class="btn btn-primary">
    </form>
    <?php

        if(isset($_POST['sub'])){
            extract($_POST);
    
            mysqli_query($connect,"INSERT INTO `ofppt` VALUES ('','$first_name','$last_name','$login','$password')");
            header("location: login1.php");
            mysqli_close($connect);
        }   
    
    ?>
</div>
</body>
</html>