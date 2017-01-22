<?php
if  (isset($_GET["size"]) == TRUE) {
   $SWITCH = "sudo python switch.py ".$_GET['size'];  }
  else  {
   $SWITCH = "";  }
system($SWITCH);
?>
