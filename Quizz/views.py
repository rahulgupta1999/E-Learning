from django.shortcuts import render
from django.http import HttpResponse
from django.template import context,loader
from Quizz.models import Institute,Batch,Student,Subject,Instructor,Quiz,ReadyQuiz,QuizResult,StudyFolder

from datetime import date,datetime

def index(request):
	
	return render(request,'index.html')
	
	
	
	
	
	
def register(request):
	return render(request,'register.html')
	
	
	
	
	
	
	
	
def registerSave(request):
	iname=request.POST["iname"]
	pwd=request.POST["pwd"]
	eid=request.POST["eid"]
	address=request.POST["address"]
	city=request.POST["city"]
	type=request.POST["type"]
	contact=request.POST["contact"]
	c=Institute(instName=iname,password=pwd,type=type,email=eid,address=address,city=city,contact=contact)
	c.save()
	a="<h1>Registered</h1>"
	resp=HttpResponse(a)
	return(resp)
	
	
	
	
	
	
def login(request):
	return render(request,'login.html')
	
	
	
	
	
	
def studentLogin(request):
	return render(request,'studentLogin.html')
	
	
	
	
	
	
	
def instituteLogin(request):
	return render(request,'instituteLogin.html')
	
	
	
	
	
	
	
	
	
def instructorLogin(request):
	return render(request,'instructorLogin.html')
	
	
	
	
	
	
def loginCheckInstitute(request):
	eid=request.POST["eid"]
	pwd=request.POST["pwd"]
	lt=Institute.objects.filter(email=eid,password=pwd)
	if lt:
		request.session["id"]=eid
		request.session["pw"]=pwd
		
		b=lt[0].instName
		c=b.capitalize()
		request.session["iname"]=b
		
		
		
		return render(request,'homeInstitute.html',{"uname":c})
	else:
		return render(request,'retry.html')

		
		
		
		
		
		
		
		
		
		
		

		
def addOpen(request):
	b=request.GET["a"]
	
	
	if b=="stu":
		c=request.session.get("iname")
		d="+@"+c+".stu.in"
		return render(request,'stuSave.html',{"in":d})
		
		
	elif b=="instu":
		c=request.session.get("iname")
		d="+@"+c+".fac.in"
		return render(request,'instuSave.html',{"in":d})
	elif b=="batch":
		return render(request,'batchSave.html')

	
	
	
	
	
	
	
	
def classRoom(request):
	b=request.GET["a"]
	
	
	if b=="stu":
		return render(request,'stuClass.html')
		
	elif b=="instu":
		return render(request,'instructClass.html')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def homeBack(request):
	b=request.GET["a"]
	
	
	if b=="teacher":
		k=request.session.get("iname")
		return render(request,'instructorHome.html',{"uname":k})
		
	elif b=="stu":
		k=request.session.get("iname").capitalize()
		return render(request,'homeStudent.html',{"uname":k})
	

	
	
	
	
	
	
	
	
	
	
			
def batchSave(request):
	iname=request.session.get("iname")
	batch=request.POST["batch"]
	c=Batch(instName=iname,batchName=batch)
	c.save()
	a="<h1>Saved</h1>"
	resp=HttpResponse(a)
	return(resp)
	
	
	
	
	
	
	
def getBatch(request):
	iname=request.session.get("iname")
	lt=Batch.objects.filter(instName=iname)
	v="<select id='batch' name='batch' class='form-control custom-select'  required>"
	v+="<option value=disabled>Select Batch</option>"
	if lt:
		for i in lt :
			
			v+="<option value='"+i.batchName+"'>"+i.batchName+"</option>"
		
		v+="</select>"
	else:
		v+="<option value=disabled>No Batch To select</option>"
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)

	
	
	
def getBatchFromTeacher(request):
	name=request.session.get("iname")
	InstName=request.session.get("instName")
	tm=request.session.get("id")
	lt=Subject.objects.filter(teacher=name,instName=InstName,teacherEmail=tm)
	l=[]
	v="<select id='batch' name='batch' class='form-control custom-select' onchange='getSubject()' required>"
	v+="<option value=disabled>Select Batch</option>"
	
	if lt:
		for i in lt :
			if i.batch not in l:
				l.append(i.batch)
		for k in l:
			v+="<option value='"+k+"'>"+k+"</option>"
		
		
		v+="</select>"
	else:
		v+="<option value=disabled>No Batch To select</option>"
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)
	
	
	
	
	
def getTeacher(request):
	iname=request.session.get("iname")
	lt=Instructor.objects.filter(instName=iname)
	v="<select id='teacher' name='teacher' class='form-control custom-select'  required>"
	v+="<option value=disabled>Select Teacher</option>"
	if lt:
		for i in lt :
			
			v+="<option value='"+i.Name+"'>"+i.Name+"</option>"
		
		v+="</select>"
	else:
		v+="<option value=disabled>No Teacher To select</option>"
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)
	
	
	
	
	
	
	
	
def getSubject(request):
	iname=request.session.get("iname")
	InstName=request.session.get("instName")
	Batch=request.GET["batch"]
	lt=Subject.objects.filter(teacher=iname,batch=Batch,instName=InstName)
	request.session["bat"]=Batch
	v="<select id='subject' name='subject' class='form-control custom-select' onchange='getQuiz()'  required>"
	v+="<option value=disabled>Select Subject</option>"
	if lt:
		for i in lt :
			
			v+="<option value='"+i.subject+"'>"+i.subject+"</option>"
		
		v+="</select>"
	else:
		v+="<option value=disabled>No subject for select selected batch</option>"
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)

	
	
	
	
	
def stuSave(request):
	InstName=request.session.get("iname")
	StuName=request.POST["name"]
	Email=request.POST["eid"]
	Password=request.POST["pwd"]
	Batch=request.POST["batch"]
	Gender=request.POST["gender"]
	Dob=request.POST["dob"]
	Address=request.POST["address"]
	c=Student(instName=InstName,stuName=StuName,email=Email,password=Password,batch=Batch,gender=Gender,dateofBirth=Dob,address=Address)
	c.save()
	a="<h1>Student Saved</h1>"
	resp=HttpResponse(a)
	return(resp)






	
