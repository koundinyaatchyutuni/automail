<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $targetDirectory = "C:/Users/MY PC/OneDrive/Desktop/email/uploads/"; 
    $targetFile = $targetDirectory . basename($_FILES["excelFile"]["name"]);
    $uploadOk = 1;
    $fileType = strtolower(pathinfo($targetFile, PATHINFO_EXTENSION));

    // Check if file is an Excel file
    if ($fileType != "xlsx" && $fileType != "xls") {
        echo "Only Excel files are allowed.";
        $uploadOk = 0;
    }

    if ($uploadOk == 0) {
        echo "File was not uploaded.";
    } else {
        if (move_uploaded_file($_FILES["excelFile"]["tmp_name"], $targetFile)) {
            echo "File " . basename($_FILES["excelFile"]["name"]) . " has been uploaded.";
        } else {
            echo "There was an error uploading the file.";
        }
    }
}
?>
