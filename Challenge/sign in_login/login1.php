<?php
        if(isset($_POST['sub'])){
            $login=$_POST['login'];
            $password=$_POST['password'];

            if (empty($login)){
                $error_msg['login']="login empty";
            }

            if (empty($password)){
                $error_msg['password']="password empty";
            }
        }
        if(empty($error_msg)) {
        include 'connect.php';
            // $login=stripcslashes($login);
    // $password=stripcslashes($password);

    // $login=mysqli_real_escape_string($connect,$login);
    // $password=mysqli_real_escape_string($connect,$password);

    if(isset($_POST['sub'])){
        $login=$_POST['login'];
        $password=$_POST['password'];
    $data=mysqli_query($connect,"SELECT * FROM ofppt WHERE email='$login' && pass='$password' ");
    $row=mysqli_fetch_array($data);

    if(isset($row) && $row['email']==$login && $row['pass']==$password){
        echo 'welcome '.$row['first_name'] .' ' .$row['last_name'];

    }

    else{
        die('error: Invalid login credentials');
    }    
}
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="bootstrap.min.css">

    <title>login</title>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark text-white d-flex justify-content-between">
        <h1 class="navbar-brand">LOGIN</h1>
        <a href="sign_in1.php" class="navbar-brand bg-light text-dark rounded" >SIGN IN</a>
    </nav>

    <div class="error_msg text-danger d-flex justify-content-center border">
            <?php
                if(isset($error_msg['login'])){
                    echo $error_msg['login'].'<br>';
                }
                if(isset($error_msg['password'])){
                    echo $error_msg['password'];
                }
            ?>
        </div>

    <div class="d-flex justify-content-center ">
        
    <form action="" method="post" enctype="multipart/form-data" class="form-group w-25 p-3 m-5 d-flex flex-column ">
        

        <label for="login">LOGIN</label>
        <input type="email" id="login" name="login" class="form-control">

        <label for="password">MOT DE PASS</label>
        <input type="password" id="password" name="password" class="form-control">
        <br>

        <input type="submit" name='sub'>

    </form>

    </div>

</body>
</html>