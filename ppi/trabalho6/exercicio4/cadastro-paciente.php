<?php
  require "conexaoMysql.php";
  $pdo = mysqlConnect();

  $nome = $_POST["nome"];
  $email = $_POST["email"];
  $telefone = $_POST["telefone"];
  $cep = $_POST["cep"];
  $logradouro = $_POST["logradouro"];
  $bairro = $_POST["bairro"];
  $cidade = $_POST["cidade"];
  $estado = $_POST["estado"];
  $peso = $_POST["peso"];
  $altura = $_POST["altura"];
  $tipo_sanguineo = $_POST["tipo_sanguineo"];

  try {
    $sql_pessoa = <<<SQL
    INSERT INTO pessoa (nome, email, telefone, cep, logradouro, bairro, cidade, estado)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    SQL;
    
    $sql_paciente = <<<SQL
    INSERT INTO paciente (peso, altura, tipo_sanguineo, codigo)
    VALUES (?, ?, ?, ?)
    SQL;

    $pdo->beginTransaction();

    $stmt_pessoa = $pdo->prepare($sql_pessoa);
    if(!$stmt_pessoa->execute([$nome, $email, $telefone, $cep, $logradouro, $bairro, $cidade, $estado])) {
      throw new Exception('Falha ao cadastrar pessoa');
    }

    $lastId = $pdo->lastInsertId();
    $stmt_paciente = $pdo->prepare($sql_paciente);
    if(!$stmt_paciente->execute([$peso, $altura, $tipo_sanguineo, $lastId])) {
      throw new Exception('Falha ao cadastrar paciente');
    }
    
    $pdo->commit();
    header("location: index.html");
  } catch (Exception $e) {
    $pdo->rollBack();
    exit('Falha ao cadastrar os dados: ' . $e->getMessage());
  }
?>