def quizSave(request):
	InstName=request.session.get("instName")
	Teacher=request.session.get("iname")
	Batch=request.POST["batch"]
	Subject=request.POST["subject"]
	Question=request.POST["question"]
	Ans1=request.POST["ans1"]
	Ans2=request.POST["ans2"]
	Ans3=request.POST["ans3"]
	Ans4=request.POST["ans4"]
	Answer=request.POST["ans"]
	Point=request.POST["point"]
	qnm=request.POST["qnm"]
	c=Quiz(instName=InstName,quizName=qnm,batch=Batch,subject=Subject,teacher=Teacher,question=Question,ans1=Ans1,ans2=Ans2,ans3=Ans3,ans4=Ans4,correct=Answer,points=Point)
	c.save()
	a="<h1>Quiz Question Saved</h1>"
	resp=HttpResponse(a)
	return(resp)
	




	
def subjectSave(request):
	InstName=request.session.get("iname")
	Batch=request.POST["batch"]
	Sub=request.POST["subject"]
	teacher=request.POST["teacher"]
	TeacherEmail=request.POST["teid"]
	c=Subject(instName=InstName,batch=Batch,subject=Sub,teacher=teacher,teacherEmail=TeacherEmail)
	c.save()
	a="<h1>Subject added</h1>"
	resp=HttpResponse(a)
	return(resp)
	
	
def instructSave(request):
	InstName=request.session.get("iname")
	name=request.POST["name"]
	Email=request.POST["eid"]
	Password=request.POST["pwd"]
	Designation=request.POST["desig"]
	Gender=request.POST["gender"]
	Dob=request.POST["dob"]
	Address=request.POST["address"]
	c=Instructor(instName=InstName,Name=name,email=Email,password=Password,gender=Gender,dateofBirth=Dob,address=Address,designation=Designation)
	c.save()
	a="<h1>Instructor Saved</h1>"
	resp=HttpResponse(a)
	return(resp)

	
	
	
	
def loginCheckStudent(request):
	eid=request.POST["eid"]
	pwd=request.POST["pwd"]
	lt=Student.objects.filter(email=eid,password=pwd)
	if lt:
		request.session["id"]=eid
		request.session["pw"]=pwd
		
		b=lt[0].stuName
		d=lt[0].instName
		bat=lt[0].batch
		request.session["iname"]=b
		request.session["instName"]=d
		request.session["btc"]=bat
		c=b.capitalize()
		return render(request,'homeStudent.html',{"uname":c})
	else:
		return render(request,'retry.html')

def loginCheckInstructor(request):
	eid=request.POST["eid"]
	pwd=request.POST["pwd"]
	lt=Instructor.objects.filter(email=eid,password=pwd)
	if lt:
		request.session["id"]=eid
		request.session["pw"]=pwd
		
		b=lt[0].Name
		d=lt[0].instName
		request.session["iname"]=b
		
		request.session["instName"]=d
		c=b.capitalize()
		return render(request,'instructorHome.html',{"uname":c})
	else:
		return render(request,'retry.html')
	
	
def quizOpen(request):
	return render(request,'quiz.html')

	
	
def getQuiz(request):
	name=request.session.get("iname")
	InstName=request.session.get("instName")
	Subject=request.GET["subject"]
	Batch=request.session.get("bat")
	lt=Quiz.objects.filter(teacher=name,subject=Subject,batch=Batch,instName=InstName)
	rs=ReadyQuiz.objects.filter(teacher=name,subject=Subject,batch=Batch,instName=InstName)
	a=[]
	if rs:
		for k in rs:
			if k.quizName not in a:
				a.append(k.quizName)
	
	l=[]
	v="<select id='qnm' name='qnm' class='form-control custom-select' onchange='checkQuiz()' required>"
	v+="<option value=disabled>Select Quiz</option>"
	if lt:
		for i in lt:
			if i.quizName not in a:
				l.append(i.quizName)
				a.append(i.quizName)
		for k in l:
			v+="<option value='"+k+"'>"+k+"</option>"
		
		v+="<option value='new'>New Quiz</option>"
		v+="</select>"
	else:
		v+="<option value='new'>New Quiz</option>"
		
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)	

def loadInput(request):
	v="<div class='form-group'>"
	v+="<label class='control-label col-sm-2 text-primary' for='qnm' >Quizz Name</label>"
	v+="<div class='col-sm-6'>"
	v+="<input type=text id='qnm' name='qnm' placeholder='Quizz Name' class='form-control' required /></div>"
	v+="</div>"
	
	resp=HttpResponse(v)
	return(resp)
	
def getquiz(request):
	name=request.session.get("iname")
	InstName=request.session.get("instName")
	Subject=request.GET["subject"]
	Batch=request.session.get("bat")
	lt=Quiz.objects.filter(teacher=name,subject=Subject,batch=Batch,instName=InstName)
	l=[]
	v="<select id='qnm' name='qnm' class='form-control custom-select' onchange='checkQuiz()' required>"
	v+="<option value='disabled'>Select Quiz</option>"
	if lt:
		for i in lt :
			if i.quizName not in l:
				l.append(i.quizName)
		for k in l:
			v+="<option value='"+k+"'>"+k+"</option>"
		
		
		v+="</select>"
	else:
		v+="<option value='disabled'>No Quizz to select</option>"
		
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)		

def getQuizForSetup(request):
	name=request.session.get("iname")
	InstName=request.session.get("instName")
	Subject=request.GET["subject"]
	Batch=request.session.get("bat")
	lt=Quiz.objects.filter(teacher=name,subject=Subject,batch=Batch,instName=InstName)
	rs=ReadyQuiz.objects.filter(teacher=name,subject=Subject,batch=Batch,instName=InstName)
	a=[]
	if rs:
		for k in rs:
			if k.quizName not in a:
				a.append(k.quizName)
	
	l=[]
	v="<select id='qnm' name='qnm' class='form-control custom-select' onchange='checkQuiz()' required>"
	v+="<option value=disabled>Select Quiz</option>"
	if lt:
		for i in lt:
			if i.quizName not in a and i.quizName not in l:
				l.append(i.quizName)
		for k in l:
			v+="<option value='"+k+"'>"+k+"</option>"
		
		
		v+="</select>"
	else:
		v+="<option >No Quiz</option>"
		
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)	
	
