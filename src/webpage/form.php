<!-- form.php -->
<!-- Created 4/5/2016 -->
<!-- Author: John Westhoff (johnjwesthoff@gmail.com) -->

<!-- A simple web form for adding to a yaml file -->
<?php
/* Data is in this form:
 * -  
 *     triggers:
 *         - "trigger1"
 *         - "trigger2"
 *         - "etc"
 *     quote: "Quote"
 *     image: "some url, but this field is optional
 */
// The file to append:
$file = '/home/john/wolfratbot/src/modules/quotes/quotes.yaml';

$data = "-  \n    triggers:\n"; // string for holding what we're writing

if ($_POST['trig'] != '') // ensure the form was propery submitted
{
    $triggers = explode("\n",$_POST['trig']); // list of triggers, line deliminated
    foreach ($triggers as $t)
    {
        $t = addcslashes(strtolower(trim($t)),"\"\\"); // trim whitespace + make lowercase
        if ($t != '') // ensure this isn't a blank line
        {
            $data = $data . "       - \"" . $t . "\"\n"; // add to the data
        }
    }

    $data = $data . "    quote: \"" . addcslashes($_POST['repl'],"\"\\") . "\"\n"; // add quote

    if ($_POST['imgr'] != '') // check if the image is provided
    {
        // if so, add it to the data
        $data = $data . "    image: \"" . addcslashes($_POST['imgr'],"\"\\") . "\"\n";  
    }

    // try to write and provide the appropriate response
    if (file_put_contents($file, $data, FILE_APPEND | LOCK_EX) == False)
    {
        echo '<div class="form-style-7"><h1>FAILED</h1></div>';
    }
    else
    {
        echo '<div class="form-style-7"><h1>Form submitted</h1></div>';
    }
}
?>
<!-- Begin the page document -->
<html>
<head>
<title>Chat Form</title>
<style type="text/css">
.form-style-7{
    max-width:400px;
    margin:50px auto;
    background:#fff;
    border-radius:2px;
    padding:20px;
    font-family: Georgia, "Times New Roman", Times, serif;
}
.form-style-7 h1{
    display: block;
    text-align: center;
    padding: 0;
    margin: 0px 0px 20px 0px;
    color: #5C5C5C;
    font-size:x-large;
}
.form-style-7 ul{
    list-style:none;
    padding:0;
    margin:0;   
}
.form-style-7 li{
    display: block;
    padding: 9px;
    border:1px solid #DDDDDD;
    margin-bottom: 30px;
    border-radius: 3px;
}
.form-style-7 li:last-child{
    border:none;
    margin-bottom: 0px;
    text-align: center;
}
.form-style-7 li > label{
    display: block;
    float: left;
    margin-top: -19px;
    background: #FFFFFF;
    height: 14px;
    padding: 2px 5px 2px 5px;
    color: #B9B9B9;
    font-size: 14px;
    overflow: hidden;
    font-family: Arial, Helvetica, sans-serif;
}
.form-style-7 input[type="text"],
.form-style-7 input[type="date"],
</style>
</head>
<body>
<form class="form-style-7" method="post">
<ul>
<li>
    <label for="trig">Trigger</label>
    <textarea rows="4" cols="50" name="trig"></textarea>
    <span>Enter the text triggers here,
    separated by newlines</span>
</li>
<li>
    <label for="repl">Reply</label>
    <input type="text" name="repl" maxlength="180">
    <span>Enter the text reply here</span>
</li>
<li>
    <label for="imgr">Image</label>
    <input type="url" name="imgr" maxlength="180">
    <span>Enter the image url here</span>
</li>
<li>
    <input type="submit" value="Send This" >
</li>
</ul>
</form>
</body>
</html>
