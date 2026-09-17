# CodeAlpha-
CodeAlpha Cyber Security internship tasks 
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Pamjive Trading CC - Complete Phishing Training</title>
<style>
body{font-family:Arial;margin:0;background:#f0f2f5;line-height:1.6}
header{background:#0a2a5e;color:white;padding:30px;text-align:center}
header h1{margin:0;font-size:32px}
.red-j{color:#ff0000}
.container{max-width:900px;margin:auto;padding:20px}
.card{background:white;padding:25px;border-radius:12px;margin:20px 0;box-shadow:0 2px 10px rgba(0,0,0,.1)}
h2{color:#0a2a5e;border-bottom:3px solid #0a2a5e;padding-bottom:8px}
ul li{margin:8px 0}
.alert{background:#ffebee;border-left:5px solid red;padding:12px;margin:10px 0}
.tip{background:#e8f5e9;border-left:5px solid green;padding:12px;margin:10px 0}
button{background:#0a2a5e;color:white;padding:12px 20px;border:none;border-radius:6px;cursor:pointer;font-weight:bold;margin-top:10px}
#cert{border:6px double #0a2a5e;padding:35px;text-align:center;background:#fffde7;display:none;margin-top:30px}
.hidden{display:none}
input[type=text]{padding:12px;width:90%;border:1px solid #ccc;border-radius:5px}

/* ONLY CERTIFICATE PRINTS */
@media print{
  body * { visibility: hidden; }
  #cert, #cert * { visibility: visible; }
  #cert {
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    display: block !important;
    border: 8px double #0a2a5e !important;
    box-shadow: none;
  }
  #cert button { display: none; }
}
</style>
</head>
<body>
<header>
<h1>Pam<span class="red-j">j</span>ive Trading CC</h1>
<h2 style="color:white;border:none">🎣 Don't Take the Bait: Phishing Awareness Training</h2>
</header>

<div class="container">

<div class="card">
<h2>1. What is Phishing?</h2>
<p>Phishing is a cyberattack where criminals pretend to be a trusted person or company to steal your passwords, money, or personal data. It's the <b>#1 way hackers break in.</b></p>
</div>

<div class="card">
<h2>2. How to Recognize Phishing Emails</h2>
<ul>
<li><b>Sender address:</b> support@paypa1.com instead of support@paypal.com</li>
<li><b>Urgent language:</b> "Your account will be CLOSED in 24 hours!"</li>
<li><b>Generic greeting:</b> "Dear Customer" instead of your name</li>
<li><b>Bad links:</b> Hover first. Does the link really go to the bank?</li>
<li><b>Attachments:</b> Unexpected invoice.zip, payment.doc</li>
</ul>
</div>

<div class="card">
<h2>3. How to Spot Fake Websites</h2>
<ul>
<li>Check URL spelling: amaz0n.com, fnb-namibia-secure.com</li>
<li>No padlock (https) + "Not Secure" warning</li>
<li>Poor design, blurry logos, grammar mistakes</li>
<li>Site asks for PIN / OTP / full password when real sites wouldn't</li>
</ul>
</div>

<div class="card">
<h2>4. Social Engineering Tactics</h2>
<p><b>Urgency & Fear:</b> "Suspicious login detected!"<br>
<b>Authority:</b> Pretending to be CEO, IT, Bank, MTC, FNB<br>
<b>Curiosity & Greed:</b> "You won N$50,000! Click to claim"<br>
<b>Sympathy:</b> Fake charity or stranded friend scam</p>
</div>

<div class="card">
<h2>5. Real-World Examples in Namibia</h2>
<div class="alert">
<b>1. Bank SMS Phish:</b> "FNB: Your account locked. Verify here: bit.ly/fnb-na123"<br>
<b>2. MTC/TN Mobile:</b> "You won a prize, send your ID and bank details via WhatsApp"<br>
<b>3. Business Email Compromise:</b> Fake invoice from "supplier" with changed bank account
</div>
</div>

<div class="card">
<h2>6. Best Practices - 5 Golden Tips</h2>
<div class="tip">
1. <b>Stop, Look, Think</b> before you click<br>
2. <b>Verify separately:</b> Call the bank/company on their official number<br>
3. <b>Never share OTPs, PINs, or passwords</b> by email/SMS<br>
4. <b>Enable 2FA</b> (Two-Factor Authentication)<br>
5. <b>Report it:</b> Delete, don't reply. Report to IT/security
</div>
</div>

<div class="card">
<h2>Trainee Information</h2>
<input type="text" id="name" placeholder="Enter your full name">
<br>
<button onclick="document.getElementById('quiz').classList.remove('hidden')">I Have Read All Modules → Take Quiz</button>
</div>

<div class="card hidden" id="quiz">
<h2>7. Final Assessment - Pass 2/3 to get Certificate</h2>
<p><b>Q1:</b> You get an email from "IT Support" asking for your password?<br>
<input type="radio" name="q1"> a) Send it quickly<br>
<input type="radio" name="q1" id="a1"> b) Ignore and report to real IT</p>
<p><b>Q2:</b> Link shows www.paypal-secure-login.com. Real or fake?<br>
<input type="radio" name="q2"> Real<br>
<input type="radio" name="q2" id="a2"> Fake</p>
<p><b>Q3:</b> Padlock icon means 100% legitimate?<br>
<input type="radio" name="q3"> True<br>
<input type="radio" name="q3" id="a3"> False</p>
<button onclick="check()">Submit & Get Certificate</button>
</div>

<div id="cert">
<h1 style="color:#0a2a5e">Certificate of Completion</h1>
<p>This certifies that</p>
<h2 id="certName" style="font-size:28px"></h2>
<p>has successfully completed <b>Phishing Awareness Training</b></p>
<p>at <b>Pam<span style="color:red">j</span>ive Trading CC</b></p>
<p>Date: <span id="date"></span> | Score: <span id="score"></span>/3</p>
<br><br>
<p>_________________________<br>Training Coordinator</p>
<p style="font-size:12px">Verified by Pam<span style="color:red">j</span>ive Trading CC</p>
<button onclick="window.print()">Print Certificate</button>
</div>

</div>
<script>
function check(){
let s=0;
if(document.getElementById('a1').checked) s++;
if(document.getElementById('a2').checked) s++;
if(document.getElementById('a3').checked) s++;
if(s>=2){
let n=document.getElementById('name').value || "Trainee";
document.getElementById('certName').innerText=n;
document.getElementById('date').innerText=new Date().toLocaleDateString();
document.getElementById('score').innerText=s;
document.getElementById('cert').style.display='block';
window.scrollTo(0,document.body.scrollHeight);
} else { alert("You scored "+s+"/3. You need 2/3 to pass. Try again!"); }
}
</script>
</body>
</html>