def QuestionBankOpen(request):
	return render(request,'question.html')

def answerBank(request):
	name=request.session.get("iname")
	InstName=request.session.get("instName")
	Subject=request.POST["subject"]
	Batch=request.POST["batch"]
	QuizName=request.POST["qnm"]
	rs=ReadyQuiz.objects.filter(teacher=name,subject=Subject,batch=Batch,instName=InstName)
	a=[]
	if rs:
		for k in rs:
			if k.quizName not in a:
				a.append(k.quizName)
	lt=Quiz.objects.filter(teacher=name,subject=Subject,batch=Batch,instName=InstName,quizName=QuizName)
	v="<html lang='en'><head><meta charset='utf-8'/>"
	v+="<meta name='viewport' content='width=device-width,initial-scale=1'/>"
	v+="<link rel='stylesheet' href='/static/bootstrap.min.css'/>"
	v+="<script src=/static/jquery.min.js></script>"
	v+="<script src='/static/bootstrap.min.js'></script>"
	v+="<script src=/static/jquery-3.3.1.min.js></script><script></script><body class='bg-success'>"
	
	v+="<div class='container'><h1>"+lt[0].subject.capitalize()+"</h1>"
	v+="<h4>"+lt[0].quizName.capitalize()+"</h4>"
	if lt:
		if lt[0].quizName not in a:
			v+="<table class='table' style='background-color:white;'><thead>"
	
			v+="<tr><th class='warning'>Points</th><th>Question</th><th  class='active'>Option A</th><th class='info'>Option B</th><th class='warning'>Option C</th><th class='danger'>Option D</th><th class='info'>Correct Answer</th><th>For Delete</th></tr></thead><tbody>"
			for i in lt:
				v+="<tr><td class='warning' >"+str(i.points)+"</td><td>"+i.question+"</td><td class='active'>"+i.ans1+"</td><td class='info'>"+i.ans2+"</td><td class='warning'>"+i.ans3+"</td><td class='danger'>"+i.ans4+"</td><td class='info'>"+i.correct+"</td><td><a href=delQuestion?q="+str(i.id)+" >Delete</a></div></td></tr>"
			
			v+="</tbody></table></div></body></html>"
		else:
			v+="<h4><font color='red'>Quiz Status :</font><font color='green'> Activated</font></h4>"
			v+="<h4><font color='blue'>*You cannot delete questions from activated quiz </font></p>"
			v+="<table class='table' style='background-color:white;'><thead>"
	
			v+="<tr><th class='warning'>Points</th><th>Question</th><th  class='active'>Option A</th><th class='info'>Option B</th><th class='warning'>Option C</th><th class='danger'>Option D</th><th class='info'>Correct Answer</th></tr></thead><tbody>"
			for i in lt:
				v+="<tr><td class='warning' >"+str(i.points)+"</td><td>"+i.question+"</td><td class='active'>"+i.ans1+"</td><td class='info'>"+i.ans2+"</td><td class='warning'>"+i.ans3+"</td><td class='danger'>"+i.ans4+"</td><td class='info'>"+i.correct+"</td></tr>"
			
			v+="</tbody></table></div></body></html>"
	else:
		v+="<h1>No record to show<h1>"
		
	resp=HttpResponse(v)
	return(resp)
def forgot(request):
	a=request.GET["a"]
	
	if a=="stu":
		b="Student"
		return render(request,'forgot.html',{"u":b})
	if a=="inst":
		c="Teacher"
		return render(request,'forgot.html',{"u":c})
def getPassword(request):
	dob=request.POST["db"]
	Email=request.POST["eid"]
	cat=request.POST["cat"]
	if cat=="Student":
		lt=Student.objects.filter(email=Email,dateofBirth=dob)
		if lt:
			v="<center><br><br><h1>Name : "+lt[0].stuName.capitalize()+"</h1><br><h1>Password : "+lt[0].password+"</h1></center>"
		else:
			v="<center><br><br><h1>Invalid Date of Birth or Email</h1></center>"
	elif cat=="Teacher":
		lt=Instructor.objects.filter(email=Email,dateofBirth=dob)
		if lt:
			v="<center><br><br><h1>Name : "+lt[0].Name.capitalize()+"</h1></br><h1>Password : "+lt[0].password+"</h1></center>"
		else:
			v="<center><br><br><h1>Invalid Date of Birth or Email</h1></center>"
	resp=HttpResponse(v)
	return(resp)
	
def delQuestion(request):
	qid=request.GET["q"]
	rs=Quiz.objects.filter(id=qid).delete()
	v="Question deleted"
	resp=HttpResponse(v)
	return(resp)
	
def stuList(request):
	return render(request,'stuList.html')
	
def getBatchForStudent(request):
	name=request.session.get("iname")
	InstName=request.session.get("instName")
	lt=Subject.objects.filter(teacher=name,instName=InstName)
	v="<select id='batch' name='batch' class='form-control custom-select' onchange='getStudent()' required>"
	v+="<option value=disabled>Select Batch</option>"
	if lt:
		for i in lt :
			
			v+="<option value='"+i.batch+"'>"+i.batch+"</option>"
		
		v+="</select>"
	else:
		v+="<option value=disabled>No Batch To select</option>"
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)

	
	
	
def getStudentList(request):
	Batch=request.GET["batch"]
	InstName=request.session.get("instName")
	lt=Student.objects.filter(instName=InstName,batch=Batch)
	v="<select id='student' name='student' class='form-control custom-select' required>"
	v+="<option value=disabled>Select Student</option>"
	if lt:
		for i in lt :
			v+="<option value='"+i.email+"'>"+(i.stuName.capitalize())+"</option>"
		v+="</select>"
	else:
		v+="<option value=disabled>No Student To select</option>"
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)
	
	
def teacherList(request):
	return render(request,'teacherList.html')
	
	
	
	
		
	
