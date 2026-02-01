<?php
$vehicleType = $_POST['vehicleType'];
$vehicleName = $_POST['vehicleName'];
$licensePlate = $_POST['licensePlate'];
$contactName = $_POST['contactName'];
$phoneNumber = $_POST['phoneNumber'];

$conn = new mysqli('localhost', 'root', '', 'vehicledetails');
if ($conn->connect_error) {
    die('Connection Failed: ' . $conn->connect_error);
} else {
    // Check if the entry already exists in the database based on the phone number
    $checkQuery = "SELECT * FROM vehicledatabase WHERE phoneNumber = ?";
    $checkStmt = $conn->prepare($checkQuery);
    $checkStmt->bind_param("s", $phoneNumber);
    $checkStmt->execute();
    $result = $checkStmt->get_result();
    
    if ($result->num_rows > 0) {
        echo "Registration Failed: This phone number is already registered.";
    } else {
        // Phone number is not found, proceed with registration
        $stmt = $conn->prepare("INSERT INTO vehicledatabase (vehicleType, vehicleName, licensePlate, contactName, phoneNumber)
            VALUES (?, ?, ?, ?, ?)");
        $stmt->bind_param("sssss", $vehicleType, $vehicleName, $licensePlate, $contactName, $phoneNumber);
        $stmt->execute();
    
    // Redirect to the next page
    header("Location: success.php");
    exit();

$stmt->close();
}

$checkStmt->close();
$conn->close();
}
?>

