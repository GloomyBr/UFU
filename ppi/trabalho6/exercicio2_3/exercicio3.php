<?php

require "conexaoMysql.php";
$pdo = mysqlConnect();

try {

  $sql = <<<SQL
  SELECT *
  FROM base_enderecos_ajax
  SQL;

  // Neste exemplo não é necessário utilizar prepared statements
  // porque não há possibilidade de injeção de SQL, 
  // pois nenhum parâmetro é utilizado na query SQL
  $stmt = $pdo->query($sql);
} catch (Exception $e) {
  exit('Ocorreu uma falha: ' . $e->getMessage());
}
?>

<!doctype html>
<html lang="pt-BR">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-CuOF+2SnTUfTwSZjCXf01h7uYhfOBuxIhGKPbfEJ3+FqH/s6cIFN9bGr1HmAg4fQ" crossorigin="anonymous">
    <title>Exercicio3</title>
    <style>
         main {
            margin: 0 auto;
            background-color: white;
            padding: 2% 4%;
            width: 100%;
            margin-top: 10px;
        }
        body {
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            line-height: 1.5rem;
            margin: 0;
        }
        .col-sm{
          border: 0.5px solid #ddd;
          border-radius: 4px;
          text-align: center;
        }
    </style>
  </head>
  <body>
      <div class="container">
        <main>
            <div class="row">
            <table class="table table-striped">
                  <thead>
                    <tr>
                      <th scope="col">#</th>
                      <th scope="col">Cep</th>
                      <th scope="col">Logradouro</th>
                      <th scope="col">Bairro</th>
                      <th scope="col">Cidade</th>
                      <th scope="col">Estado</th>
                    </tr>
                  </thead>
                  <tbody>
                  <?php
                      $count = 0;
                      while ($row = $stmt->fetch()) {
                        $cep = $row["cep"];
                        $logradouro = $row["logradouro"];
                        $bairro = $row["bairro"];
                        $cidade = $row["cidade"];
                        $estado = $row["estado"];

                        echo <<<HTML
                        <tr>
                          <th scope="row">$count</th>
                          <td>$cep</td>
                          <td>$logradouro</td>
                          <td>$bairro</td>
                          <td>$cidade</td>
                          <td>$estado</td>
                        </tr>
                        HTML;
                        $count++;
                    }
                  ?>
                  </tbody>
             </table>
            </div>
        </main>
      </div>
          <!-- Option 1: Bootstrap Bundle with Popper.js -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-popRpmFF9JQgExhfw5tZT4I9/CI5e2QcuUZPOVXb1m7qUmeR2b50u+YFEYe1wgzy" crossorigin="anonymous"></script>
  </body>
</html>