def getTeacherList(request):
	Batch=request.session.get("btc")
	InstName=request.session.get("instName")
	lt=Subject.objects.filter(instName=InstName,batch=Batch)
	a=[]
	v="<select id='subject' name='subject' class='form-control custom-select' required>"
	v+="<option value=disabled>Select Subject</option>"
	for j in lt:
		if j.subject not in a:
			a.append(j.subject)
	for k in a:
		v+="<option value='"+k+"'>"+k+"</option>"
				
		
	v+="</select>"
	resp=HttpResponse(v)
	return(resp)
		

		
	
	
	
def changepasswordOpen(request):	
	a=request.GET["a"]
	return render(request,'changepassword.html',{"u":a})

	
def changepassword(request):
	old=request.POST["opwd"]
	new=request.POST["npwd"]
	cnew=request.POST["cnpwd"]
	id=request.session.get("id")
	a=request.POST["cat"]
	if a=="Institute":
		qs=Institute.objects.filter(email=id,password=old)
	elif a=="Teacher":
		qs=Instructor.objects.filter(email=id,password=old)
	elif a=="Student":
		qs=Student.objects.filter(email=id,password=old)
		
	if new==cnew and qs:
		qs[0].password=new
		qs[0].save()
		msg="<h1>Password change<h1>"
	else:
		msg="<h1>Invalid Password<h1>"
	resp=HttpResponse(msg)
	return(resp)
	
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
def startQuiz(request):
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	<script>
	$(document).ready(function(){
	t=$("#time").val()
	tj=parseInt(t)	
	tm=tj*60
	a=tm
	k=setInterval(function(){
	a--;
	s=a
	var h=Math.floor(s/3600);
	s-=h*3600;
	var m=Math.floor(s/60);
	s-=m*60
	msg="Time Left:"+(m<10 ? '0'+m : m)+":"+(s<10 ? '0'+s : s);
	tf=((tm-a)/tm)*100
	$("#timer").text(msg);
	$("#progress").text(msg);
	$("#progress").css("width",tf+"%");
	if(a<30)
	{
	$("#timer").css("background-color","red");
	$("#progress").css("width",tf+"%");
	$("#progress").removeClass("progress-bar-success");
	$("#progress").addClass("progress-bar-danger");
	$("#alert").css("display","block");
	}
	if(a==1)
	{
	clearInterval(k);
	document.quizForm.submit();
	}
	},1000)
	
	ques=$(".ques");
	tq=ques.length;
	$(".nextQ").click(function(){
	qno=$(this).val();
	if(qno<tq-1) 
	{
	$(this).parent().hide();
	$(this).parent().next().show();
	}
	})
	$(".prevQ").click(function(){
	qno=$(this).val();
	if(qno>0)
	{
	$(this).parent().hide();
	$(this).parent().prev().show();
	}
	})


	});
	
	</script>

	</head>
	<body>
	
	<form name="quizForm" method=get action=resultSave >
	'''
	eid=request.session.get("id")
	s=Student.objects.filter(email=eid)
	inm=s[0].instName
	Batch=s[0].batch
	QuizName=request.GET["qnm"]
	Subject=request.GET["sub"]
	qs=Quiz.objects.filter(instName=inm,batch=Batch,quizName=QuizName)
	k=qs.count()
	rs=ReadyQuiz.objects.filter(instName=inm,batch=Batch,quizName=QuizName,subject=Subject)
	t=rs[0].time
	v+="<input type=hidden name='time' value="+t+" id='time' ></input>"
	
	v+="<center><h3 id=timer  style='width:10%; align:center;' >Time Left: </h3></center><div class='progress'><div class='progress-bar progress-bar-success progress-bar-striped active' role='progressbar' aria-valuenow='40' aria-valuemin='0' area-valuemax='100' id='progress'  >Total Time:"+t+"</div></div>"
		
		
	i=0
	for rec in qs:
		
	
		if i==0:
			
			v+="<div class='ques'  style='display:block' >"
			v+="<div class='container'><ul class='pagination'>"
			for j in range(0,k):
				if j==i:
					v+="<li class='active'><a>"+str(j+1)+"</a></li>"
				else:
					v+="<li><a>"+str(j+1)+"</a></li>"
			v+="</ul></div>"
			v+="<h4><font color='blue'>Question Points: "+str(rec.points)+"</font><br><br>Ques 1 : "+rec.question+"</h4>"
		else:
			
			
			v+="<div class='ques'  style='display:none' >"
			v+="<div class='container'><ul class='pagination'>"
			for j in range(0,k):
				if j==i:
					v+="<li class='active' ><a>"+str(j+1)+"</a></li>"
				else:
					v+="<li><a>"+str(j+1)+"</a></li>"
			v+="</ul></div>"
			v+="<h4><font color='blue'>Question Points: "+str(rec.points)+"</font><br><br>Ques "+str(i+1)+" : "+rec.question+"</h4>"
		
		
		v+="<h4>"
		v+="<input type=radio name='ans"+str(i)+"' value=a />"+rec.ans1+"</br>"
		v+="<input type=radio name='ans"+str(i)+"' value=b />"+rec.ans2+"</br>"
		v+="<input type=radio        name='ans"+str(i)+"' value=c />"+rec.ans3+"</br>"
		v+="<input type=radio name='ans"+str(i)+"' value=d />"+rec.ans4+"</br><input type=radio style='display:none' name='ans"+str(i)+"' value='None' checked/></br></h4>"
		v+="<input type=hidden name='correctAns"+str(i)+"' value='"+rec.correct+"'  />"
		v+="<input type=hidden name='teacher' value='"+rec.teacher+"'  />"
		v+="<input type=hidden name='batch' value='"+rec.batch+"'  />"
		v+="<input type=hidden name='instName' value='"+rec.instName+"'  />"
		v+="<input type=hidden name='qnm' value='"+rec.quizName+"'  />"
		v+="<input type=hidden name='subject' value='"+rec.subject+"'  />"
		v+="<input type=hidden name='points"+str(i)+"' value="+str(rec.points)+"  /><br><br>"
		v+="<button type=button class='nextQ form-control btn btn-info' value="+str(i)+" >Next Question</button> "
		v+="<button type=button class='prevQ form-control btn btn-success' value="+str(i)+">Previous Question</button> "

		v+="</div>"
		i=i+1
	v+="<input type=submit value='Submit' class='form-control btn btn-danger'></form><div id='alert' class='alert alert-danger' style='display:none; width:20%;'><strong>Hurry!!</strong>Less than 30 sec left.</strong></div> </body>"
	resp=HttpResponse(v)
	return(resp)


def quizList(request):
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	</head>
	<body>
	'''
	eid=request.session.get("id")
	s=Student.objects.filter(email=eid)
	Batch=s[0].batch
	inm=s[0].instName
	qs=ReadyQuiz.objects.filter(instName=inm,batch=Batch)
	v+="<h1>Active Quiz</h1><table class='table'><tr><th class='active'>Quiz Name</th><th class='active'>Subject</th><th class='active'>Total Question</th><th class='active'>Time</th><th class='active'>Start quiz</th>"
	for rec in qs:
		Teacher=rec.teacher
		Subject=rec.subject
		QuizName=rec.quizName
		rs=Quiz.objects.filter(instName=inm,teacher=Teacher,quizName=QuizName,batch=Batch,subject=Subject)

		v+="<tr><td  class='info'>"+rec.quizName.capitalize()+"</td><td class='info'>"+rec.subject+"</td><td class='info'>"+str(len(rs))+"</td><td class='info'>"+rec.time+" Minutes</td><td class='success'><a href=startQuiz?qnm="+rec.quizName+"&sub="+rec.subject+" >Start Quiz</td>"
	v+="</table>"
		
	resp=HttpResponse(v)
	return(resp)
	
	
