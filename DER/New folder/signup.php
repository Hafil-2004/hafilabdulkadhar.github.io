<?php
$servername = "localhost";
$username = "root";  // Change if you have a different MySQL user
$password = "";      // Change to your MySQL password
$dbname = "user_db";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Handle POST request for signup
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $username = $_POST['signup-username'];
    $email = $_POST['signup-email'];
    $password = password_hash($_POST['signup-password'], PASSWORD_BCRYPT);

    // Check if username or email exists
    $checkQuery = $conn->prepare("SELECT * FROM users WHERE username = ? OR email = ?");
    $checkQuery->bind_param("ss", $username, $email);
    $checkQuery->execute();
    $result = $checkQuery->get_result();

    if ($result->num_rows > 0) {
        echo "Username or email already exists!";
    } else {
        // Insert new user
        $stmt = $conn->prepare("INSERT INTO users (username, email, password) VALUES (?, ?, ?)");
        $stmt->bind_param("sss", $username, $email, $password);
        $stmt->execute();
        echo "Signup successful! <a href='login.html'>Login</a>";
        $stmt->close();
    }

    $checkQuery->close();
}

$conn->close();
?>
