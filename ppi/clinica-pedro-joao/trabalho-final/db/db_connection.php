 <?php
  $db_host = "fdb30.awardspace.net";
  $db_username = "3634411_trabalho6";
  $db_password = "N8rW5dEe8VF6!N_e";
  $db_name = "3634411_trabalho6";
  $dsn = "mysql:host=$db_host;dbname=$db_name;charset=utf8mb4";

  $options = [
    PDO::ATTR_EMULATE_PREPARES => false,
    PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
    PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC,
  ];
  
  try {
    $pdo = new PDO($dsn, $db_username, $db_password, $options);
  }
  catch (Exception $e) {
    exit('Falha na conexão com o MySQL: ' . $e->getMessage());
  }
?>