def setupQuiz(request):
	return render(request,'quizSetup.html')

	
	
def quizActivate(request):
	InstName=request.session.get("instName")
	QuizName=qnm=request.POST["qnm"]
	Teacher=request.session.get("iname")
	Batch=request.POST["batch"]
	Subject=request.POST["subject"]
	Attempts=request.POST["attempt"]
	Time=request.POST["time"]
	c=ReadyQuiz(instName=InstName,quizName=QuizName,batch=Batch,subject=Subject,teacher=Teacher,attempts=Attempts,time=Time)
	c.save()
	a="<h1>Quiz Activated</h1>"
	resp=HttpResponse(a)
	return(resp)

def resultSave(request):
	eid=request.session.get("id")
	Teacher=request.GET["teacher"]
	QuizName=request.GET["qnm"]
	Subject=request.GET["subject"]
	Batch=request.GET["batch"]
	InstName=request.GET["instName"]
	qs=Quiz.objects.filter(instName=InstName,teacher=Teacher,quizName=QuizName,batch=Batch,subject=Subject)
	rqs=ReadyQuiz.objects.filter(instName=InstName,teacher=Teacher,quizName=QuizName,batch=Batch,subject=Subject)
	att=int(rqs[0].attempts)
	gs=QuizResult.objects.filter(instName=InstName,teacher=Teacher,quizName=QuizName,batch=Batch,subject=Subject,stuEmail=eid)
	attdone=len(gs)
	if attdone>=att:
		v="<h1><font color=blue>Oops... you have reach Maximum no of attempts !!<font><h1>"
	else:
		corr=0
		points=0
		totalpoints=0
		tqs=len(qs)
		v="<html lang='en'><head><meta charset='utf-8'/>"
		v+="<meta name='viewport' content='width=device-width,initial-scale=1'/>"
		v+="<link rel='stylesheet' href='/static/bootstrap.min.css'/>"
		v+="<script src=/static/jquery.min.js></script>"
		v+="<script src='/static/bootstrap.min.js'></script>"
		v+="<script src=/static/jquery-3.3.1.min.js></script><script></script><body class='bg-success'>"
		v+="<table class='table' style='background-color:white;'><thead>"
		v+="<tr><th class='active'>Question Number</th><th  class='active'>Your Answer</th><th class='active'>Correct Answer</th><th class='active'>Points</th><th class='active'>Status</th></tr></thead><tbody>"
		for i in range(0,len(qs)):
		
			ca=request.GET["correctAns"+str(i)]
			ua=request.GET["ans"+str(i)]
			p=int(request.GET["points"+str(i)])
			totalpoints=totalpoints+p
			if ca==ua: 
				corr=corr+1
				points=points+p
				v+="<tr><td class='info'>"+str(i+1)+"</td><td  class='info'>"+ua.capitalize()+"</td><td class='info'>"+ca.capitalize()+"</td><td class='info'>"+str(p)+"</td><td class='info'>Correct</td></tr>"
			else:
				v+="<tr><td class='danger'>"+str(i+1)+"</td><td  class='danger'>"+ua.capitalize()+"</td><td class='danger'>"+ca.capitalize()+"</td><td class='danger'>"+str(p)+"</td><td class='danger'>Incorrect</td></tr>"
		v+="</tbody></table>"
		v+="<h1>Your result is "+str(corr)+" out of "+str(len(qs))+" answer are correct.</h1>";
		v+="<h1>You score "+str(points)+" points out of "+str(totalpoints)+" points.</h1>";
		today=date.today()
		dt=today.strftime("%Y-%m-%d")
		now=datetime.now()
		tm=now.strftime("%H:%M:%S")
		qr=QuizResult(instName=InstName	,quizName=QuizName,batch=Batch,subject=Subject,teacher=Teacher,totalPoints=points,quizDate=dt,quizTime=tm,stuEmail=eid,correctAnswer=corr,totalQues=tqs)
		qr.save()
		v+="<h1 align='center'>Quiz Submitted</h1>"
	resp=HttpResponse(v)
	return(resp)

