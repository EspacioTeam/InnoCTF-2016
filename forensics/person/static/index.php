<?php
if(isset($_POST['submit'])){
    if($_POST['cookie']=='cookie'){
        echo "Flag: InnoCTF{Chris Tavares}";
    }
}
?>
<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>Forensic100</title>
</head>
<body>
<form action="index.php" method="post">
    <p>Я был рождем в 1970 и был первым в своем роде. Я помню IBM 2741. Я отлично знаком с PL/I. И я очень голоден. Что ты можешь мне предложить?</p>
    <p><input type="text" name="cookie" ></p>
    <p><input type="submit" name="submit" value="Предложить"></p>
</form>
</body>
</html>