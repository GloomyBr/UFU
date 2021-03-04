<!doctype html>
<html lang="pt-BR">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-CuOF+2SnTUfTwSZjCXf01h7uYhfOBuxIhGKPbfEJ3+FqH/s6cIFN9bGr1HmAg4fQ" crossorigin="anonymous">
    <title>Exercicio2</title>
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
    </style>
  </head>
  <body>
      <div class="container">
        <main>
        <table class="table table-striped">
                  <thead>
                    <tr>
                      <th scope="col">Nº</th>
                      <th scope="col">Produto</th>
                      <th scope="col">Descrição</th>
                    </tr>
                  </thead>
                  <tbody>
                    <?php
                    $qde = $_GET["qde"];
                    $qde = htmlspecialchars($qde);
                    $produtos[0] = 'Sabonete';
                    $produtos[1] = 'Desodorante';
                    $produtos[2] = 'Creme dental';
                    $produtos[3] = 'Escova de dente';
                    $produtos[4] = 'Pomada';
                    $produtos[5] = 'Shampoo';
                    $produtos[6] = 'Bucha';
                    $produtos[7] = 'Condicionador';
                    $produtos[8] = 'Minancora';
                    $produtos[9] = 'Papel Higiênico';
                  
                    $descricao[0] = 'Para te deixar cheirosinho';
                    $descricao[1] = 'Para não deixar dar catinga no subaco';
                    $descricao[2] = 'Para tirar o bafo de onça';
                    $descricao[3] = 'Para deixar os dentes branquinhos';
                    $descricao[4] = 'Para deixar o cabelinho na régua';
                    $descricao[5] = 'Para lavar o cabelo ensebado';
                    $descricao[6] = 'Para tirar os macuco do corpo';
                    $descricao[7] = 'Para deixar o cabelinho maciozinho';
                    $descricao[8] = 'Para matar as frieira e qualquer outro tipo de fungo, também mata muitas bactérias';
                    $descricao[9] = 'Para limpar o bumbumzinho';
                    for ($i = 0; $i < $qde; $i++) {
                      $r1 = rand(0,9);
                      echo <<<HTML
                      <tr>
                        <th scope="row">$i</th>
                        <td>$produtos[$r1]</td>
                        <td>$descricao[$r1]</td>
                      </tr>
                      HTML;
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