<?php

require "conexaoMysql.php";
$pdo = mysqlConnect();

$nome = $cpf = $email = $senha = "";
$datanascimento = $estadocivil = $altura = "";

if (isset($_POST["cep"])) $cep = htmlspecialchars($_POST["cep"]);
if (isset($_POST["logradouro"])) $logradouro = htmlspecialchars($_POST["logradouro"]);
if (isset($_POST["bairro"])) $bairro = htmlspecialchars($_POST["bairro"]);
if (isset($_POST["cidade"])) $cidade = htmlspecialchars($_POST["cidade"]);
if (isset($_POST["estado"])) $estado = htmlspecialchars($_POST["estado"]);


try {

  $sql = <<<SQL
  -- Repare que a coluna Id foi omitida por ser auto_increment
  INSERT INTO base_enderecos_ajax (cep, logradouro, bairro, cidade, 
                       estado)
  VALUES (?, ?, ?, ?, ?)
  SQL;

  // Neste caso utilize prepared statements para prevenir
  // ataques do tipo SQL Injection, pois precisamos
  // cadastrar dados fornecidos pelo usuário 
  $stmt = $pdo->prepare($sql);
  $stmt->execute([
    $cep, $logradouro, $bairro, $cidade,
    $estado
  ]);

  header("location: index.html");
  exit();
} 
catch (Exception $e) {  
  //error_log($e->getMessage(), 3, 'log.php');
  if ($e->errorInfo[1] === 1062)
    exit('Dados duplicados: ' . $e->getMessage());
  else
    exit('Falha ao cadastrar os dados: ' . $e->getMessage());
}
