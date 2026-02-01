<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (isset($_POST["name"]) && isset($_POST["email"]) && isset($_POST["password"])) {
        // Registration logic
        $name = $_POST['name'];
        $email = $_POST['email'];
        $password = $_POST['password'];

        // Hash the password (use a secure password hashing library like password_hash)
        $hashed_password = password_hash($password, PASSWORD_DEFAULT);

        $conn = new mysqli('localhost', 'root', '', 'logindetails');
        if ($conn->connect_error) {
            die('Connection Failed : ' . $conn->connect_error);
        }

        $stmt = $conn->prepare("INSERT INTO users (name, email, password) VALUES (?, ?, ?)");
        if (!$stmt) {
            die('Prepare Failed : ' . $conn->error);
        }

        $stmt->bind_param("sss", $name, $email, $password);
        if (!$stmt->execute()) {
            die('Execute Failed : ' . $stmt->error);
        }

        $stmt->close();
        $conn->close();

        // Registration successful, redirect to login page
        header("Location: loginpage.html");
        exit;
    } 
} 
    $email = $_POST["email"];
    $password = $_POST["password"];
    
    // Database connection
    $con = new mysqli("localhost","root","","logindetails");
    if($con->connect_error) {
        die("Failed to connect :".$con->connect_error);
    }else{
        $stmt = $con->prepare("select * from users where email = ?");
        $stmt->bind_param("s", $email);
        $stmt->execute();
        $stmt_result = $stmt->get_result();
        if($stmt_result->num_rows > 0){
            $data = $stmt_result->fetch_assoc();
            if($data['password'] === $password){
                echo"<h2>Login Successful</h2>";
                header("Location: veh_reg.html");
        exit;
            }else{
                echo "<h2>Invalid Email or Password</h2>";
            }

        } else {
            echo "<h2>Invalid Email or Password</h2>";
        }
    }
?>