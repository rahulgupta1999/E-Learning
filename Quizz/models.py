from django.db import models
class Institute(models.Model):
	instName=models.CharField(max_length=50)
	password=models.CharField(max_length=50)
	type=models.CharField(max_length=50)
	email=models.CharField(max_length=50,primary_key=True)
	address=models.CharField(max_length=150)
	city=models.CharField(max_length=150)
	contact=models.CharField(max_length=150)
class Batch(models.Model):
	class Meta:
		unique_together=(('instName','batchName'))
	instName=models.CharField(max_length=50)
	batchName=models.CharField(max_length=50,primary_key=True)

class Student(models.Model):
	instName=models.CharField(max_length=50)
	stuName=models.CharField(max_length=50)
	email=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(max_length=50)
	batch=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	dateofBirth=models.DateField()
	address=models.CharField(max_length=50)
	
class Subject(models.Model):
	class Meta:
		unique_together=(('instName','batch','subject'))
	instName=models.CharField(max_length=50)
	batch=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	teacher=models.CharField(max_length=50)
	teacherEmail=models.CharField(max_length=50)
class Instructor(models.Model):
	instName=models.CharField(max_length=50)
	Name=models.CharField(max_length=50)
	email=models.CharField(max_length=50,primary_key=True)
	password=models.CharField(max_length=50)
	gender=models.CharField(max_length=50)
	dateofBirth=models.DateField()
	address=models.CharField(max_length=50)
	designation=models.CharField(max_length=50)

class Quiz(models.Model):
	instName=models.CharField(max_length=50)
	quizName=models.CharField(max_length=50)
	batch=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	teacher=models.CharField(max_length=50)
	question=models.CharField(max_length=50)
	ans1=models.CharField(max_length=50)
	ans2=models.CharField(max_length=50)
	ans3=models.CharField(max_length=50)
	ans4=models.CharField(max_length=50)
	correct=models.CharField(max_length=50)	
	points=models.IntegerField(default=1)	
class ReadyQuiz(models.Model):
	class Meta:
		unique_together=(('instName','batch','subject','quizName'))
	instName=models.CharField(max_length=50)
	quizName=models.CharField(max_length=50)
	batch=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	teacher=models.CharField(max_length=50)
	attempts=models.CharField(max_length=50)
	time=models.CharField(max_length=50)

class QuizResult(models.Model):
	instName=models.CharField(max_length=50)
	quizName=models.CharField(max_length=50)
	batch=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	teacher=models.CharField(max_length=50)
	correctAnswer=models.CharField(max_length=50)
	totalPoints=models.CharField(max_length=50)
	quizDate=models.DateField(max_length=50)
	quizTime=models.CharField(max_length=50)
	stuEmail=models.CharField(max_length=50)
	totalQues=models.CharField(max_length=50)

class StudyFolder(models.Model):
	class Meta:
		unique_together=(('instName','batch','subject','teacherEmail','folderName'))
	instName=models.CharField(max_length=50)
	batch=models.CharField(max_length=50)
	subject=models.CharField(max_length=50)
	teacherEmail=models.CharField(max_length=50)
	folderName=models.CharField(max_length=50)
	