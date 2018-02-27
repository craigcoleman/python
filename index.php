<html><head><title>START LINUX COMMANDS</title>
<style>
#menu {
    position: absolute;
    left: 50px;
    top: 0px;
}
#contents{
    position: absolute;
    left: 100px;
    top: 50px;
}
</style>

</head>
<body>
<div id = "menu">
<a href = "index.php?v=0"  >BASH DATE</a>&nbsp; 
<a href = "index.php?v=1"  >MAN PS</a>&nbsp; 
<a href = "index.php?v=2"  >PS</a>&nbsp; 
<a href = "index.php?v=3"  >PS -A</a>&nbsp;
<a href = "index.php?v=4"  >TIME C CODE</a>&nbsp;
<a href = "index.php?v=5"  >PYTHON PING </a>&nbsp;
<a href = "source/">SOURCE </a>&nbsp;
<hr />
</div>

<div id = "contents">
<pre>
<?php
if (isset($_GET['v'])) {
	$thepost = $_GET['v']; // Default page
	} else {
		$thepost = -1;
	}
	
if ($thepost == -1) {
	$output = shell_exec('cal');
	 echo "OUTPUT";
	echo "<pre>$output</pre>";
}
if ($thepost == 0) {
	$output = shell_exec('date');
	 echo "OUTPUT";
	echo "<pre>$output</pre>";
}
if ($thepost == 1) {
	$output = shell_exec('man ps');
	 echo "OUTPUT";
	echo "<pre>$output</pre>";
}
if ($thepost == 2) {
	$output = shell_exec('ps');
	 echo "OUTPUT";
	echo "<pre>$output</pre>";
}

if ($thepost == 3) {
	$output = shell_exec('ps -a');
	 echo "OUTPUT";
	echo "<pre>$output</pre>";
}
if ($thepost == 4) {
        $output = shell_exec('./source/time');
	 echo "OUTPUT";
        echo "<pre>$output</pre>";
}

if ($thepost == 5) {
        $output = shell_exec('python3 source/pingdate.py');
	 echo "OUTPUT";
        echo "<pre>$output</pre>";
}

?>
</pre>
<hr />
</div>


</body>
</html>
