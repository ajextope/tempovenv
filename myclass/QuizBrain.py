

class Quiz():
    def __init__(self, __questions):
        self.questions=__questions
        self.question_no = 0
        self.score= 0
        self.current_question = None
    
    def isComplete(self):
        """To check if the quiz has more questions"""
        return self.question_no < len(self.questions)
    
    def next_question(self):
        """Get the next question by incrementing the question number"""
        
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_item
        return f"Q.{self.question_no}: {q_text}"
    
    def prev_question(self):
        """Get the previous question by decrementing the question number"""
        
        self.current_question = self.questions[self.question_no]
        self.question_no -= 1
        q_text = self.current_question.question_item
        return f"Q.{self.question_no}: {q_text}"
    
    def check_answer(self, user_answer):
        """Check the user answer against the correct answer and maintain the score"""
        
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
        
    def get_scores(self):
        wrong =int(self.question_no) - int(self.score)
        percentage = int(self.score/ self.question_no * 100)
        return (wrong,self.score, percentage)
       
    
        
        
        
        