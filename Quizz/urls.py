
from . import views
from django.urls import path

urlpatterns = [
	path('index',views.index),
   path('register',views.register),
   path('registerSave',views.registerSave),
   path('login',views.login),
   path('studentLogin',views.studentLogin),
   path('instituteLogin',views.instituteLogin),
   path('instructorLogin',views.instructorLogin),
   path('loginCheckInstitute',views.loginCheckInstitute),   path('loginCheckStudent',views.loginCheckStudent),path('loginCheckInstructor',views.loginCheckInstructor),
   path('addOpen',views.addOpen),path('quizOpen',views.quizOpen),
   path('batchSave',views.batchSave),path('quizSave',views.quizSave),
path('getBatch',views.getBatch),path('getSubject',views.getSubject),path('getBatchFromTeacher',views.getBatchFromTeacher),
path('stuSave',views.stuSave),path('subjectSave',views.subjectSave),path('instructSave',views.instructSave),path('getTeacher',views.getTeacher),
path('classRoom',views.classRoom),
path('homeBack',views.homeBack),path('getquiz',views.getquiz),
path('getQuiz',views.getQuiz),path('loadInput',views.loadInput),
path('QuestionBankOpen',views.QuestionBankOpen),path('answerBank',views.answerBank),path('forgot',views.forgot),path('getPassword',views.getPassword),
path('delQuestion',views.delQuestion),path('stuList',views.stuList),path('getBatchForStudent',views.getBatchForStudent),path('getStudentList',views.getStudentList),

path('changepasswordOpen',views.changepasswordOpen),path('changepassword',views.changepassword),path('quizList',views.quizList),
path('startQuiz',views.startQuiz),path('setupQuiz',views.setupQuiz),path('quizActivate',views.quizActivate),path('getQuizForSetup',views.getQuizForSetup)
,path('resultSave',views.resultSave),path('quizDeactivate',views.quizDeactivate),path('deactivateOpen',views.deactivateOpen),
path('getactivateQuiz',views.getactivateQuiz),path('profile',views.profile),path('getStuProfile',views.getStuProfile),
 path('intsructProfile',views.intsructProfile), path('getTeacherList',views.getTeacherList),path('teacherList',views.teacherList),
path('getInstructProfile',views.getInstructProfile),path('scorecardStudent',views.scorecardStudent),path('scorecardInstructor',views.scorecardInstructor),
path('scorecardOpen',views.scorecardOpen),path('studyMaterial',views.studyMaterial),path('materialList',views.materialList),path('addFolder',views.addFolder),

 ]

