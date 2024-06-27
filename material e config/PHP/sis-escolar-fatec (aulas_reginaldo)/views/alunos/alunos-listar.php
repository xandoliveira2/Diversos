<?php
    require "../usuarios/usuario-verifica.php";
    //chama a Classe Aluno.php para o baile
    require_once "../../classes/Aluno.php";

    //Vamos criar mais um objeto Aluno
    $aluno = new Aluno();

    //chama o método "listar" e armazenar o resultado em uma variavel
    $lista = $aluno->listar();





?>
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistema Acadêmico</title>
</head>
<body>
    <h1>Sistema Acadêmico</h1>
    <table border="1">
        <tr>
            <th>Código</th>
            <th>Foto</th>
            <th>Nome</th>
            <th>E-mail</th>
            <th>Turma</th>
            <th>Ações</th>
        </tr>
        <?php foreach($lista as $linha):?>
        <tr>
            <td><?= $linha['id']?></td>
            <td><img src="../../img/<?= $linha['foto']?>" alt="foto" height="80"></td>
            <td><?= $linha['nome']?></td>
            <td><?= $linha['email']?></td>
            <td><?= $linha['descTurma']?></td>
            <td>
                <a href="alunos-editar.php?id=<?= $linha['id'] ?>">Atualizar</a>
                |
                <a href="alunos-excluir.php?id=<?= $linha['id'] ?>">Excluir</a>
            </td>
        </tr>

        <?php endforeach?>
    </table>
    <a href="alunos-inserir.php">NOVO ALUNO</a><br><br>
    <a href="../../index2.php">VOLTAR</a>


</body>
</html>