def quizDeactivate(request):
	InstName=request.session.get("instName")
	QuizName=qnm=request.POST["qnm"]
	Teacher=request.session.get("iname")
	Batch=request.POST["batch"]
	Subject=request.POST["subject"]

	c=ReadyQuiz.objects.filter(instName=InstName,quizName=QuizName,batch=Batch,subject=Subject,teacher=Teacher).delete()
	a="<h1>Quiz Deactivated</h1>"
	resp=HttpResponse(a)
	return(resp)	
	
def deactivateOpen(request):
	return render(request,'deactivate.html')
	
	
	
def getactivateQuiz(request):
	name=request.session.get("iname")
	InstName=request.session.get("instName")
	Subject=request.GET["subject"]
	Batch=request.session.get("bat")
	rs=ReadyQuiz.objects.filter(teacher=name,subject=Subject,batch=Batch,instName=InstName)
	a=[]
	v="<select id='qnm' name='qnm' class='form-control custom-select'  required>"
	v+="<option value=disabled>Select Quiz</option>"
	if rs:
		for k in rs:
			if k.quizName not in a:
				a.append(k.quizName)
	
	
	
	
		for i in a:
			v+="<option value='"+i+"'>"+i+"</option>"
		
		
		v+="</select>"
	else:
		v+="<option >No Quiz</option>"
		
		v+="</select>"
	resp=HttpResponse(v)
	return(resp)	
	
def profile(request):
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	</head>
	<body class="bg-success">
	'''
	StuName=request.session.get("iname")
	InstName=request.session.get("instName")
	Batch=request.session.get("btc")
	Email=request.session.get("id")
	stu=Student.objects.filter(instName=InstName,batch=Batch,email=Email,stuName=StuName)
	sub=Subject.objects.filter(instName=InstName,batch=Batch,)
	if stu:
		v+="<br><br><div class='container' style=' background-image:url(/static/classbg.jpg)' ><img src='/static/profile.jpg' style='width:20%;' class='img-circle'>"
		v+="<br><h2><font color='white'>"+StuName.capitalize()+ " </font><span class='badge' style='background-color:white;'><span style='color:white;'>&#10004;</span></span></h2><h4><span class='label label-warning'>Student</h4></div>"
		v+="<br><div class='container' ><div class='row'><div class='col-lg-6 bg-info' style='background-color:white;'>"
		v+="<br><h5 class='bg-success'>&#x1F947;  " +stu[0].batch.capitalize()+"</h5><br>"	
		
		v+="<h5 class='bg-info'>&#127891;  " +stu[0].instName+"</h5><br>"
		v+="<h5 class='bg-warning'>&#x2709;  " +stu[0].email+"</h5><br>"
		v+="<h5 class='bg-success'>&#x1F382;  " +str(stu[0].dateofBirth)+"</h5><br>"	
		v+="<h5 class='bg-primary'>&#x1F38E;  " +stu[0].gender.capitalize()+"</h5><br>"
		v+="<h5 class='bg-danger'>&#x1F30D;  " +stu[0].address+"</h5><br></div>"	
		v+="<br><br><div class='col-lg-6' ><table class='table'><tr><th class='danger'>Subject</th><th class='warning'>Teacher Name</th>"
		for rec in sub:
			v+="<tr><td class='danger'>"+rec.subject+"</td><td class='warning'>"+rec.teacher+"</td>"
		v+="<table>"
		v+="</div></div></div>"
	resp=HttpResponse(v)
	return(resp)	
	
def getStuProfile(request):
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	</head>
	<body class="bg-success">
	'''
	Email=request.POST["student"]
	InstName=request.session.get("instName")
	Batch=request.POST["batch"]
	
	stu=Student.objects.filter(instName=InstName,batch=Batch,email=Email)
	sub=Subject.objects.filter(instName=InstName,batch=Batch,)
	if stu:
		v+="<br><br><div class='container' style=' background-image:url(/static/classbg.jpg)' ><img src='/static/profile.jpg' style='width:20%;' class='img-circle'>"
		v+="<br><h2><font color='white'>"+stu[0].stuName.capitalize()+ " </font><span class='badge' style='background-color:white;'><span style='color:white;'>&#10004;</span></span></h2><h4><span class='label label-warning'>Student</h4></div>"
		v+="<br><div class='container' ><div class='row'><div class='col-lg-6 bg-info' style='background-color:white;'>"
		v+="<br><h5 class='bg-success'>&#x1F947;  " +stu[0].batch.capitalize()+"</h5><br>"	
		
		v+="<h5 class='bg-info'>&#127891;  " +stu[0].instName+"</h5><br>"
		v+="<h5 class='bg-warning'>&#x2709;  " +stu[0].email+"</h5><br>"
		v+="<h5 class='bg-success'>&#x1F382;  " +str(stu[0].dateofBirth)+"</h5><br>"	
		v+="<h5 class='bg-primary'>&#x1F38E;  " +stu[0].gender.capitalize()+"</h5><br>"
		v+="<h5 class='bg-danger'>&#x1F30D;  " +stu[0].address+"</h5><br></div>"	
		v+="<br><br><div class='col-lg-6' ><table class='table'><tr><th class='danger'>Subject</th><th class='warning'>Teacher Name</th>"
		for rec in sub:
			v+="<tr><td class='danger'>"+rec.subject+"</td><td class='warning'>"+rec.teacher+"</td>"
		v+="<table>"
		v+="</div></div></div>"
	resp=HttpResponse(v)
	return(resp)	
	
