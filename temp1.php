<?php
$page = file_get_contents('temp1.txt');
$page = $page . "<h3>Current Temp:&nbsp";
$temp = file_get_contents('/run/temp');
if ($temp>18660) { $page = $page . "46F"; }
elseif ($temp>18537) { $page = $page . "47F"; }
elseif ($temp>18375) { $page = $page . "48F"; }
elseif ($temp>18225) { $page = $page . "49F"; }
elseif ($temp>18075) { $page = $page . "50F"; }
elseif ($temp>17885) { $page = $page . "51F"; }
elseif ($temp>17700) { $page = $page . "52F"; }
elseif ($temp>17600) { $page = $page . "53F"; }
elseif ($temp>17500) { $page = $page . "54F"; }
elseif ($temp>17375) { $page = $page . "55F"; }
elseif ($temp>17225) { $page = $page . "56F"; }
elseif ($temp>17075) { $page = $page . "57F"; }
elseif ($temp>16925) { $page = $page . "58F"; }
elseif ($temp>16775) { $page = $page . "59F"; }
elseif ($temp>16625) { $page = $page . "60F"; }
elseif ($temp>16475) { $page = $page . "61F"; }
elseif ($temp>16325) { $page = $page . "62F"; }
elseif ($temp>16175) { $page = $page . "62F"; }
elseif ($temp>16000) { $page = $page . "64F"; }
else { $page = $page . "65F+"; }
$page = $page . "<br>Set Point:&nbsp";
$temp = file_get_contents('set_pt');
if ($temp==18700) { $page = $page . "46F"; }
if ($temp==18450) { $page = $page . "48F"; }
if ($temp==18150) { $page = $page . "50F"; }
if ($temp==17800) { $page = $page . "52F"; }
if ($temp==17600) { $page = $page . "54F"; }
if ($temp==17300) { $page = $page . "56F"; }
if ($temp==17000) { $page = $page . "58F"; }
if ($temp==16700) { $page = $page . "60F"; }
if ($temp==16400) { $page = $page . "62F"; }
if ($temp==16100) { $page = $page . "64F"; }
$page = $page . "<br></h3>";
$page = $page . file_get_contents('temp2.txt');
echo $page;
