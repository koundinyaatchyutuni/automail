<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Handle uploaded Excel file
    if ($_FILES["excelFile"]["error"] == UPLOAD_ERR_OK) {
        $excelFilePath = "uploads/" . $_FILES["excelFile"]["name"];
        move_uploaded_file($_FILES["excelFile"]["tmp_name"], $excelFilePath);
        echo "Excel file uploaded successfully.<br>";
    }

    // Handle uploaded CSS file
    if ($_FILES["cssFile"]["error"] == UPLOAD_ERR_OK) {
        $cssFilePath = "uploads/" . $_FILES["cssFile"]["name"];
        move_uploaded_file($_FILES["cssFile"]["tmp_name"], $cssFilePath);
        echo "CSS file uploaded successfully.<br>";
    }
}
?>