def intsructProfile(request):
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	</head>
	<body class="bg-success">
	'''
	Email=request.session.get("id")
	InstName=request.session.get("instName")
	name=request.session.get("iname")
	
	stu=Instructor.objects.filter(instName=InstName,Name=name,email=Email)
	sub=Subject.objects.filter(instName=InstName,teacher=name)
	if stu:
		v+="<br><br><div class='container' style=' background-image:url(/static/classbg.jpg)' ><img src='/static/profile.jpg' style='width:20%;' class='img-circle'>"
		v+="<br><h2><font color='white'>"+stu[0].Name.capitalize()+ " </font><span class='badge' style='background-color:white;'><span style='color:white;'>&#10004;</span></span></h2><h4><span class='label label-success'>Teacher</h4></div>"
		v+="<br><div class='container' ><div class='row'><div class='col-lg-6 bg-info' style='background-color:white;'>"
		v+="<br><h5 class='bg-success'>&#x1F947;  " +stu[0].designation.capitalize()+"</h5><br>"	
		
		v+="<h5 class='bg-info'>&#127891;  " +stu[0].instName+"</h5><br>"
		v+="<h5 class='bg-warning'>&#x2709;  " +stu[0].email+"</h5><br>"
		
		v+="<h5 class='bg-success'>&#x1F382;  " +str(stu[0].dateofBirth)+"</h5><br>"	
		v+="<h5 class='bg-primary'>&#x1F38E;  " +stu[0].gender.capitalize()+"</h5><br>"
		v+="<h5 class='bg-danger'>&#x1F30D;  " +stu[0].address+"</h5><br></div>"	
		v+="<br><br><div class='col-lg-6' ><table class='table'><tr><th class='danger'>Subject</th><th class='warning'>Batch</th>"
		for rec in sub:
			v+="<tr><td class='danger'>"+rec.subject.capitalize()+"</td><td class='warning'>"+rec.batch.capitalize()+"</td>"
		v+="<table>"
		v+="</div></div></div>"
	resp=HttpResponse(v)
	return(resp)	
	
def getInstructProfile(request):
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	</head>
	<body class="bg-success">
	'''
	Batch=request.session.get("btc")
	InstName=request.session.get("instName")
	subj=request.POST["subject"]
	subt=Subject.objects.filter(instName=InstName,batch=Batch,subject=subj)
	Email=subt[0].teacherEmail
	
	stu=Instructor.objects.filter(instName=InstName,email=Email)
	sub=Subject.objects.filter(instName=InstName,teacherEmail=Email)
	if stu:
		v+="<br><br><div class='container' style=' background-image:url(/static/classbg.jpg)' ><img src='/static/profile.jpg' style='width:20%;' class='img-circle'>"
		v+="<br><h2><font color='white'>"+stu[0].Name.capitalize()+ " </font><span class='badge' style='background-color:white;'><span style='color:white;'>&#10004;</span></span></h2><h4><span class='label label-success'>Teacher</h4></div>"
		v+="<br><div class='container' ><div class='row'><div class='col-lg-6 bg-info' style='background-color:white;'>"
		v+="<br><h5 class='bg-success'>&#x1F947;  " +stu[0].designation.capitalize()+"</h5><br>"	
		v+="<h5 class='bg-info'>&#127891;  " +stu[0].instName+"</h5><br>"
		v+="<h5 class='bg-warning'>&#x2709;  " +stu[0].email+"</h5><br>"
		v+="<h5 class='bg-success'>&#x1F382;  " +str(stu[0].dateofBirth)+"</h5><br>"	
		v+="<h5 class='bg-primary'>&#x1F38E;  " +stu[0].gender.capitalize()+"</h5><br>"
		v+="<h5 class='bg-danger'>&#x1F30D;  " +stu[0].address+"</h5><br></div>"	
		v+="<br><br><div class='col-lg-6' ><table class='table'><tr><th class='danger'>Subject</th><th class='warning'>Batch</th>"
		for rec in sub:
			v+="<tr><td class='danger'>"+rec.subject.capitalize()+"</td><td class='warning'>"+rec.batch.capitalize()+"</td>"
		v+="<table>"
		v+="</div></div></div>"
	resp=HttpResponse(v)
	return(resp)	
	
	
def scorecardStudent(request):
	eid=request.session.get("id")
	Batch=request.session.get("btc")
	InstName=request.session.get("instName")
	gs=QuizResult.objects.filter(instName=InstName,batch=Batch,stuEmail=eid)

	v="<html lang='en'><head><meta charset='utf-8'/>"
	v+="<meta name='viewport' content='width=device-width,initial-scale=1'/>"
	v+="<link rel='stylesheet' href='/static/bootstrap.min.css'/>"
	v+="<script src=/static/jquery.min.js></script>"
	v+="<script src='/static/bootstrap.min.js'></script>"
	v+="<script src=/static/jquery-3.3.1.min.js></script><script></script><body class='bg-success'>"
	v+="<table class='table' style='background-color:white;'><thead>"
	v+="<tr><th class='active'>Date</th><th class='active'>Time</th><th class='active'>Subject</th><th  class='active'>Quiz Name</th><th class='active'>Teacher</th><th class='active'>Total Questions/Correct Answers</th><th class='active'>Points Score</th></tr></thead><tbody>"
	if gs:
		for i in gs:
			v+="<tr><td class='info'>"+str(i.quizDate)+"</td><td  class='warning'>"+str(i.quizTime)+"</td><td class='active'>"+i.subject.capitalize()+"</td><td class='danger'>"+i.quizName+"</td><td class='success'>"+i.teacher+"</td><td class='warning'>"+str(i.totalQues)+"/"+str(i.correctAnswer)+"</td><td class='info'>"+str(i.totalPoints)+"</td></tr>"
		v+="</tbody></table>"
		
	resp=HttpResponse(v)
	return(resp)
	
def scorecardOpen(request):
	return render(request,'scorecardInstructor.html')

	
