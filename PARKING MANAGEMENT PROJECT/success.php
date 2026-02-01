<!DOCTYPE html>
<html>
<head>
    <title>Registration Success<br></title>
    <style>
        body {
	
	background: #a8dddc;
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
	font-family: 'Montserrat', sans-serif;
	height: 100vh;
	margin: -20px 0 50px;
    
}
h1 {
	font-weight: bold;
	margin: 0;
    color: #009688;
}
p{
    font-weight: bold;
	margin: 0;
    color: #009688;
}
h2 {
    font-weight: bold;
	margin: 0;
    color: #009688;
}
        table {
            border-collapse: collapse;
            width: 80%;
            margin: 20px auto;
            table-layout: auto;
            color: #009688;
            background-color: rgba(0,0,0,0.22);
        }

        th, td {
            border: 1px solid #ccc;
            padding: 8px;
            text-align: left;
            color: #009688
        }

        th {
            background-color: #f2f2f2;
            color: #009688
        }

        .banner{
    width: 100%;
    height: 100vh;
    background-image: linear-gradient(rgba(0,0,0,0.75),rgba(0,0,0,0.75)),url(background.jpeg);
    background-size: cover;
    background-position: center;
}
.navbar{
    width: 50%;
    margin: auto;
    padding: 100px 0;
    display: auto;
    align-items: center;
	text-align: center;
    justify-content: space-between;
}

footer {
    background-color: rgba(0,0,0,0.6);;
    color: #fff;
    font-size: 14px;
    bottom: 0;
    position: fixed;
    left: 0;
    right: 0;
    text-align: center;
    z-index: 999;
}

footer p {
    margin: 10px 0;
}

footer i {
    color: red;
}

footer a {
    color: #3c97bf;
    text-decoration: none;
}
    </style>
</head>
<body>
<div class="banner">
		<div class="navbar">
      
    <h1>Successfully Registered</h1>
    
    <?php
    $conn = new mysqli('localhost', 'root', '', 'vehicledetails');
    
    if ($conn->connect_error) {
        die('Connection Failed : ' . $conn->connect_error);
    } else {
        // Count the number of registered vehicles
        $sql = "SELECT COUNT(*) AS vehicleCount FROM vehicledatabase";
        $result = $conn->query($sql);
        
        if ($result->num_rows > 0) {
            $row = $result->fetch_assoc();
            $vehicleCount = $row['vehicleCount'];
            $spacesLeft = 50 - $vehicleCount;
            
            echo "<p>No. of Vehicles registered: $vehicleCount</p>";
            echo "<p>No. of Spaces Left out of 50: $spacesLeft</p>";
            
            // Display the list of registered vehicles in a table
            $sql = "SELECT * FROM vehicledatabase";
            $result = $conn->query($sql);
            
            if ($result->num_rows > 0) {
                echo "<h2>List of Registered Vehicles</h2>";
                echo "<table>";
                echo "<tr><th>Vehicle Type</th><th>Vehicle Name</th><th>License Plate</th><th>Contact Name</th><th>Phone Number</th></tr>";
                
                while ($row = $result->fetch_assoc()) {
                    echo "<tr>";
                    echo "<td>" . $row['vehicleType'] . "</td>";
                    echo "<td>" . $row['vehicleName'] . "</td>";
                    echo "<td>" . $row['licensePlate'] . "</td>";
                    echo "<td>" . $row['contactName'] . "</td>";
                    echo "<td>" . $row['phoneNumber'] . "</td>";
                    echo "</tr>";
                }
                
                echo "</table>";
            } else {
                echo "No data available";
            }
        } else {
            echo "No data available";
        }
        
        $conn->close();
    }
    ?>
    <footer>
	<p>
		©Parking Management System by SKASC
	</p>
</footer>
</body>
</html>
