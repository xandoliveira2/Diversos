<?php
// Inclui o arquivo que contém a definição da classe Aluno e Turma
require_once "../../classes/Turma.php";
/*******MUNDANÇA DE CAMINHO*****/
$turma = new Turma();
$lista = $turma->listar();

require_once "../../classes/Aluno.php";
/*******MUNDANÇA DE CAMINHO*****/

// Obtém o valor do parâmetro "id" passado na URL via método GET
$id = $_GET['id'];

// Cria um novo objeto da classe Turma passando o valor de $id como parâmetro
$aluno = new Aluno($id);
?>

<!DOCTYPE html>
<html lang="pt-br">

<head>
    <meta charset="UTF-8">

    <title>Sistema Acadêmico</title>
</head>

<body>
    <div>
        <h3>Sistema Acadêmico - Painel de controle</h3>
    </div>
    <div>
        <h3>
            ATUALIZAR REGISTRO
        </h3>
    </div>
    <div>
        <form enctype="multipart/form-data" action="alunos-editar-gravar.php" method="POST">
            <div>

            </div>
            <input type="hidden" name="id" value="<?= $aluno->id ?>">
            <div>
                <label for="txtnome">Nome:</label>
                <input  type="text" name="txtnome" value="<?= $aluno->nome ?>">
            </div>
            <div>
                <label for="txtemail">E-mail:</label>
                <input  type="text" name="txtemail" value="<?= $aluno->email ?>">
            </div>
            <div>
                <label for="selturma">Turma:</label>
                <select  name="selturma">
                    <option value=''>Selecione...</option>
                    <?php
                    foreach ($lista as $linha) :
                        if ($linha['id'] == $aluno->turma_id) {
                            echo "<option value='{$linha['id']}' selected> 
                                         {$linha['descTurma']}
                                    </option>";
                        } else {
                            echo "<option value='{$linha['id']}'> 
                                         {$linha['descTurma']}
                                    </option>";
                        }
                    endforeach
                    ?>
                </select>
            </div>

            <img class="img-thumbnail my-3" id="preview" src="../../img/<?= $aluno->foto ?>" height="150"><br>
            <input type="file" id="inputFile" name="foto" onchange="previewImage(this)">
            <br><br>
            <input class="form-control btn btn-success" type="submit" value="Gravar">
        </form>
    </div>

    </div>

    <script>
        //Javascrip para atualizar a foto automaticamente após a seleção
        function previewImage(input) {
            var preview = document.getElementById('preview');
            var file = input.files[0];
            var reader = new FileReader();

            reader.onload = function(e) {
                preview.src = e.target.result;
                preview.style.display = 'block';
            };

            if (file) {
                reader.readAsDataURL(file);
            } else {
                preview.src = '#';
                preview.style.display = 'none';
            }
        }
    </script>


</body>

</html>