def scorecardInstructor(request):
	Batch=request.POST["batch"]
	Subject=request.POST["subject"]
	quiz=request.POST["qnm"]
	InstName=request.session.get("instName")
	gs=QuizResult.objects.filter(instName=InstName,batch=Batch,subject=Subject,quizName=quiz)
	qs=Quiz.objects.filter(instName=InstName,batch=Batch,subject=Subject,quizName=quiz)
	tp=0
	pas=0
	fail=0
	for j in qs:
		tp+=int(j.points)
	v="<html lang='en'><head><meta charset='utf-8'/>"
	v+="<meta name='viewport' content='width=device-width,initial-scale=1'/>"
	v+="<link rel='stylesheet' href='/static/bootstrap.min.css'/>"
	v+="<script src=/static/jquery.min.js></script>"
	v+="<script src='/static/bootstrap.min.js'></script>"
	v+="<script src=/static/jquery-3.3.1.min.js></script><script></script><body class='bg-success'>"
	v+="<table class='table' style='background-color:white;'><thead>"
	v+="<tr><th class='active'>Student</th><th class='active'>Student mail</th><th class='active'>Date</th><th class='active'>Time</th><th class='active'>Total Questions/Correct Answers</th><th class='active'>Points Score</th><th class='info'>Status</th></tr></thead><tbody>"
	if gs:
		for i in gs:
			eid=i.stuEmail
			stu=Student.objects.filter(instName=InstName,batch=Batch,email=eid)
			tk=int(i.totalPoints)
			tj=(tk/tp)*100
			if tj>=33:
				v+="<tr><td class='active'>"+stu[0].stuName+"</td><td class='info'>"+i.stuEmail+"</td><td class='warning'>"+str(i.quizDate)+"</td><td  class='success'>"+str(i.quizTime)+"</td><td class='warning'>"+str(i.totalQues)+"/"+str(i.correctAnswer)+"</td><td class='activate'>"+str(i.totalPoints)+"</td><td class='info'>Pass </td></tr>"
				pas=pas+1
			else:
				fail=fail+1
				v+="<tr class='danger'><td class='active'>"+stu[0].stuName+"</td><td class='info'>"+i.stuEmail+"</td><td class='warning'>"+str(i.quizDate)+"</td><td  class='danger'>"+str(i.quizTime)+"</td><td class='success'>"+str(i.totalQues)+"/"+str(i.correctAnswer)+"</td><td class='activate'>"+str(i.totalPoints)+"</td><td>Fail</td></tr>"				
	
	tot=pas+fail
	paspercent=int((pas/tot)*100)
	failpercent=(100-paspercent)
	v+="<div class='progress'><div class='progress-bar progress-bar-success progress-bar-success' role='progressbar' style='width:"+str(paspercent)+"%;' >PASS : "+str(paspercent)+"%</div><div class='progress-bar progress-bar-danger progress-bar-success' role='progressbar' style='width:"+str(failpercent)+"%;' >Fail : "+str(failpercent)+"%</div></div>"
	resp=HttpResponse(v)
	return(resp)
	
def studyMaterial(request):
	return render(request,'studyMaterialTeacher.html')
	
def materialList(request):
	Batch=request.POST["batch"]
	Subject=request.POST["subject"]
	InstName=request.session.get("instName")
	tm=request.session.get("id")
	qs=StudyFolder.objects.filter(instName=InstName,batch=Batch,subject=Subject,teacherEmail=tm)
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	</head>
	<body class='bg-warning'>
	'''
	
	v+="<form method=get action='addFolder' class='form-horizontal' ><div class='form-group'>"
	v+="<label class='control-label col-sm-2 text-primary' for='fnm' > Folder Name: </label>"
	v+="<div class='col-sm-4'>"
	v+="<input type='text' id='fnm' name='fnm' placeholder='Add New Folder' class='form-control' />"
	v+="<input type='hidden' id='batch' name='batch' value='"+Batch+"' class='form-control' />"
	v+="<input type='hidden' id='subject' name='subject' value='"+Subject+"' class='form-control' />"
	v+="<button type=submit class='btn btn-info' class='form-control'>Submit</button></div></div></form>"
	
	v+="<table class='table'><tr><th class='info'>Name</th><th class='success'>open folder</th>"
	for rec in qs:
		v+="<tr><td  class='info'>"+rec.folderName+"</td><td class='success'><a href=matterOpen?batch="+rec.batch+"&sub="+rec.subject+"&fnm="+rec.folderName+"  >open folder</a></td>"
	v+="</table>"
	
	resp=HttpResponse(v)
	return(resp)

def addFolder(request):
	Batch=request.GET["batch"]
	Subject=request.GET["subject"]
	InstName=request.session.get("instName")
	tm=request.session.get("id")
	FolderName=request.GET["fnm"]
	qs=StudyFolder(instName=InstName,batch=Batch,subject=Subject,teacherEmail=tm,folderName=FolderName)
	qs.save()
	v="Folder Added"
	resp=HttpResponse(v)
	return(resp)	
def matterOpen(request):
	Batch=request.GET["batch"]
	Subject=request.GET["sub"]
	FolderName=request.GET["fnm"]
	InstName=request.session.get("instName")
	tm=request.session.get("id")
	qs=StudyMaterial.objects.filter(instName=InstName,batch=Batch,subject=Subject,teacherEmail=tm,folderName=FolderName)
	v='''
	<html>
	<head>
	<meta charset="utf-8"/>
	<meta name="viewport" content="width=device-width,initial-scale=1"/>
	<link rel="stylesheet" href="/static/bootstrap.min.css"/>
	<script src="/static/jquery.min.js"></script>
	<script src="/static/bootstrap.min.js"></script>
	</head>
	<body class='bg-warning'>
	'''
	
	v+="<form method=get action='addFolder' class='form-horizontal' ><div class='form-group'>"
	v+="<label class='control-label col-sm-2 text-primary' for='fnm' > Folder Name: </label>"
	v+="<div class='col-sm-4'>"
	v+="<input type='text' id='fnm' name='fnm' placeholder='Add New Folder' class='form-control' />"
	v+="<input type='hidden' id='batch' name='batch' value='"+Batch+"' class='form-control' />"
	v+="<input type='hidden' id='subject' name='subject' value='"+Subject+"' class='form-control' />"
	v+="<input type='hidden' id='fnm' name='fnm' value='"+FolderName+"' class='form-control' />"
	v+="<button type=submit class='btn btn-info' class='form-control'>Submit</button></div></div></form>"
	
	v+="<table class='table'><tr><th class='info'>Name</th><th class='success'>open folder</th>"
	for rec in qs:
		v+="<tr><td  class='info'>"+rec.folderName+"</td><td class='success'><a href=matterOpen?batch="+rec.batch+"&sub="+rec.subject+"&fnm="+rec.folderName+"  >open folder</a></td>"
	v+="</table>"
	
	resp=HttpResponse(v)
	return(resp)
