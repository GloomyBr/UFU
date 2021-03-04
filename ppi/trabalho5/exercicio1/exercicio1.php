<!doctype html>
<html lang="pt-BR">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-CuOF+2SnTUfTwSZjCXf01h7uYhfOBuxIhGKPbfEJ3+FqH/s6cIFN9bGr1HmAg4fQ" crossorigin="anonymous">
    <title>Exercicio1</title>
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
                <?php
                  $cep = $_POST["cep"];
                  $logradouro = $_POST["logradouro"];
                  $bairro = $_POST["bairro"];
                  $cidade = $_POST["cidade"];
                  $estado = $_POST["estado"];

                  $cep = htmlspecialchars($cep);
                  $logradouro = htmlspecialchars($logradouro);
                  $bairro = htmlspecialchars($bairro);
                  $cidade = htmlspecialchars($cidade);
                  $estado = htmlspecialchars($estado);
                  echo <<<HTML
                  <div class="col-sm">
                  $cep
                  </div>
                  <div class="col-sm">
                  $logradouro
                  </div>
                  <div class="col-sm">
                  $bairro
                  </div>
                  <div class="col-sm">
                  $cidade
                  </div>
                  <div class="col-sm">
                  $estado
                  </div>
                  HTML;
                ?>
            </div>
        </main>
      </div>
          <!-- Option 1: Bootstrap Bundle with Popper.js -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-popRpmFF9JQgExhfw5tZT4I9/CI5e2QcuUZPOVXb1m7qUmeR2b50u+YFEYe1wgzy" crossorigin="anonymous"></script>
  </body>
</html>