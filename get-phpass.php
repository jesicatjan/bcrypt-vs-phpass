<?php
require_once 'PasswordHash.php';

$hasher = new PasswordHash(8, true);

function displayHashedPassword($password, $hasher) {
    echo "Password to hash: " . $password . PHP_EOL;
    $hash = $hasher->HashPassword($password);
    echo "Phpass hashed password: " . $hash . PHP_EOL . PHP_EOL;
}

displayHashedPassword('password', $hasher);
displayHashedPassword('jesicatjan', $hasher);
?>