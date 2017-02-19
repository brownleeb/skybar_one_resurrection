<?php
switch ($_GET["temp"]) {
  case "46":
     $setpt=18700;
     break;
  case "48":
     $setpt=18450;
     break;
  case "50":
     $setpt=18150;
     break;
  case "52":
     $setpt=17800;
     break;
  case "54":
     $setpt=17600;
     break;
  case "56":
     $setpt=17300;
     break;
  case "58":
     $setpt=17000;
     break;
  case "60":
     $setpt=16700;
     break;
  case "62":
     $setpt=16400;
     break;
  case "64":
     $setpt=16100;
     break;
}
if (($_GET["temp"]) == "98") {
   system("/usr/local/bin/gpio write 22 1");
   exit();  }
if (($_GET["temp"]) == "99") {
   system("/usr/local/bin/gpio write 22 0");
   exit();  }
if (($_GET["temp"]) == "96") {
   system("/usr/local/bin/dump.sh");
   touch ("/srv/http/no_bottle");
   exit();  }
if (($_GET["temp"]) == "97") {
   system("sudo /usr/local/bin/vacuum.py");
   if (file_exists("/srv/http/no_bottle")) {
      unlink("/srv/http/no_bottle");  }
   exit();  }
$mfile=fopen("set_pt","w");
fwrite($mfile,$setpt);
fclose($mfile);
?>
