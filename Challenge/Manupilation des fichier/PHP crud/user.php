<?php
include 'connection.php';
 if(isset($_POST['submit'])){
    $name=$_POST['name'];
    $email=$_POST['email'];
    $mobile=$_POST['mobile'];
    $password=$_POST['password'];

    $sql="insert into `crud` (name ,email,mobile,password) values('$name','$email','$mobile','$password')";
    $result=mysqli_query($con,$sql);
    if($result){
        echo "data inserted successfully ";
    }else{
        die(mysqli_error($con));
    }
}
?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="bootstrap-5.0.2-dist/css/bootstrap.min.css">
    <title>Document</title>
</head>
<body>
<div class="container">
    <form methode="post" action="user.php">
        <div class="groupe">
        <label style="font-weight: bold;">id</label>
        <input type="text" name="id" autocomplete="off" placeholder="id" class="form-control w-50 "><br><br>
        <label style="font-weight: bold;">Name</label>
        <input type="text"  name="name" autocomplete="off" placeholder="Name" class="form-control w-50"><br><br>
        <label style="font-weight: bold;">Email</label>
        <input type="email" name="email"  placeholder="EMAIL" class="form-control w-50 "><br><br>
        <label style="font-weight: bold;">Mobile</label>
        <input type="text"  name="mobile" autocomplete="off" placeholder="Mobile" class="form-control w-50"><br><br>
        <label style="font-weight: bold;">Password</label>
        <input type="password" autocomplete="off" placeholder=" Password" class="form-control w-50"><br><br>

        <button style="font-weight: bold;" type="submit" name="submit" class="btn btn-primary">Submit</button>
      </div>
    </form>
</div>
</body>
</html>