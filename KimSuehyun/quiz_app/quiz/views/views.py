from flask import request, redirect, url_for, render_template, flash, session
import os
import random
from quiz import app

quizSet = []
randRange = []

def readQuestion():
  global quizSet

  quizSet = []
  data = None
  parent_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
  filePath = os.path.join(parent_dir, 'quiz.txt')

  with open(filePath, 'r') as inputData:
    data = inputData.read().split('\n')

  questions = {}
  count = 0
  for line in data:
    if (len(line)<=0):
      break
    if count % 2 == 0:
      if (len(line)<=1):
        break
      questions = {}
      questions['Q'] = line
    else:
      questions['A'] = line
      quizSet.append(questions)
    count += 1

@app.route('/', methods=['POST','GET'])
def index():
  return render_template('index.html')

@app.route('/start', methods=['GET','POST'])
def question():
  global randRange
  global quizSet

  readQuestion()
  randRange = [i for i in range(len(quizSet))]
  questionNum = random.choice(randRange)
  question = quizSet[questionNum]['Q']
  attempted = 0
  return render_template('display.html', score=0, questionNum=questionNum, question=question, attempted=attempted)

@app.route('/question', methods=['GET','POST'])
def nextQuestion():
  global randRange
  global quizSet

  questionNum = int(request.args.get('questionNum'))
  score = int(request.args.get('score'))
  answer = request.args.get('question')
  attempted = int(request.args.get('attempted'))
  question = quizSet[questionNum]
  if answer == question['A']:
    score += 1
    isCorrect = '正解'
  else:
    isCorrect = '不正解'

  correctAnswer = question['A']
  return render_template('answer.html', score=score, questionNum=questionNum, question=question['Q'],attempted=attempted, answer=correctAnswer, entered=answer, isCorrect=isCorrect)

@app.route('/answer', methods=['GET','POST'])
def nextAnswer():
  global randRange
  global quizSet

  questionNum = int(request.args.get('questionNum'))
  score = int(request.args.get('score'))
  attempted = int(request.args.get('attempted'))
  isCorrect = request.args.get('isCorrect')

  attempted += 1
  randRange.remove(questionNum)
  if (len(randRange)<=0):
    percent = round((score/attempted)*100)
    return render_template('score.html', score=score, attempted=attempted-1, percent=percent)
  
  questionNum = random.choice(randRange)
  question = quizSet[questionNum]
  return render_template('display.html', score=score, questionNum=questionNum, question=question['Q'],attempted=attempted)