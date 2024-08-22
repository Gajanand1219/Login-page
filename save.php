<?php
$server = "localhost";
$username = "root";
$password = "";
$dbname = "camera";

$con = mysqli_connect($server, $username, $password, $dbname);

if (!$con) {
    echo "not connect";
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // if(isset($_post['']))
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $city  = $_POST['city'];
    $password  = $_POST['password'];

    $sql = "INSERT INTO `loginform`(`name`, `email`, `phone`, `city`, `password`) VALUES ('$name','$email','$phone','$city','$password')";

    if (mysqli_query($con, $sql)) {
        echo "Data submitted successfully";
    }
}

mysqli_close($con);
?>
